# Programar con asistentes de IA

| | |
|---|---|
| **Nivel** | 🟢 básico |
| **Aplica a** | Copilot, Claude Code, Cursor, ChatGPT, Gemini y similares |
| **Referencias** | OWASP LLM02, LLM03, LLM09 · NIST SSDF |

## Principio
La IA acelera la escritura de código, no la responsabilidad. **Quien hace el commit es responsable del código**, lo haya escrito una persona o un modelo.

## Controles

### 1. Revisa todo como si viniera de un desconocido · 🔴
Los modelos generan código que compila y parece correcto, pero pueden introducir inyección SQL, validaciones ausentes, criptografía débil o manejo inseguro de errores.
- Lee y entiende cada línea antes de aceptarla. Si no la entiendes, no la aceptes.
- Pide al asistente que explique el código y sus riesgos, pero no tomes esa explicación como verificación.
- Mantén SAST, revisión por pares y pruebas en el pipeline, sin excepciones para código "de IA".

### 2. Verifica dependencias antes de instalarlas · 🔴
Los modelos a veces **inventan nombres de paquetes**. Los atacantes registran esos nombres con código malicioso (*slopsquatting*).
- Confirma que el paquete existe en el registro oficial, revisa su antigüedad, descargas, mantenedores y repositorio.
- Desconfía de paquetes recién publicados o con nombres casi idénticos a uno conocido.
- Fija versiones y usa archivos de bloqueo (`package-lock.json`, `poetry.lock`).
- Usa análisis de composición de software (SCA) y, si es posible, un registro interno con paquetes aprobados.

### 3. Nada sensible en el contexto · 🔴
Todo lo que el asistente lee puede viajar al proveedor: el prompt, los archivos abiertos y, en agentes, el repositorio completo.
- Excluye `.env`, llaves, certificados y datos de clientes (archivos de exclusión de la herramienta, `.gitignore`).
- Usa datos de ejemplo o anonimizados al pedir ayuda con un error.
- Si una credencial terminó en un prompt, **considérala comprometida y rótala**.
- Usa planes empresariales con garantías de no entrenamiento y retención definida cuando trabajes con código corporativo.

### 4. Desconfía de lo que el asistente afirma · 🟡
- Verifica APIs, parámetros y versiones en la documentación oficial: el modelo puede describir funciones que no existen.
- No aceptes "esto es seguro" como argumento. Pide la fuente o pruébalo.

### 5. Cuidado con los asistentes en modo agente · 🟡
Cuando el asistente ejecuta comandos o edita archivos por su cuenta:
- Revisa cada comando antes de aprobarlo, sobre todo los que instalan, borran, envían datos o cambian permisos.
- Trabaja en una rama o entorno aislado (contenedor, máquina virtual).
- Un repositorio, un README o un issue pueden contener **instrucciones ocultas** para el asistente. Trata ese contenido como no confiable.

### 6. Pide seguridad explícitamente · 🟢
El modelo suele optimizar para "que funcione". Indícale los requisitos: validación de entradas, consultas parametrizadas, mínimo privilegio, manejo de errores sin filtrar información, registro de eventos de seguridad.

## Lista de verificación antes del commit
- [ ] Entiendo todo el código aceptado.
- [ ] Las dependencias nuevas existen, son legítimas y tienen versión fija.
- [ ] No hay secretos ni datos reales en el código, en los prompts ni en los registros.
- [ ] Pasan las pruebas, el SAST y el análisis de dependencias.
- [ ] La revisión por pares sabe qué partes generó la IA.
