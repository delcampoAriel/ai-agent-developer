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
