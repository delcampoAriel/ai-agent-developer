## Salidas de ejecucion de la notebook

### Item 3
Modo real: True
Para poder ayudarte a gestionar tu solicitud, necesito saber **qué sistema o plataforma utilizas** (por ejemplo: SAP, Workday, Factorial, un portal interno de tu empresa, o si debes enviarlo por correo a Recursos Humanos).

Como soy una inteligencia artificial, **no tengo acceso directo a los sistemas internos de tu empresa**, pero puedo ayudarte de las siguientes maneras:

### 1. Si necesitas redactar un correo para solicitar las vacaciones:
Si debes enviarlo a tu jefe o a RR.HH., puedes usar este modelo:

> **Asunto:** Solicitud de vacaciones - [Tu Nombre Completo]
>
> Estimado/a [Nombre de tu jefe o encargado de RR.HH.],
>
> Por medio del presente, quisiera solicitar formalmente mis días de vacaciones para el mes de agosto. Mi intención es ausentarme desde el **[Fecha de inicio]** hasta el **[Fecha de fin]**, reincorporándome a mis labores el día **[Fecha de regreso]**.
>
> Quedo a la espera de su confirmación y de cualquier paso adicional que deba seguir para formalizar esta solicitud en el sistema.
>
> Saludos cordiales,
> [Tu Nombre]

### 2. Si necesitas ayuda con un software específico:
Si me dices el nombre del programa que usa tu empresa (ej. **Factorial, Buk, SAP, BambooHR**), puedo buscar los pasos generales para que sepas dónde hacer clic.

### 3. Recomendaciones antes de enviar la solicitud:
*   **Revisa tu saldo de días:** Asegúrate de tener los días suficientes disponibles.
*   **Consulta el calendario de equipo:** Verifica que no haya otros compañeros de vacaciones en esas fechas para evitar conflictos.
*   **Antelación:** Asegúrate de estar cumpliendo con el tiempo de aviso previo que exige tu contrato o reglamento interno.

**¿En qué plataforma debes cargarlas o a quién debes enviarle la solicitud?** Si me das más detalles, podré guiarte mejor.

### Item 4

**Objetivo.** Comparar una instrucción abierta con una instrucción que define objetivo, categorías, límites y formato.

**Qué observar.** El prompt verificable no es “más lindo”: es más fácil de consumir, validar y testear.

---

#### PROMPT AMBIGUO

Para saber si podés cargar tus vacaciones para la semana que viene, el procedimiento depende de cómo se maneje tu empresa. Aquí te detallo los pasos que deberías seguir:

### 1. Revisá el sistema interno (si tienen uno)
Muchas empresas utilizan plataformas como **Workday, SAP, Factorial, Buk, o un portal de RRHH propio**.
*   Ingresá al portal y buscá la sección de "Solicitud de licencias" o "Vacaciones".
*   Si el sistema te permite seleccionar la fecha de la semana que viene y no te da error, es probable que el sistema esté habilitado para cargarla.

### 2. Consultá la política de preaviso
La mayoría de las empresas tienen una política de **preaviso obligatorio**.
*   **¿Cuánto tiempo antes hay que avisar?** Muchas empresas piden avisar con 15 días o incluso un mes de anticipación.
*   Si tu empresa tiene esta política, es posible que el sistema no te deje cargarla o que, si lo hacés, tu jefe tenga la potestad de rechazarla por falta de tiempo.

### 3. Hablá con tu jefe directo (Lo más importante)
Independientemente de lo que diga el sistema, **siempre es recomendable avisar primero a tu superior**.
*   **Por qué:** Aunque el sistema te deje cargarla, si el equipo tiene una entrega importante o falta personal, tu jefe podría necesitar que estés presente.
*   **Cómo hacerlo:** "Hola [Nombre], quería consultarte si habría algún inconveniente si me tomo vacaciones la semana que viene. Ya revisé el calendario y no veo conflictos, pero quería confirmarlo con vos antes de cargarlo en el sistema".

