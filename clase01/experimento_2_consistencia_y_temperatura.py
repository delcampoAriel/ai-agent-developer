import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

def generar_con_temperatura(temperatura: float) -> str:
    response = client.models.generate_content(
        model=model,
        contents=(
            "Proponé tres nombres para una aplicación que coordina "
            "agentes de análisis financiero."
        ),
        config=types.GenerateContentConfig(
            temperature=temperatura,
            max_output_tokens=150,
        ),
    )
    return response.text

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

if not api_key:
    raise RuntimeError("Falta GEMINI_API_KEY en el archivo .env")

client = genai.Client(api_key=api_key)

for temperatura in (0.0, 0.5, 1.0):
    print(f"\nTEMPERATURA: {temperatura}")
    print(generar_con_temperatura(temperatura))
    
# RESPUESTA DEL SCRIPT

# TEMPERATURA: 0.0
# Para proponer nombres efectivos, he buscado conceptos que transmitan **precisión, inteligencia colectiva y fluidez**. Aquí tienes tres opciones con enfoques distintos:
# 1. Synapse Finance
# El concepto: La sinapsis es el punto de conexión donde se transmite la información entre neuronas.
# Por qué funciona: Sugiere que la aplicación no solo tiene agentes individuales, sino que los conecta para que trabajen como un solo "cerebro" financiero. Es un nombre moderno, tecnológico y fácil de recordar.
# 2. Orchestral (o Orchestral AI)
# El concepto: La orquestación implica coordinar múltiples elementos (instrument

# TEMPERATURA: 0.5
# Para elegir el nombre ideal, es importante considerar si buscas algo que suene tecnológico, profesional o enfocado en la eficiencia. Aquí tienes tres propuestas con enfoques distintos:
# 1. FinSync (Enfoque en coordinación)
# Por qué funciona:** Es una combinación de *Finance* y *Sync* (sincronización). Transmite la idea de que múltiples agentes están trabajando al unísono, alineando datos y estrategias de forma fluida. Es corto, moderno y fácil de recordar.
# 2. QuantHive (Enfoque en inteligencia colectiva)
# Por qué funciona:** *Quant* hace referencia al análisis cuantitativo (el núcleo del análisis financiero

# TEMPERATURA: 1.0
# Aquí tienes tres propuestas de nombres, cada una con un enfoque distinto según la identidad que busques para la aplicación:
# 1. FinSync (Enfoque en eficiencia y coordinación)
# Por qué funciona:** Es un nombre corto, moderno y fácil de recordar. La combinación de "Fin" (Finanzas) y "Sync" (Sincronización) transmite inmediatamente la idea de que la aplicación es el eje central que mantiene a todos los agentes financieros trabajando en la misma dirección y al mismo tiempo.
# Ideal para:** Una plataforma centrada en la automatización de procesos y la gestión de flujos de trabajo en equipo.
# 2. Axiom Core (Enfo

# Preguntas:
# ¿Qué configuración produjo respuestas más similares entre ejecuciones?
# ¿Cuál elegirías para extraer datos de una factura?
# ¿Cuál podría ser útil para una lluvia de ideas?
# ¿La temperatura cambió el conocimiento disponible o solamente el patrón de generación?