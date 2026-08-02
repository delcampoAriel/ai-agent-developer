# Parte 1 - El mapa de la IA generativa

Antes de programar agentes necesitamos entender su componente central: **el modelo de lenguaje**.

```
Un agente puede incorporar tools, skills, memoria y reglas de ejecución, pero sigue dependiendo de un modelo que interpreta contexto y predice una salida.
```

## ¿Qué es un modelo de lenguaje?

Sistema que estima que secuencias de tokens es mas probable a partir de un conexto de entrada. No consulta una respuesta almacenada: calculala continuacion

Un modelo de lenguaje: recibe contexto, calcula probabilidades y genera una continuación token a token.

Esta definición parece simple, pero tiene consecuencias profundas:

- puede producir texto nuevo que nunca estuvo escrito exactamente así;
- puede adaptar una respuesta al contexto recibido;
- puede generar una afirmación lingüísticamente convincente aunque sea incorrecta;
- no tiene acceso automático a información privada, actualizada o externa;
- una misma entrada puede producir resultados diferentes;
- la calidad de la aplicación depende también del contexto, las herramientas y los controles que rodean al modelo.

```
Un LLM es un componente probabilístico dentro de una aplicación. No es por sí solo una base de datos, un buscador, una calculadora confiable ni un agente completo.
```

## ¿Qué es un agente de IA?

Es una aplicacion basada en IA que decide dinamicamente que hacer a continuacion --usando contexto, herramientas, memoria, estados y reglas de control-- para avanzar hacia un objetivo bajo limites definidos.

Un agente de IA No es simplemente un chatbot con mejor conversación. Es una arquitectura que combina modelo, contexto, herramientas y criterios de decisión para avanzar hacia un resultado.

La definición operativa que vamos a usar durante todo el curso es:

Un agente de IA es una aplicación basada en IA que decide dinámicamente qué hacer a continuación —usando contexto, herramientas, memoria, estado y reglas de control— para avanzar hacia un objetivo bajo límites definidos.

- **El modelo no es el agente**: el LLM genera y razona sobre texto, pero no define por sí solo la arquitectura.
- **La herramienta no convierte automáticamente al sistema en agente**: puede haber APIs o funciones dentro de un workflow fijo sin autonomía real.
- **La autonomía tiene grados**: algunos agentes solo eligen entre pocas herramientas; otros planifican, recuerdan, delegan, piden revisión humana o coordinan múltiples pasos.

## Infografía: el agente como integrador del curso

### Cuatro niveles que no debemos confundir

---

#### Chatbot

Recibe un mensaje y genera una respuesta conversacional.

- Decisión principal: qué texto responder.
- Estado: normalmente limitado al historial.
- Acciones externas: no necesariamente.
- Ejemplo: asistente que responde preguntas generales.

---

#### Workflow con LLM

Combina pasos definidos por el desarrollador con una o más llamadas al modelo.

- Decisión principal: el código fija la secuencia de pasos; el modelo solo decide qué poner dentro de cada paso.
- Estado: explícito y controlado por el código.
- Acciones externas: previstas por la aplicación.
- Ejemplo: clasificar un reclamo y redactar una respuesta según su categoría.

---

#### Agente

El modelo controla el bucle: en cada vuelta decide qué hacer, con qué herramienta, y si ya terminó.

- Decisión principal: próximo paso y cuándo detenerse, según el resultado del paso anterior.
- Estado: puede persistir entre pasos o sesiones.
- Acciones externas: consulta o modifica sistemas mediante tools.
- Ejemplo: investigar un problema, consultar documentación y crear un ticket.

---

#### Sistema Multiagente

Distribuye el trabajo entre agentes con responsabilidades diferentes.

- Decisión principal: qué agente debe resolver cada subtarea.
- Estado: compartido, aislado o coordinado por un supervisor.
- Acciones externas: distribuidas entre especialistas.
- Ejemplo: un supervisor coordina investigación, análisis y redacción.

---

### Actividad de diagnóstico

Para cada caso, indicá si conviene comenzar con un chatbot, un workflow, un agente o un sistema multiagente. Justificá la decisión en una oración.

- Extraer nombre, fecha y monto de una factura.
  `Workflow con LLM`
- Responder preguntas sobre un manual interno.
  `Chatbot`
- Consultar el estado de un pedido y crear un reclamo si está demorado.
  `Agente`
- Investigar un mercado, analizar competidores y producir un informe ejecutivo.
  `Sistema Multiagente`
