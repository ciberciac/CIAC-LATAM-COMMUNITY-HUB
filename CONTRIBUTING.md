# Guía de contribución

¡Gracias por sumarte! Esta guía explica cómo aportar contenido de calidad y fácil de revisar.

## Formas de contribuir

- **Corregir o mejorar** contenido existente: errores, enlaces rotos, actualizaciones.
- **Aportar contenido nuevo**: una guía, una regla, un playbook, un laboratorio.
- **Reportar** falsos positivos de una regla o recomendaciones que no funcionan.
- **Mejorar la redacción** y la claridad de las guías.
- **Proponer iniciativas** en Discussions.

## Flujo de trabajo

1. Haz *fork* del repositorio y crea una rama: `tipo/descripcion-corta`
   (`sigma/powershell-descarga-remota`, `ir/playbook-bec`, `docs/corrige-enlaces`).
2. Copia la plantilla `_plantilla.md` de la carpeta donde vas a aportar, si existe.
3. Usa mensajes de commit claros, preferiblemente con [Conventional Commits](https://www.conventionalcommits.org/es/v1.0.0/):
   `feat(sigma): detección de borrado de shadow copies` · `fix(ir): corrige paso de contención` · `docs: actualiza README`.
4. Abre el Pull Request con la plantilla y espera la revisión. Los checks automáticos deben pasar.

## Reglas de contenido

| Regla | Detalle |
|---|---|
| **Solo TLP:CLEAR** | Nada confidencial, de clientes ni de tu empleador sin autorización. |
| **Sin datos personales** | Anonimiza nombres, correos, IPs internas, hostnames y datos de víctimas. |
| **Sin malware real** | No subas binarios ni muestras, tampoco en ZIP con contraseña. Usa hashes y enlaza a repositorios especializados. |
| **Sin herramientas ofensivas operativas** | El enfoque es defensivo. Las técnicas de ataque se describen para detectarlas y mitigarlas. |
| **Fuentes** | Cita las fuentes en las que te basas, con enlace. |
| **Indicadores desactivados** | En Markdown escribe `dominio[.]com` y `hxxps://`. En archivos de reglas o CSV, el valor real. |
| **Referencias estándar** | Técnicas como ID de MITRE ATT&CK (`T1566.001`), fechas ISO 8601 (`2026-11-14`), países ISO 3166 (`CO`, `MX`, `BR`). |
| **Probado** | Las reglas y comandos se prueban en laboratorio. Indica en qué versión o plataforma. |

## Idioma y estilo de escritura

- **Todo el contenido se escribe en español.
- Los términos técnicos en inglés se usan solo cuando son nombres propios o el término estándar del sector (*threat hunting*, *playbook*, *phishing*). La primera vez, acompáñalos de su explicación en español.
- Español neutro, frases cortas, voz activa.
- Explica el **por qué** de cada recomendación, no solo el **qué**.
- Indica el nivel: 🟢 básico · 🟡 intermedio · 🔴 avanzado.
- Para equipos pequeños, marca qué es **imprescindible** y qué es **deseable**.

## Licencia de tus aportes

Al contribuir aceptas que tu aporte se publique bajo la licencia de la carpeta correspondiente: **CC BY 4.0** para el contenido general y **DRL 1.1** para `detection-as-code/`. Conservas el crédito como autor/a.

## Revisión

- Primera respuesta en un plazo objetivo de 5 días hábiles.
- Un PR necesita la aprobación de al menos una persona mantenedora.
- Las observaciones son sobre el contenido, nunca sobre la persona.