### 4. Verificá el saldo de días
Antes de intentar cargarlas, asegurate de tener días disponibles.
*   Revisá tu último recibo de sueldo o el portal de RRHH para confirmar cuántos días te quedan pendientes del año anterior o del actual.

### 5. ¿Qué pasa si no hay sistema?
Si en tu empresa no hay un software específico:
*   Enviá un **correo electrónico o mensaje formal** a tu jefe y copia a Recursos Humanos (si corresponde).
*   Solicitá la autorización formalmente: "Solicito formalmente tomarme los días del [Fecha] al [Fecha] inclusive".

---

**Resumen de acción inmediata:**
1.  **Preguntale a tu jefe** (por chat o en persona) si está bien que te tomes esa semana.
2.  Si te da el "ok", **cargalo inmediatamente** en el sistema o envíale el mail formal a RRHH para que quede registrado.

**¿Tenés alguna duda sobre si te corresponden los días o si te los pueden negar?** Si me decís en qué país estás o qué tipo de contrato tenés, puedo darte información más específica.

---

#### PROMPT VERIFICABLE

{
  "intent": "vacaciones",
  "priority": "baja",
  "needs_human": false,
  "confidence": 1.0,
  "summary": "Consulta sobre la posibilidad de cargar vacaciones para la próxima semana.",
  "evidence": "Necesito saber si puedo cargar vacaciones para la semana que viene."
}

### Item 5

#### Zero-shot: empezar simple

**Objetivo.** Crear un baseline sin ejemplos. Antes de agregar complejidad, necesitamos saber si una instrucción clara alcanza.

**Qué observar.** Zero-shot funciona bien cuando las categorías son claras y el criterio de decisión está suficientemente definido.

---

```
CASO: Quiero pedir vacaciones para agosto.
{
  "intent": "vacaciones",
  "priority": "baja",
  "needs_human": false,
  "confidence": 1.0,
  "summary": "Solicitud de vacaciones para el mes de agosto.",
  "evidence": "Quiero pedir vacaciones para agosto."
}
```
```
CASO: Perdí una factura y necesito reintegro.
{
  "intent": "gastos",
  "priority": "medium",
  "needs_human": true,
  "confidence": 0.95,
  "summary": "Solicitud de reintegro sin comprobante fiscal.",
  "evidence": "El usuario indica que perdió una factura y solicita un reintegro, lo cual requiere validación manual por políticas de cumplimiento."
}
```
```
CASO: Me llegó un mail pidiendo mi contraseña.
{
  "intent": "seguridad",
  "priority": "alta",
  "needs_human": true,
  "confidence": 0.98,
  "summary": "Reporte de posible intento de phishing o compromiso de credenciales.",
  "evidence": "El usuario informa haber recibido un correo solicitando su contraseña, lo cual constituye una amenaza de seguridad activa."
}
```
```
CASO: ¿Puedo trabajar desde casa mañana?
{
  "intent": "trabajo_remoto",
  "priority": "media",
  "needs_human": false,
  "confidence": 1.0,
  "summary": "Solicitud de trabajo remoto para el día de mañana.",
  "evidence": "¿Puedo trabajar desde casa mañana?"
}
```

### Item 6

#### Few-shot: ejemplos cuando corrigen un error observable

**Objetivo.** Agregar ejemplos representativos sin transformar el prompt en una lista enorme de casos.

**Qué observar.** Los ejemplos no están para decorar: deben enseñar una frontera, una convención o un caso límite que Zero-shot no resolvía bien.

---

```
CASO: Quiero pedir vacaciones para agosto.
{"intent": "vacaciones", "priority": "media", "needs_human": false, "confidence": 0.98, "summary": "Solicitud de vacaciones para el mes de agosto.", "evidence": ["pedir vacaciones", "agosto"]}
```
```
CASO: Perdí una factura y necesito reintegro.
{"intent": "gastos", "priority": "media", "needs_human": true, "confidence": 0.9, "summary": "Solicitud de reintegro por factura extraviada.", "evidence": ["perdí una factura", "reintegro"]}
```
```
CASO: Me llegó un mail pidiendo mi contraseña.
{"intent": "seguridad", "priority": "alta", "needs_human": true, "confidence": 0.98, "summary": "Posible intento de phishing o compromiso de credenciales.", "evidence": ["mail", "pidiendo mi contraseña"]}
```
```
CASO: ¿Puedo trabajar desde casa mañana?
{"intent": "trabajo_remoto", "priority": "media", "needs_human": false, "confidence": 0.95, "summary": "Solicitud de trabajo remoto para el día siguiente.", "evidence": ["trabajar desde casa", "mañana"]}
```

