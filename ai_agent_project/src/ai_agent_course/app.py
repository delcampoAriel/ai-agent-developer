from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Callable
import time
import uuid

from .conversation import ConversationSession
from .errors import PartialStreamError
from .resilience import RetryEvent, generate_with_resilience
from .runtime import JsonlTraceStore


@dataclass(frozen=True)
class ChatResponse:
    run_id: str
    session_id: str
    text: str
    attempts: int
    provider: str
    model: str
    latency_ms: float
    input_tokens: int
    output_tokens: int
    estimated_cost_usd: float

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass(frozen=True)
class StreamChatResponse:
    run_id: str
    session_id: str
    text: str
    chunks: int
    first_chunk_ms: float
    total_ms: float
    provider: str
    model: str

    def to_dict(self) -> dict:
        return asdict(self)


SENSITIVE_TERMS = (
    "contraseña",
    "password",
    "api key",
    "tarjeta",
    "dni",
    "cbu",
    "cuenta bancaria",
)


@dataclass(frozen=True)
class ProviderRoute:
    """Decisión de a qué provider enviar un mensaje, y por qué."""

    provider_key: str
    reason: str

    def to_dict(self) -> dict:
        return asdict(self)


def route_by_privacy_or_cost(
    user_text: str,
    *,
    budget_remaining_usd: float | None = None,
) -> ProviderRoute:
    """Elige provider según privacidad primero, costo después.

    `budget_remaining_usd=None` significa "sin presupuesto configurado":
    nunca fuerza el fallback local por costo, solo por privacidad.
    """
    lowered = user_text.lower()
    if any(term in lowered for term in SENSITIVE_TERMS):
        return ProviderRoute(
            "local",
            "el mensaje contiene datos sensibles: se evita enviarlo a un provider externo",
        )
    if budget_remaining_usd is not None and budget_remaining_usd <= 0:
        return ProviderRoute(
            "local",
            "presupuesto agotado: se usa el provider local sin costo",
        )
    return ProviderRoute(
        "remote",
        "sin datos sensibles y con presupuesto disponible: se prioriza calidad",
    )


