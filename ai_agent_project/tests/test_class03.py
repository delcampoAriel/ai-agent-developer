from __future__ import annotations

import asyncio
from unittest.mock import AsyncMock

from ai_agent_course.app import ConversationApp, route_by_privacy_or_cost
from ai_agent_course.conversation import ConversationSession
from ai_agent_course.errors import ProviderConfigurationError
from ai_agent_course.providers import FakeProvider, GenerationResult
from ai_agent_course.resilience import generate_with_resilience
from ai_agent_course.runtime import JsonlTraceStore
from ai_agent_course.settings import Settings


async def check_fake_provider_contract():
    result = await FakeProvider(delay_seconds=0).agenerate("hola")
    assert result.provider == "fake"
    assert result.text
    assert result.input_tokens > 0


async def check_retry_transient_error():
    provider = FakeProvider(delay_seconds=0, failures=["rate_limit"])
    outcome = await generate_with_resilience(
        provider,
        "mensaje válido",
        timeout_seconds=0.2,
        max_retries=1,
        base_delay_seconds=0,
    )
    assert outcome.attempts == 2
    assert len(outcome.retries) == 1


async def check_configuration_error_is_not_retried():
    provider = FakeProvider(delay_seconds=0, failures=["config"])
    try:
        await generate_with_resilience(
            provider,
            "mensaje válido",
            timeout_seconds=0.2,
            max_retries=3,
            base_delay_seconds=0,
        )
    except ProviderConfigurationError:
        return
    raise AssertionError("Se esperaba ProviderConfigurationError")


async def check_async_mock_called_once():
    provider = type("ProviderMock", (), {})()
    provider.agenerate = AsyncMock(
        return_value=GenerationResult(
            text="respuesta mock",
            model="mock-model",
            provider="mock",
            latency_ms=1,
            input_tokens=2,
            output_tokens=2,
        )
    )
    outcome = await generate_with_resilience(
        provider,
        "mensaje válido",
        timeout_seconds=0.2,
        max_retries=1,
        base_delay_seconds=0,
    )
    provider.agenerate.assert_awaited_once()
    assert outcome.result.text == "respuesta mock"


def test_fake_provider_contract():
    asyncio.run(check_fake_provider_contract())


def test_retry_transient_error():
    asyncio.run(check_retry_transient_error())


def test_configuration_error_is_not_retried():
    asyncio.run(check_configuration_error_is_not_retried())


def test_async_mock_called_once():
    asyncio.run(check_async_mock_called_once())


def test_history_window():
    session = ConversationSession(max_turns=1)
    session.add("user", "mensaje uno")
    session.add("assistant", "respuesta uno")
    session.add("user", "mensaje dos")
    session.add("assistant", "respuesta dos")
    assert len(session.messages) == 4
    assert len(session.recent_messages()) == 2


def test_route_prefers_local_for_sensitive_text():
    route = route_by_privacy_or_cost("¿Cuál es mi contraseña guardada?")
    assert route.provider_key == "local"


def test_route_prefers_remote_when_budget_available():
    route = route_by_privacy_or_cost("Resumí este artículo", budget_remaining_usd=1.0)
    assert route.provider_key == "remote"


def test_route_falls_back_to_local_when_budget_exhausted():
    route = route_by_privacy_or_cost("Resumí este artículo", budget_remaining_usd=0.0)
    assert route.provider_key == "local"


async def check_app_routes_sensitive_message_to_local_at_zero_cost(tmp_path):
    local_provider = FakeProvider(model="fake-local", delay_seconds=0)
    remote_provider = FakeProvider(model="fake-remote", delay_seconds=0)
    app = ConversationApp(
        remote_provider,
        Settings(app_env="testing", use_real_gemini=False),
        JsonlTraceStore(tmp_path / "trace.jsonl"),
        providers={"local": local_provider, "remote": remote_provider},
        router=route_by_privacy_or_cost,
    )
    session = ConversationSession(max_turns=2)

    response = await app.ask(session, "Mi contraseña es 1234, ¿la guardo así?")

    assert response.model == "fake-local"
    assert response.estimated_cost_usd == 0.0


def test_app_routes_sensitive_message_to_local_at_zero_cost(tmp_path):
    asyncio.run(check_app_routes_sensitive_message_to_local_at_zero_cost(tmp_path))


async def check_app_routes_normal_message_to_remote_with_cost(tmp_path):
    local_provider = FakeProvider(model="fake-local", delay_seconds=0)
    remote_provider = FakeProvider(model="fake-remote", delay_seconds=0)
    app = ConversationApp(
        remote_provider,
        Settings(app_env="testing", use_real_gemini=False),
        JsonlTraceStore(tmp_path / "trace.jsonl"),
        providers={"local": local_provider, "remote": remote_provider},
        router=route_by_privacy_or_cost,
        budget_usd=1.0,
    )
    session = ConversationSession(max_turns=2)

    response = await app.ask(session, "Resumí las ventajas de usar streaming")

    assert response.model == "fake-remote"
    assert response.estimated_cost_usd > 0.0


def test_app_routes_normal_message_to_remote_with_cost(tmp_path):
    asyncio.run(check_app_routes_normal_message_to_remote_with_cost(tmp_path))