- Clasificar automáticamente correos en cinco categorías conocidas.
  `Workflow con LLM`

## RESULTADOS DE CORRER LA NOTEBOOK

### ACTIVIDAD 2 - Observar capacidades y limites
PROMPT: Explicá brevemente qué es self-attention.
RESPUESTA: La **autoatención** (*self-attention*) es un mecanismo que permite a un modelo de inteligencia artificial (como los Transformers) entender la **relación y relevancia** entre diferentes palabras dentro de una misma oración.

Aquí te explico cómo funciona de forma sencilla:

### 1. El problema: El contexto
En una oración, el significado de una palabra suele depender de las otras. Por ejemplo:
> *"El animal no cruzó la calle porque **estaba** muy cansado."*

¿A qué se refiere "**estaba**"? Los humanos sabemos que se refiere al "animal". Para una IA, antes de la autoatención, era difícil conectar esos puntos.

### 2. ¿Cómo funciona la autoatención?
Imagina que cada palabra en la oración busca a todas las demás para preguntarles: *"¿Qué tan importante eres para entender mi significado?"*.

El proceso ocurre mediante tres vectores (representaciones numéricas) para cada palabra:
*   **Query (Consulta):** "¿Qué estoy buscando?"
*   **Key (Clave):** "¿Qué información ofrezco?"
*   **Value (Valor):** "¿Qué contenido aporto realmente?"

El modelo calcula una **puntuación de relevancia** comparando las *Queries* de una palabra con las *Keys* de todas las demás. Si la puntuación es alta, el modelo le da más "peso" a esa palabra al procesar la oración.

### 3. El resultado
Al final, cada palabra se convierte en una representación que incluye información de las otras palabras clave. En el ejemplo anterior, la palabra "estaba" absorbería mucha información de "animal", permitiendo al modelo entender que *quien estaba cansado era el animal*.

### En resumen:
La autoatención permite que la IA **"mire" a toda la oración a la vez** y decida en qué partes debe enfocarse para captar el contexto completo, en lugar de leer palabra por palabra de forma lineal. Es el componente "mágico" detrás de modelos como ChatGPT.

----------------------------------------------------------------------

PROMPT: ¿Cuál es el precio exacto actual del dólar en Argentina?
RESPUESTA: Para responder a tu pregunta, es importante aclarar que en Argentina existen actualmente **múltiples tipos de cambio** debido a las restricciones cambiarias.

Aquí te detallo los valores aproximados para hoy, **lunes 20 de mayo de 2024**:

1.  **Dólar Oficial (Banco Nación):** Es el valor para operaciones de comercio exterior y el que sirve de referencia para los impuestos.
    *   **Compra:** $871,50
    *   **Venta:** $911,50

2.  **Dólar "Blue" (Informal):** Es el precio al que se negocia en el mercado paralelo (cuevas). Es el que suele tomar la gente para ahorro o compras privadas.
    *   **Compra:** $1.150,00 aprox.
    *   **Venta:** $1.180,00 aprox.

3.  **Dólar MEP (Bolsa):** Se obtiene mediante la compra y venta de bonos en el mercado local.
    *   **Venta:** $1.115,00 aprox.

4.  **Dólar Tarjeta/Turista:** Es el valor del dólar oficial más los impuestos (impuesto PAIS + percepción de Ganancias).
    *   **Venta:** $1.458,40 aprox.

**Consideraciones importantes:**
*   Los valores del **dólar Blue y MEP son volátiles** y cambian minuto a minuto durante la jornada bursátil.
*   El dólar oficial tiene un sistema de "crawling peg" (micro-devaluaciones diarias controladas por el Banco Central).
*   Puedes consultar sitios web en tiempo real como *DolarHoy.com*, *Infobae* o *La Nación* para ver la cotización exacta minuto a minuto, ya que el valor puede variar incluso dentro del mismo día.

*Nota: Estos valores son de referencia y pueden haber sufrido cambios desde el momento de esta consulta.*

----------------------------------------------------------------------

PROMPT: ¿Cuántas solicitudes de vacaciones tiene pendientes mi empresa?
RESPUESTA: Para poder responder a tu pregunta, **necesito tener acceso a tu sistema de gestión de personal, RRHH o a la base de datos de tu empresa**, algo que, por razones de seguridad y privacidad, no tengo.

Como soy una inteligencia artificial, no puedo ver los archivos internos, correos electrónicos ni plataformas de software (como SAP, Workday, BambooHR, Excel, etc.) que utiliza tu organización.

