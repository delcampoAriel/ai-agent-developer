import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

if not api_key:
    raise RuntimeError("Falta GEMINI_API_KEY en el archivo .env")

client = genai.Client(api_key=api_key)

prompts = {
    "español": "Explicá qué es un agente de inteligencia artificial.",
    "inglés": "Explain what an artificial intelligence agent is.",
    "código": "def calcular_total(precios): return sum(precios)",
    "json": '{"cliente": 42, "estado": "pendiente", "monto": 1500.50}',
}

for nombre, contenido in prompts.items():
    conteo = client.models.count_tokens(
        model=model,
        contents=contenido,
    )
    char_count=len(contenido.replace(" ", ""))
    token_count=conteo.total_tokens
    print(f"{nombre:8} | caracteres: {char_count:4} | tokens: {token_count:4} | caracteres/tokens: {char_count/token_count}")
    

# RESUTADOS:
# español  | caracteres:   45 | tokens:   12 | caracteres/tokens: 3.75
# inglés   | caracteres:   43 | tokens:    9 | caracteres/tokens: 4.777777777777778
# código   | caracteres:   45 | tokens:   15 | caracteres/tokens: 3.0
# json     | caracteres:   51 | tokens:   27 | caracteres/tokens: 1.8888888888888888