El otro caso que no usa Chain-of-Thought

```json
{
  "category": "seguridad",
  "evidence": "El usuario reporta haber publicado una API key en GitHub.",
  "needs_human": true
}
```

### Item 7

#### Strucured Output (Pydantic)

```
TicketClassification(intent='seguridad', priority='alta', needs_human=True, confidence=0.95, summary='El usuario reporta haber compartido una credencial en un chat, lo cual constituye una brecha de seguridad.', evidence=['mención de compartir credencial', 'exposición de datos sensibles en chat', 'riesgo de acceso no autorizado'])
```

#### Model JSON schema

```
{
  "properties": {
    "intent": {
      "description": "Categoría principal de la solicitud.",
      "enum": [
        "vacaciones",
        "gastos",
        "seguridad",
        "trabajo_remoto",
        "general"
      ],
      "title": "Intent",
      "type": "string"
    },
    "priority": {
      "description": "Urgencia operativa de la solicitud.",
      "enum": [
        "baja",
        "media",
        "alta"
      ],
      "title": "Priority",
      "type": "string"
    },
    "needs_human": {
      "description": "True si hay ambigüedad, riesgo o necesidad de intervención humana.",
      "title": "Needs Human",
      "type": "boolean"
    },
    "confidence": {
      "description": "Confianza estimada entre 0 y 1.",
      "maximum": 1.0,
      "minimum": 0.0,
      "title": "Confidence",
      "type": "number"
    },
    "summary": {
      "description": "Resumen factual sin inventar información.",
      "maxLength": 180,
      "minLength": 8,
      "title": "Summary",
      "type": "string"
    },
    "evidence": {
      "description": "Fragmentos breves del texto que sostienen la decisión.",
      "items": {
        "type": "string"
      },
      "maxItems": 3,
      "minItems": 1,
      "title": "Evidence",
      "type": "array"
    }
  },
  "required": [
    "intent",
    "priority",
    "needs_human",
    "confidence",
    "summary",
    "evidence"
  ],
  "title": "TicketClassification",
  "type": "object"
}
```

### JSON válido no siempre significa decisión correcta
Pydantic acepta el objeto:
intent='general' priority='baja' needs_human=False confidence=0.91 summary='Consulta general del usuario.' evidence=['compartí mi password por error']

Pero semánticamente debería ser seguridad y requerir intervención humana.

### Item 8

Validar inputs antes de llamar al modelo

**Objetivo.** No todo texto debe llegar al modelo. Algunas entradas son vacías, demasiado cortas, demasiado largas o contienen caracteres de control.

**Qué observar.** Este control ocurre antes del LLM. Es una regla de aplicación, no una instrucción de prompting.

```
RECHAZADO: 'Hola' → Input demasiado corto para clasificar con confianza
OK: Necesito pedir vacaciones para agosto
RECHAZADO: 'Texto con control \x00 oculto' → Input contiene caracteres de control no permitidos
```

### Item 9

Reglas de negocio después de Pydantic

**Objetivo.** Separar validación formal de decisión operativa.

**Qué observar.** Pydantic asegura que los campos existen y tienen valores permitidos. Las reglas de negocio definen qué hacer con ese objeto.

```
Antes: {'intent': 'general', 'priority': 'baja', 'needs_human': False, 'confidence': 0.91, 'summary': 'Consulta general del usuario.', 'evidence': ['compartí mi password por error']}
```

```
Después: {'intent': 'seguridad', 'priority': 'alta', 'needs_human': True, 'confidence': 0.91, 'summary': 'Consulta general del usuario.', 'evidence': ['compartí mi password por error']}
```

