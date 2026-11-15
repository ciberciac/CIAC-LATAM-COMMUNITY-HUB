# Construir aplicaciones con LLM

| | |
|---|---|
| **Nivel** | 🟡 intermedio |
| **Aplica a** | Chatbots, asistentes internos, RAG, clasificación o resumen automatizado |
| **Referencias** | OWASP Top 10 for LLM Applications 2025 · MITRE ATLAS · NIST AI 600-1 |

## Modelo mental
Un LLM **no distingue con fiabilidad entre instrucciones y datos**. Todo texto que llega al modelo (del usuario, de un documento, de una página web, de un correo) puede intentar cambiar su comportamiento. Diseña asumiendo que, en algún momento, lo logrará.

## OWASP Top 10 para LLM (2025) y controles clave

| Riesgo | Qué es | Controles principales |
|---|---|---|
| **LLM01 Inyección de prompts** | Instrucciones maliciosas directas o escondidas en contenido que procesa el modelo | Separar instrucciones de datos, limitar lo que el modelo puede hacer, validar salidas, confirmación humana en acciones sensibles |
| **LLM02 Divulgación de información sensible** | El modelo revela datos personales, secretos o información de otros usuarios | No poner en el contexto lo que el usuario no debe ver; control de acceso **antes** de recuperar datos; filtrado de salidas |
| **LLM03 Cadena de suministro** | Modelos, datasets, plugins o paquetes comprometidos | Fuentes confiables, verificación de integridad, inventario (AI-BOM), SCA |
| **LLM04 Envenenamiento de datos y modelos** | Datos de entrenamiento, ajuste o RAG manipulados | Control de quién puede escribir en las fuentes, revisión de datos, procedencia |
| **LLM05 Manejo inadecuado de salidas** | La salida del modelo se usa sin validar en HTML, SQL, shell o APIs | Tratar la salida como entrada de usuario: escapar, parametrizar, validar contra esquema |
| **LLM06 Agencia excesiva** | El modelo tiene más herramientas, permisos o autonomía de los necesarios | Mínimo privilegio, herramientas específicas en vez de genéricas, aprobación humana |
| **LLM07 Filtración del prompt de sistema** | El prompt de sistema expone reglas, credenciales o lógica interna | Nunca guardar secretos ni controles de seguridad en el prompt; aplicarlos en código |
| **LLM08 Debilidades en vectores y embeddings** | Fugas entre usuarios o inyección a través de la base vectorial | Segmentar por usuario o tenant, control de acceso en la recuperación, validar documentos ingeridos |
| **LLM09 Desinformación** | Respuestas falsas presentadas con seguridad | Citar fuentes, RAG con fuentes verificadas, avisos al usuario, revisión humana en decisiones críticas |
| **LLM10 Consumo sin límites** | Abuso que dispara costos o tumba el servicio | Límites de tasa, de tokens y de presupuesto por usuario; alertas de consumo |

## Controles de arquitectura

### Los controles de seguridad viven en el código, no en el prompt · 🔴
"No reveles datos de otros clientes" en el prompt **no es un control de acceso**. La autorización se aplica antes de que el dato llegue al modelo.

### Valida la salida como cualquier entrada externa · 🔴
- Si se muestra en una web: escapar HTML y desactivar la carga automática de imágenes y enlaces generados (vía común de exfiltración).
- Si se usa en consultas o comandos: parametrizar y validar contra una lista permitida.
- Si se espera un formato: validar contra un esquema (JSON Schema) y rechazar lo que no cumpla.

### RAG con permisos · 🔴
El usuario solo debe recibir fragmentos de documentos a los que ya tiene acceso. Filtra por permisos en la consulta a la base vectorial, no después.

### Registro y monitoreo · 🟡
Registra prompts, respuestas, documentos recuperados y llamadas a herramientas (minimizando datos personales) para investigar incidentes y detectar abuso.

### Pruebas adversariales antes de publicar · 🟡
Incluye casos de inyección directa e indirecta, extracción del prompt de sistema, fuga entre usuarios y abuso de consumo. Repite tras cada cambio de modelo o prompt.

## Lista de verificación
- [ ] La autorización se aplica antes de enviar datos al modelo.
- [ ] Ningún secreto en el prompt de sistema.
- [ ] Salidas validadas y escapadas según su destino.
- [ ] Límites de tasa, tokens y presupuesto.
- [ ] Registro de interacciones con retención definida.
- [ ] Pruebas de inyección de prompts documentadas.
- [ ] Revisado dónde procesa los datos el proveedor y si aplica transferencia internacional.