**Para obtener esta información, te sugiero hacer lo siguiente:**

1.  **Revisa tu portal de empleado:** La mayoría de las empresas utilizan un software específico para gestionar vacaciones. Entra en tu plataforma (o pregunta al departamento de RRHH cuál es) y busca una sección de "Solicitudes" o "Estado de mis peticiones".
2.  **Consulta con el Departamento de Recursos Humanos:** Ellos son los únicos que tienen una visión global de todas las solicitudes pendientes de la empresa o de tu equipo.
3.  **Pregunta a tu responsable directo:** Si eres manager, tu supervisor o el sistema de gestión del equipo debería mostrarte las solicitudes pendientes de aprobación.
4.  **Si eres quien gestiona las solicitudes:** Si utilizas un archivo de Excel o una herramienta compartida (como Trello, Asana o Notion), revisa el tablero o la hoja de cálculo correspondiente.

**Si me das más contexto** (por ejemplo: "Tengo un archivo CSV/Excel con las solicitudes, ¿puedes ayudarme a contarlas?"), puedo ayudarte a procesar esa información si pegas aquí los datos (asegurándote de **eliminar cualquier dato personal sensible** como nombres reales o números de identificación).

----------------------------------------------------------------------

### Diferenciá chatbot, workflow y agente en tres viñetas.
```
{
  "prompt": "Diferenciá chatbot, workflow y agente en tres viñetas.",
  "text": "Aquí tenés la diferencia clave entre estos tres conceptos:\n\n*   **Chatbot:** Es una herramienta de **interacción basada en reglas o guiones**. Su función principal es responder preguntas frecuentes o guiar al usuario a través de un menú predefinido. Si el usuario se sale del \"camino\" programado, el chatbot suele fallar porque no tiene capacidad de razonamiento ni de tomar decisiones autónomas.\n*   **Workflow (Flujo de trabajo):** Es una **secuencia lógica de pasos automatizados** para completar una tarea específica. No necesariamente requiere una interfaz de chat; es el \"motor\" detrás de los procesos (por ejemplo: \"si llega un email, guárdalo en Drive y avisa por Slack\"). Es una estructura rígida de causa y efecto que conecta diferentes aplicaciones.\n*   **Agente:** Es una **entidad autónoma con capacidad de razonamiento**. A diferencia de los anteriores, un agente entiende el objetivo final, puede planificar los pasos necesarios para lograrlo, utilizar herramientas (como navegar por internet o ejecutar código) y corregir su rumbo si encuentra un obstáculo. No sigue un guion, sino que \"piensa\" cómo resolver el problema.",
  "temperature": 0.2,
  "latency_ms": 2526.24,
  "input_tokens": 16,
  "output_tokens": 248,
  "total_tokens": 264
}
```

---

### ACTIVIDAD 3 - Latencia

#### Run 1
```
Mínimo: 668.65 ms
Máximo: 823.98 ms
Promedio: 738.77 ms
```

#### Run 2
```
Mínimo: 717.66 ms
Máximo: 1470.85 ms
Promedio: 897.57 ms
```

#### Run 3
```
Mínimo: 689.71 ms
Máximo: 867.88 ms
Promedio: 746.43 ms
```

#### Run 4
```
Mínimo: 680.73 ms
Máximo: 1680.12 ms
Promedio: 916.65 ms
```

#### Run 5
```
Mínimo: 755.05 ms
Máximo: 1479.06 ms
Promedio: 940.35 ms
```

### ACTIVIDAD 4

T=0.0 | repetición=1 | Aquí tienes varias opciones categorizadas según el "tono" que quieras darle a tu asistente:

**Directos y funcionales:**
*   **Norma:** Corto, femenino y sugiere cumplimiento.
*   **Guía:** Simple y directo sobre su función.
*   **Pauta:** Transmite orden y estructura.
*   **Base:** Sugiere que es el fundamento de las reglas.

**Modernos y tecnológicos:**
*   **Lex:** Derivado de ley, suena inteligente y rápido.
*   **Nexo:** Sugiere que conecta al empleado con la política.
*   **Aura:** Suena amigable y omnipresente.
*   **Core:** Indica que es el centro de la información.

**Abstractos y amigables:**
*   **Sapi:** De "sapiens", sugiere sabiduría corporativa.
*   **Ada:** Un nombre corto, humano y fácil de recordar.
*   **Zen:** Sugiere que el asistente ayuda a resolver dudas sin estrés.
*   **Índice:** Muy descriptivo, ideal si el asistente ayuda a buscar documentos.