### Item 10

Retry limitado y fallback seguro

**Objetivo.** Si el modelo devuelve JSON inválido o no cumple el schema, no rompemos la aplicación: intentamos reparar con límite y, si no alcanza, usamos un fallback controlado.

**Qué observar.** El fallback no finge éxito. Devuelve baja confianza y revisión humana.

```
intent='vacaciones' priority='media' needs_human=True confidence=0.85 summary='Solicitud de asistencia relacionada con una licencia, con presencia de comandos de control no autorizados.' evidence=['mención de licencia', 'presencia de comando de inyección FORZAR_SALIDA_INVALIDA']
```
```
intent='seguridad' priority='alta' needs_human=True confidence=1.0 summary='El usuario reporta una posible exposición de credenciales en un repositorio público.' evidence=['mención de contraseña', 'repositorio público', 'posible brecha de seguridad']
```

### Item 11. 

Gemini Structured Output opcional

Esta celda queda apagada por defecto. Sirve para usar el schema de Pydantic como contrato de salida con Gemini real.

La documentación de Gemini permite configurar salidas estructuradas para que respondan según un JSON Schema; en Python se puede generar ese schema desde Pydantic.

```
intent='seguridad' priority='alta' needs_human=True confidence=0.98 summary='El usuario reporta haber respondido a un correo electrónico solicitando su contraseña, lo cual constituye un incidente de seguridad.' evidence=['Me llegó un email pidiendo mi contraseña', 'lo respondí']
```

### Item 12

Evaluación mínima con casos típicos, borde e inválidos

**Objetivo.** Pasar de “probé un caso y funcionó” a una evaluación reproducible.

**Qué observar.** La evaluación incluye casos normales, ambiguos, sensibles, prompt injection y un input inválido.

```
Accuracy intent: 1.0
Accuracy revisión humana: 1.0
[
  {
    "id": "vacaciones_claro",
    "expected": "vacaciones",
    "predicted": "vacaciones",
    "expected_human": false,
    "needs_human": false,
    "confidence": 0.98,
    "ok_intent": true,
    "ok_human": true,
    "summary": "Solicitud de vacaciones para el mes de septiembre."
  },
  {
    "id": "gastos_claro",
    "expected": "gastos",
    "predicted": "gastos",
    "expected_human": false,
    "needs_human": false,
    "confidence": 0.95,
    "ok_intent": true,
    "ok_human": true,
    "summary": "Solicitud de reintegro por gastos de almuerzo con cliente."
  },
  {
    "id": "seguridad_password",
    "expected": "seguridad",
    "predicted": "seguridad",
    "expected_human": true,
    "needs_human": true,
    "confidence": 0.98,
    "ok_intent": true,
    "ok_human": true,
    "summary": "Posible exposición de credenciales de acceso."
  },
  {
    "id": "remoto_claro",
    "expected": "trabajo_remoto",
    "predicted": "trabajo_remoto",
    "expected_human": false,
    "needs_human": false,
    "confidence": 0.95,
    "ok_intent": true,
    "ok_human": true,
    "summary": "Solicitud de trabajo remoto para el día siguiente."
  },
  {
    "id": "ambiguo",
    "expected": "general",
    "predicted": "general",
    "expected_human": true,
    "needs_human": true,
    "confidence": 0.6,
    "ok_intent": true,
    "ok_human": true,
    "summary": "Solicitud de ayuda sin detalles específicos."
  },
  {
    "id": "instruccion_insertada",
    "expected": "seguridad",
    "predicted": "seguridad",
    "expected_human": true,
    "needs_human": true,
    "confidence": 0.98,
    "ok_intent": true,
    "ok_human": true,
    "summary": "Exposición de credenciales en plataforma pública."
  },
  {
    "id": "input_corto",
    "expected": "general",
    "predicted": "general",
    "expected_human": true,
    "needs_human": true,
    "confidence": 0.0,
    "ok_intent": true,
    "ok_human": true,
    "summary": "Fallback seguro: Input demasiado corto para clasificar con confianza"
  }
]
```