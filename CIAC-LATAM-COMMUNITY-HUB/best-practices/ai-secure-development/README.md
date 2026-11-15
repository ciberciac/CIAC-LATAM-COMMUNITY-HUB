# Desarrollo seguro con IA

Buenas prácticas para dos situaciones que hoy conviven en casi todos los equipos:

1. **Programar con ayuda de IA** (asistentes de código, *vibe coding*, agentes que editan repositorios).
2. **Construir aplicaciones que usan IA** (chatbots, RAG, agentes con herramientas, integraciones MCP).

Y una tercera, propia de los equipos de seguridad: **usar IA en el trabajo de ciberseguridad** (SOC, CTI, respuesta a incidentes) sin exponer datos ni confiar a ciegas en sus resultados.

| Guía | Para quién | Nivel |
|---|---|---|
| [asistentes-de-codigo.md](asistentes-de-codigo.md) | Cualquier persona que programa con IA | 🟢 |
| [aplicaciones-llm.md](aplicaciones-llm.md) | Equipos que integran LLM en productos | 🟡 |
| [agentes-y-herramientas.md](agentes-y-herramientas.md) | Equipos que dan herramientas, permisos o autonomía a un modelo | 🔴 |
| [ia-en-operaciones-de-seguridad.md](ia-en-operaciones-de-seguridad.md) | SOC, CTI, DFIR | 🟡 |

## Hoja de ruta mínima

| # | Control | Prioridad | Referencia |
|---|---|---|---|
| 1 | Política de uso de IA: qué herramientas están aprobadas y qué datos **nunca** se envían | 🔴 | NIST AI RMF (Govern) · ISO/IEC 42001 |
| 2 | El código generado por IA pasa por la **misma revisión, pruebas y SAST** que el código humano | 🔴 | NIST SSDF (SP 800-218) |
| 3 | Verificar que cada dependencia sugerida **existe y es la legítima** antes de instalarla | 🔴 | OWASP LLM03 |
| 4 | Ningún secreto, credencial ni dato personal en prompts, contexto o archivos que lee el asistente | 🔴 | OWASP LLM02 |
| 5 | Tratar **toda salida del modelo como entrada no confiable** (validar, escapar, nunca ejecutar directo) | 🔴 | OWASP LLM05 |
| 6 | Mínimo privilegio para agentes y herramientas; confirmación humana para acciones irreversibles | 🔴 | OWASP LLM06 |
| 7 | Asumir que la **inyección de prompts** es posible y diseñar para limitar su impacto | 🟡 | OWASP LLM01 · MITRE ATLAS |
| 8 | Registro y monitoreo de prompts, llamadas a herramientas y consumo | 🟡 | OWASP LLM10 |
| 9 | Inventario de modelos, proveedores y dónde se procesan los datos | 🟡 | NIST AI 600-1 · leyes locales de protección de datos |
| 10 | Pruebas adversariales (*red teaming*) antes de publicar aplicaciones con IA | 🟢 | MITRE ATLAS · OWASP GenAI Red Teaming Guide |

## Marcos de referencia

- **OWASP Top 10 for LLM Applications (2025)** y proyecto OWASP GenAI Security
- **MITRE ATLAS**: tácticas y técnicas de ataque contra sistemas de IA
- **NIST AI RMF 1.0** y su perfil de IA generativa **NIST AI 600-1**
- **NIST SP 800-218 (SSDF)** y su complemento para IA generativa SP 800-218A
- **ISO/IEC 42001**: sistemas de gestión de IA
- **Google SAIF** (Secure AI Framework)
- Leyes de protección de datos de la región (p. ej. LGPD en Brasil, Ley 1581 de 2012 en Colombia, LFPDPPP en México): revisa si enviar datos a un proveedor de IA implica transferencia internacional.