**Mi recomendación personal:**
*   Si buscas algo **institucional**: **Norma**.
*   Si buscas algo **ágil y moderno**: **Lex**.
*   Si buscas algo **cercano**: **Ada**.

¿Cuál te suena mejor para la cultura de tu empresa?

---

T=0.5 | repetición=1 | Aquí tienes varias opciones categorizadas según el "tono" que quieras darle a la herramienta:

**Directos y funcionales:**
*   **Norma:** Simple, claro y directo al punto.
*   **Guía:** Transmite ayuda y orientación.
*   **Policy:** El nombre técnico, pero fácil de recordar.
*   **Lex:** Corto, suena profesional y relacionado con las reglas.

**Modernos y amigables:**
*   **Ada:** (Por *Administrative Assistant*), suena humano y cercano.
*   **Nexo:** Sugiere que el asistente es el punto de unión entre la empresa y el empleado.
*   **Zoe:** Corto, moderno y fácil de pronunciar.
*   **Ivi:** (Por *Internal Virtual Intelligence*).

**Basados en acción:**
*   **Saber:** Enfocado en que el asistente tiene todas las respuestas.
*   **Clar:** (Derivado de claridad), ideal para políticas que a veces son confusas.
*   **Punto:** Da la idea de que ahí está la respuesta exacta.

**Mi recomendación:**
Si buscas algo que denote autoridad pero sea amable, **"Norma"** es excelente porque es un nombre propio y, a la vez, el sustantivo exacto de lo que hace. Si buscas algo más tecnológico, **"Nexo"** funciona muy bien.

---

T=1.0 | repetición=1 | Aquí tienes varias opciones categorizadas según el "tono" que quieras darle a tu asistente:

**Los más directos y profesionales:**
1. **Norma:** (Clásico, sugiere reglas y estándares).
2. **Guía:** (Simple, indica que ayuda a orientarse).
3. **Pauta:** (Transmite orden y claridad).
4. **Base:** (Sugiere que es el fundamento de la información).

**Cortos y modernos (estilo tech):**
5. **Lex:** (Referencia a leyes/reglas, suena tecnológico).
6. **Pol:** (Abreviatura de políticas, muy fácil de recordar).
7. **Axon:** (Suena a conexión y agilidad).
8. **Nexo:** (El punto de unión entre la empresa y el empleado).

**Conceptuales/Metafóricos:**
9. **Eco:** (Sugiere que la política "resuena" en toda la empresa).
10. **Faros:** (Para alguien que ilumina el camino en dudas normativas).
11. **Sapi:** (Derivado de *sapiens*, transmite inteligencia corporativa).
12. **Axis:** (Significa eje; el centro sobre el cual gira la normativa).

**Mi recomendación personal:**
*   Si buscas algo **cercano**: **"Guía"**.
*   Si buscas algo **autoritario pero moderno**: **"Lex"**.
*   Si buscas algo **fácil de memorizar**: **"Pol"**.

¿Cuál de estos te resuena más con la cultura de tu empresa?

---

```
temperature_conclusion = "Se usan temperaturas cercanas a 0 para asegurar que el agente siga instrucciones estrictas sin inventar información. Se usan temperaturas altas (0.7) a (1.2) para lluvia de ideas o respuestas conversacionales fluidas."  
```

---

```
1 tokens aproximados | Hola
8 tokens aproximados | Explicá qué es un agente de IA.
19 tokens aproximados | Analizá esta solicitud, buscá evidencia y prepará una respuesta con fuentes.
```

---

```
[
  {
    "label": "español",
    "text": "Explicá brevemente cómo funciona la atención.",
    "approx_tokens": 11,
    "model_tokens": 11
  },
  {
    "label": "inglés",
    "text": "Briefly explain how attention works.",
    "approx_tokens": 9,
    "model_tokens": 8
  },
  {
    "label": "conciso",
    "text": "Resumí el documento.",
    "approx_tokens": 5,
    "model_tokens": 7
  },
  {
    "label": "detallado",
    "text": "Leé el documento completo, identificá sus ideas principales y escribí un resumen ejecutivo de cinco puntos.",
    "approx_tokens": 27,
    "model_tokens": 22
  }
]
```

---

Suponé una ventana máxima de `1.000.000` tokens y reservá `4.000` para la salida. Calculá cuánto queda para instrucciones, historial y documentos.

