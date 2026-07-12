import os

from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

if not api_key:
    raise RuntimeError(
        "Falta GEMINI_API_KEY. Creá el archivo .env antes de continuar."
    )

client = genai.Client(api_key=api_key)

prompt = """
Explicá en no más de 80 palabras la diferencia entre
un chatbot y un agente de IA. Incluí un ejemplo de cada uno.
""".strip()

response = client.models.generate_content(
    model=model,
    contents=prompt,
    config=types.GenerateContentConfig(
        system_instruction=(
            "Sos docente de ingeniería de IA. "
            "Respondé con precisión, claridad y sin exageraciones."
        ),
        temperature=0.2,
        max_output_tokens=300,
    ),
)

print("MODELO:", model)
print("\nRESPUESTA:\n")
print(response.text)
