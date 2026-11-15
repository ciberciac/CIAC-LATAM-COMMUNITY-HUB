# Agentes de IA, herramientas y MCP

| | |
|---|---|
| **Nivel** | 🔴 avanzado |
| **Aplica a** | Agentes que ejecutan acciones: llamadas a APIs, consultas a bases de datos, envío de correos, ejecución de código, servidores MCP |
| **Referencias** | OWASP LLM01, LLM06 · OWASP Agentic AI – Threats and Mitigations · MITRE ATLAS |

## Por qué es distinto
En un chatbot, una inyección de prompts produce una mala respuesta. En un agente, produce una **mala acción**: borrar datos, enviar información fuera, modificar configuraciones. El riesgo crece con cada herramienta y permiso.

## La "tríada letal"
Un agente es especialmente peligroso cuando combina a la vez:
1. Acceso a **datos privados**,
2. Exposición a **contenido no confiable** (correos, páginas web, documentos, issues),
3. Capacidad de **comunicarse hacia afuera** (enviar correos, hacer peticiones web, escribir en repositorios públicos).

Si tu diseño junta las tres, un texto escondido en un documento puede hacer que el agente exfiltre datos. **Quita al menos una** o pon aprobación humana en el punto de salida.

## Controles

### 1. Mínimo privilegio real · 🔴
- Credenciales propias del agente, con el alcance mínimo y de corta duración. Nunca las de un administrador.
- Herramientas específicas (`consultar_estado_ticket`) en lugar de genéricas (`ejecutar_sql`, `ejecutar_shell`).
- Solo lectura por defecto; escritura como excepción justificada.

### 2. Persona en el circuito para lo irreversible · 🔴
Pagos, borrados, envíos externos, cambios de permisos o de configuración requieren confirmación humana **mostrando exactamente qué se va a hacer**.

### 3. Aislamiento · 🔴
- Ejecución de código en entornos efímeros (contenedor o micro-VM) sin acceso a la red interna ni a credenciales.
- Lista permitida de dominios para salida a Internet.

### 4. Servidores MCP y plugins · 🔴
- Usa solo servidores de fuentes confiables; revisa su código o su reputación y fija la versión.
- Revisa qué herramientas expone cada servidor y desactiva las que no necesitas.
- Las descripciones de herramientas y sus respuestas son texto que lee el modelo: pueden contener instrucciones maliciosas.
- Un servidor MCP con acceso a correo, archivos o repositorios equivale a dar ese acceso al modelo.

### 5. Separar planificación y ejecución · 🟡
Cuando sea posible, que el plan se genere solo con la instrucción del usuario y el contenido no confiable se procese después, sin poder cambiar el plan ni las herramientas disponibles.

### 6. Trazabilidad completa · 🟡
Registra cada llamada a herramienta con sus parámetros, el resultado y qué contenido la motivó. Sin esto no hay investigación posible.

### 7. Límites de ejecución · 🟡
Número máximo de pasos, de llamadas por herramienta y de costo por tarea. Un agente en bucle también es un incidente.

## Lista de verificación
- [ ] Revisada la tríada letal y eliminada al menos una condición o añadida aprobación humana.
- [ ] Credenciales propias, mínimas y de corta duración.
- [ ] Acciones irreversibles con confirmación humana.
- [ ] Ejecución de código aislada.
- [ ] Servidores MCP y plugins revisados, con versión fija.
- [ ] Registro de todas las llamadas a herramientas.
- [ ] Pruebas de inyección indirecta (en documentos, correos, páginas) realizadas.