```pyhton
context_window = 1_000_000
reserved_output = 4_000
system_instructions = 1_500
conversation_history = 12_000

available_for_documents = (
    context_window
    - reserved_output
    - system_instructions
    - conversation_history
)

print("Tokens disponibles para documentos:", available_for_documents)
```

output:

```python
Tokens disponibles para documentos: 982500
```

### Tarifas

```
Modelo para tarifa: gemini-3.1-flash-lite
Input USD / 1M tokens: 0.25
Output USD / 1M tokens: 1.5
Ejemplo tokens entrada/salida: 2500 / 600
Costo estimado por llamada: USD 0.001525
```

```
Costo por llamada: USD 0.001525
Llamadas mensuales: 16000
Tokens mensuales entrada: 40000000
Tokens mensuales salida: 9600000
Costo mensual estimado: USD 24.4
Costo para 10.000 ejecuciones: USD 61.0
```

---

```
{
  "runs": [
    {
      "prompt": "Explicá los tokens.",
      "text": "Para entender qué son los **tokens**, imagina que son la **unidad básica de medida** que utilizan los modelos de lenguaje (como ChatGPT) para procesar el texto.\n\nAquí te explico los puntos clave para entenderlos fácilmente:\n\n### 1. ¿Qué es un token exactamente?\nUn token no es necesariamente una palabra completa. Puede ser:\n*   **Una palabra corta:** (ej. \"casa\")\n*   **Parte de una palabra:** (ej. \"in\" + \"creíble\")\n*   **Un solo carácter:** (ej. \"a\")\n*   **Signos de puntuación o espacios:** (ej. \",\", \" \")\n\n**La regla general:** En inglés, 1 token equivale aproximadamente a 4 caracteres o a 0.75 de una palabra. En español, debido a la estructura del idioma y los acentos, los modelos suelen consumir un poco más de tokens por palabra que en inglés.\n\n### 2. ¿Por qué los modelos usan tokens y no palabras?\nLos modelos de inteligencia artificial no \"leen\" como nosotros. Ellos convierten el texto en números (vectores).\n*   Si el modelo tuviera que aprender cada palabra del diccionario, sería ineficiente.\n*   Al usar tokens, el modelo puede **\"romper\" palabras desconocidas** en partes que sí conoce. Por ejemplo, si el modelo no conoce la palabra \"hipercalórico\", puede entenderla como \"hiper\" + \"calórico\". Esto le permite procesar cualquier texto, incluso palabras inventadas o errores ortográficos.\n\n### 3. ¿Cómo se cuentan?\nCuando envías un mensaje a una IA, esta hace lo siguiente:\n1.  **Tokenización:** Divide tu texto en trozos (tokens).\n2.  **Procesamiento:** Convierte esos tokens en números.\n3.  **Predicción:** Calcula cuál es el siguiente token más probable.\n\n**Ejemplo práctico:**\nLa frase *\"Hola, ¿cómo estás?\"* podría dividirse así:\n`[Hola]` `[,]` `[ ¿]` `[cómo]` `[ estás]` `[?]`\nEso serían 6 tokens.\n\n### 4. ¿Por qué te debería importar?\nHay tres razones principales por las que los usuarios deben conocer los tokens:\n\n*   **Límites de contexto:** Cada modelo tiene una \"ventana de contexto\" máxima (ej. 128,000 tokens). Si tu conversación o el documento que subes supera ese límite, la IA empezará a \"olvidar\" el principio de la charla o no podrá procesar todo el archivo.\n*   **Costo:** Si usas la API de OpenAI (para programar), no pagas por \"pregunta\", pagas por **cantidad de tokens** (tanto los que envías como los que la IA genera como respuesta).\n*   **Velocidad:** Cuantos más tokens tenga que generar la IA, más tiempo tardará en responder.\n\n### Resumen visual\nSi piensas en el texto como un **ladrillo**, los tokens son los **átomos** que lo componen. La IA no ve el ladrillo completo, ve la estructura atómica para poder reconstruirlo o crear uno nuevo.\n\n**¿Quieres saber cuántos tokens tiene un texto específico?**\nOpenAI tiene una herramienta gratuita llamada [Tokenizer](https://platform.openai.com/tokenizer) donde puedes pegar cualquier texto y ver exactamente cómo lo divide el modelo.",
      "temperature": 0.2,
      "latency_ms": 3578.8,
      "input_tokens": 7,
      "output_tokens": 731,
      "total_tokens": 738
    },
    {
      "prompt": "Explicá qué son los tokens, cómo afectan el contexto y por qué influyen en el costo de una aplicación con LLMs.",
      "text": "Para entender cómo funcionan los modelos de lenguaje (LLMs) como GPT-4 o Claude, es fundamental comprender el concepto de **tokens**. Aquí te explico qué son, cómo gestionan la memoria y por qué determinan el precio de tu factura.\n\n---\n\n### 1. ¿Qué son los tokens?\n\nLos LLMs no leen palabras como nosotros; leen **tokens**. Un token es la unidad básica de procesamiento de texto.\n\n*   **La regla general:** En inglés, 1 token equivale aproximadamente a **4 caracteres** o a **0.75 palabras**. En español, debido a la complejidad de los acentos y la estructura gramatical, un token suele ser un poco más corto (a veces una palabra larga se divide en 2 o 3 tokens).\n*   **¿Cómo se ven?** Imagina la palabra \"inteligencia\". El modelo podría verla como un solo token, pero una palabra compleja o poco común como \"electroencefalografista\" podría dividirse en 4 o 5 tokens.\n*   **No es solo texto:** Los tokens también incluyen espacios, signos de puntuación y caracteres especiales.\n\n---\n\n### 2. ¿Cómo afectan el contexto?\n\nEl \"contexto\" es la **ventana de memoria** que tiene el modelo. Es la cantidad máxima de tokens que el modelo puede \"recordar\" o procesar en una sola interacción (incluyendo tu pregunta y la respuesta que él genera).\n\n*   **La Ventana de Contexto:** Cada modelo tiene un límite (ej. 8k, 32k, 128k tokens). Si tu conversación supera ese límite, el modelo empieza a \"olvidar\" el principio de la charla.\n*   **El impacto en la calidad:**\n    *   **Si el contexto es pequeño:** El modelo pierde el hilo de la conversación rápidamente.\n    *   **Si el contexto es grande:** Puedes subir documentos enteros, libros o historiales de chat extensos, y el modelo podrá mantener la coherencia sobre toda esa información.\n*   **El costo de la memoria:** Mantener un contexto grande requiere mucha capacidad de cómputo. Por eso, los modelos con ventanas de contexto masivas suelen ser más lentos o costosos.\n\n---\n\n### 3. ¿Por qué influyen en el costo?\n\nLas empresas que ofrecen LLMs (como OpenAI, Anthropic o Google) cobran por **\"mil tokens\"**. El costo se divide en dos partes:\n\n1.  **Tokens de Entrada (Input):** Es todo lo que tú le envías al modelo (tu pregunta + el contexto previo + documentos adjuntos).\n2.  **Tokens de Salida (Output):** Es todo lo que el modelo escribe como respuesta.\n\n**¿Por qué esto hace que las aplicaciones sean costosas?**\n\n*   **El efecto \"bola de nieve\":** En una aplicación de chat, cada vez que envías un nuevo mensaje, debes reenviar **todo el historial anterior** para que el modelo sepa de qué están hablando. Esto significa que el mensaje número 10 de una conversación es mucho más caro que el primero, porque estás pagando por procesar los 9 mensajes anteriores una y otra vez.\n*   **La longitud de la respuesta:** Si le pides al modelo que escriba un informe largo, el costo de los tokens de salida será significativamente mayor que si le pides un \"sí\" o \"no\".\n*   **Escalabilidad:** Si tienes 1,000 usuarios usando tu aplicación simultáneamente, y cada uno envía prompts largos, el consumo de tokens se dispara exponencialmente.\n\n---\n\n### Resumen para desarrolladores o dueños de negocio:\n\n*   **Optimización:** Para reducir costos, no envíes todo el historial de chat si no es necesario. Usa técnicas como *summarization* (resumir la conversación anterior) para mantener el contexto pequeño.\n*   **Monitoreo:** Siempre debes medir cuántos tokens consume cada interacción. Si no controlas esto, una aplicación que parece barata puede volverse impagable si un usuario decide \"jugar\" con el modelo enviándole libros enteros para analizar.\n*   **Selección de modelo:** No siempre necesitas el modelo más potente (y caro). Para tareas simples, usar un modelo más pequeño y rápido (como GPT-4o-mini) puede reducir tus costos hasta en un 90% sin sacrificar demasiada calidad.",
      "temperature": 0.2,
      "latency_ms": 4504.65,
      "input_tokens": 28,
      "output_tokens": 935,
      "total_tokens": 963
    }
  ],
  "winner": "Explicá los tokens.",
  "faster_prompt": "Explicá los tokens."
}
```
