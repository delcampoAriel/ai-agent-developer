import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from dataclasses import asdict, dataclass

@dataclass
class Medicion:
    modelo: str
    tokens_estimados_entrada: int
    tokens_reales_entrada: int | None
    tokens_salida: int | None
    tokens_totales: int | None

def estimar_costo(
    input_tokens: int,
    output_tokens: int,
    input_usd_por_millon: float,
    output_usd_por_millon: float,
) -> float:
    return (
        input_tokens / 1_000_000 * input_usd_por_millon
        + output_tokens / 1_000_000 * output_usd_por_millon
    )

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

input_tokens = medicion.tokens_reales_entrada or 0
output_tokens = medicion.tokens_salida or 0

# Consultá la página oficial y reemplazá ambos valores.
precio_input = 3.00
precio_output = 15.00

costo_ejecucion = estimar_costo(
    input_tokens=input_tokens,
    output_tokens=output_tokens,
    input_usd_por_millon=precio_input,
    output_usd_por_millon=precio_output,
)

print(f"Costo estimado por ejecución: USD {costo_ejecucion:.8f}")
print(f"Costo estimado por 10.000 ejecuciones: USD {costo_ejecucion * 10_000:.2f}")

# REPSUESTA QUE INTERESA
# Costo estimado por ejecución: USD 0.00767100
# Costo estimado por 10.000 ejecuciones: USD 76.71