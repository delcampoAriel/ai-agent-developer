import os
from dataclasses import asdict, dataclass

from dotenv import load_dotenv
from google import genai
from google.genai import types


@dataclass
class Medicion:
    modelo: str
    tokens_estimados_entrada: int
    tokens_reales_entrada: int | None
    tokens_salida: int | None
    tokens_totales: int | None


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

if not api_key:
    raise RuntimeError("Falta GEMINI_API_KEY en el archivo .env")

client = genai.Client(api_key=api_key)

prompt = """
Una empresa recibe reclamos por email y necesita clasificarlos,
consultar el estado del cliente y crear un ticket cuando corresponda.
Indicá si conviene comenzar con un chatbot, un workflow o un agente.
Justificá la decisión con tres criterios técnicos.
""".strip()

# 1. Contar tokens antes de generar
conteo = client.models.count_tokens(
    model=model,
    contents=prompt,
)

print("Tokens estimados de entrada:", conteo.total_tokens)
# print(conteo.model_dump_json(indent=4))

# 2. Generar la respuesta
response = client.models.generate_content(
    model=model,
    contents=prompt,
    config=types.GenerateContentConfig(
        system_instruction=(
            "Sos arquitecto de soluciones de IA. "
            "Priorizá la alternativa más simple que resuelva el problema."
        ),
        temperature=0.2,
        max_output_tokens=500,
    ),
)

print("\nRespuesta:\n", response.text)

# 3. Leer metadatos reales informados por la API
usage = response.usage_metadata

medicion = Medicion(
    modelo=model,
    tokens_estimados_entrada=conteo.total_tokens,
    tokens_reales_entrada=getattr(usage, "prompt_token_count", None),
    tokens_salida=getattr(usage, "candidates_token_count", None),
    tokens_totales=getattr(usage, "total_token_count", None),
)

print("\nMedición:")
for clave, valor in asdict(medicion).items():
    print(f"- {clave}: {valor}")


# PRINT DE LA RESPONSE DE GOOGLE SDK
# {
#     "sdk_http_response": {
#         "headers": {
#             "content-type": "application/json; charset=UTF-8",
#             "vary": "Origin, X-Origin, Referer",
#             "content-encoding": "gzip",
#             "date": "Sun, 12 Jul 2026 22:25:38 GMT",
#             "server": "scaffolding on HTTPServer2",
#             "x-xss-protection": "0",
#             "x-frame-options": "SAMEORIGIN",
#             "x-content-type-options": "nosniff",
#             "server-timing": "gfet4t7; dur=914",
#             "alt-svc": "h3=\":443\"; ma=2592000,h3-29=\":443\"; ma=2592000",
#             "transfer-encoding": "chunked"
#         },
#         "body": null
#     },
#     "total_tokens": 55,
#     "cached_content_token_count": null
# }
# ---
# ---
# SALIDAS DEL SCRIPT
# Tokens estimados de entrada: 55
# ---
# Respuesta:
#  Como arquitecto de soluciones, mi recomendación es comenzar con un **Workflow de Automatización (Orquestador)**.
# En lugar de construir una interfaz conversacional (chatbot) o un sistema autónomo complejo (agente), la solución más eficiente es un flujo de trabajo que conecte los sistemas existentes mediante APIs.
# ¿Por qué un Workflow?
# El problema describe un proceso lineal y determinista: **Recibir -> Clasificar -> Consultar -> Crear Ticket**. Un workflow permite orquestar estos pasos sin la incertidumbre de un modelo generativo en cada etapa.
# ---
# ### Justificación técnica (3 criterios)
# #### 1. Determinismo y Trazabilidad
# Un workflow permite definir reglas de negocio claras (ej: "si el cliente es VIP, priorizar"). A diferencia de un agente autónomo, donde el razonamiento puede variar, el workflow garantiza que cada email pase por el mismo proceso de validación. Esto facilita el *debugging* y asegura que ningún reclamo se pierda en una "alucinación" del modelo.
# #### 2. Menor latencia y costo (Eficiencia)
# No necesitas un LLM para todo. Puedes usar un clasificador ligero (o incluso reglas basadas en palabras clave) para categorizar el email, y solo invocar un LLM si la clasificación es ambigua. Esto reduce drásticamente el consumo de tokens y el tiempo de respuesta en comparación con un agente que debe "pensar" cada paso del proceso.
# #### 3. Integración nativa con sistemas legados
# La consulta del estado del cliente y la creación del ticket suelen residir en CRMs (Salesforce, Zendesk, HubSpot). Los motores de workflow (como n8n, Make o Zapier) tienen conectores nativos para estas herramientas. Intentar que un agente gestione estas integraciones mediante llamadas a funciones (*function calling*) añade una capa de complejidad innecesaria y puntos de falla adicionales.
# ---
# ### Hoja de ruta sugerida:
# 1. **Capa de Clasificación:** Un modelo pequeño (o un prompt simple) que extraiga la intención y el ID del cliente del email.
# 2. **Capa de Integración (Workflow):** El motor de workflow consulta el CRM con el ID extraído.
# 3. **Capa de Acción:** Si el cliente existe y el reclamo es válido, el workflow dispara la API de creación
# Medición:
# - modelo: gemini-3.1-flash-lite
# - tokens_estimados_entrada: 55
# - tokens_reales_entrada: 77
# - tokens_salida: 496
# - tokens_totales: 573