class ConversationApp:
    def __init__(
        self,
        provider,
        settings,
        trace_store: JsonlTraceStore,
        *,
        providers: dict[str, object] | None = None,
        router: Callable[..., ProviderRoute] | None = None,
        budget_usd: float | None = None,
    ):
        self.provider = provider
        self.providers = providers or {"default": provider}
        self.router = router
        self.settings = settings
        self.trace_store = trace_store
        self.budget_usd = budget_usd
        self.spent_usd = 0.0

    def _estimate_cost(self, provider_key: str, input_tokens: int, output_tokens: int) -> float:
        if provider_key == "local":
            return 0.0
        return round(
            input_tokens / 1_000_000 * self.settings.input_usd_per_million
            + output_tokens / 1_000_000 * self.settings.output_usd_per_million,
            8,
        )

    def _select_provider(self, user_text: str) -> tuple[object, ProviderRoute]:
        if self.router is None:
            return self.provider, ProviderRoute("default", "sin routing configurado")
        remaining = None if self.budget_usd is None else max(self.budget_usd - self.spent_usd, 0.0)
        route = self.router(user_text, budget_remaining_usd=remaining)
        provider = self.providers.get(route.provider_key, self.provider)
        return provider, route

    def _start_run(
        self,
        *,
        run_id: str,
        session: ConversationSession,
        mode: str,
        provider: object,
        route: ProviderRoute,
    ) -> None:
        self.trace_store.append(
            run_id=run_id,
            session_id=session.session_id,
            event="run.started",
            payload={
                "mode": mode,
                "provider": type(provider).__name__,
                "model": getattr(provider, "model", "unknown"),
                "history_messages": len(session.recent_messages()),
            },
        )
        self.trace_store.append(
            run_id=run_id,
            session_id=session.session_id,
            event="routing.selected",
            payload=route.to_dict(),
        )

    async def ask(
        self,
        session: ConversationSession,
        user_text: str,
        *,
        system: str = "Sos un asistente útil, preciso y breve.",
    ) -> ChatResponse:
        clean_text = user_text.strip()
        if not clean_text:
            raise ValueError("El mensaje no puede estar vacío")

        run_id = str(uuid.uuid4())
        prompt = session.build_prompt(clean_text)
        provider, route = self._select_provider(clean_text)
        self._start_run(run_id=run_id, session=session, mode="async", provider=provider, route=route)

        def on_retry(event: RetryEvent) -> None:
            self.trace_store.append(
                run_id=run_id,
                session_id=session.session_id,
                event="llm.retry",
                payload=asdict(event),
            )

        try:
            outcome = await generate_with_resilience(
                provider,
                prompt,
                system=system,
                timeout_seconds=self.settings.request_timeout_seconds,
                max_retries=self.settings.max_retries,
                base_delay_seconds=self.settings.retry_base_delay_seconds,
                on_retry=on_retry,
            )
            result = outcome.result
            session.add("user", clean_text)
            session.add("assistant", result.text)

            cost = self._estimate_cost(route.provider_key, result.input_tokens, result.output_tokens)
            self.spent_usd += cost

            response = ChatResponse(
                run_id=run_id,
                session_id=session.session_id,
                text=result.text,
                attempts=outcome.attempts,
                provider=result.provider,
                model=result.model,
                latency_ms=result.latency_ms,
                input_tokens=result.input_tokens,
                output_tokens=result.output_tokens,
                estimated_cost_usd=cost,
            )
            self.trace_store.append(
                run_id=run_id,
                session_id=session.session_id,
                event="run.completed",
                payload=response.to_dict(),
            )
            return response
        except Exception as exc:
            self.trace_store.append(
                run_id=run_id,
                session_id=session.session_id,
                event="run.failed",
                payload={"error_type": type(exc).__name__, "message": str(exc)},
            )
            raise

    async def ask_stream(
        self,
        session: ConversationSession,
        user_text: str,
        *,
        system: str = "Sos un asistente útil, preciso y breve.",
    ) -> StreamChatResponse:
        clean_text = user_text.strip()
        if not clean_text:
            raise ValueError("El mensaje no puede estar vacío")

        run_id = str(uuid.uuid4())
        prompt = session.build_prompt(clean_text)
        provider, route = self._select_provider(clean_text)
        self._start_run(run_id=run_id, session=session, mode="stream", provider=provider, route=route)

        started = time.perf_counter()
        chunks: list[str] = []
        first_chunk_ms: float | None = None

        try:
            async for chunk in provider.astream(prompt, system=system):
                chunks.append(chunk)
                if first_chunk_ms is None:
                    first_chunk_ms = round((time.perf_counter() - started) * 1000, 2)
        except Exception as exc:
            if chunks:
                error = PartialStreamError(
                    f"El stream falló después de {len(chunks)} fragmentos: {exc}"
                )
            else:
                error = exc
            self.trace_store.append(
                run_id=run_id,
                session_id=session.session_id,
                event="run.failed",
                payload={"error_type": type(error).__name__, "message": str(error)},
            )
            raise error

        text = "".join(chunks).strip()
        total_ms = round((time.perf_counter() - started) * 1000, 2)
        session.add("user", clean_text)
        session.add("assistant", text)

        response = StreamChatResponse(
            run_id=run_id,
            session_id=session.session_id,
            text=text,
            chunks=len(chunks),
            first_chunk_ms=first_chunk_ms or total_ms,
            total_ms=total_ms,
            provider="gemini" if type(provider).__name__ == "GeminiProvider" else "fake",
            model=getattr(provider, "model", "unknown"),
        )
        self.trace_store.append(
            run_id=run_id,
            session_id=session.session_id,
            event="run.completed",
            payload=response.to_dict(),
        )
        return response
