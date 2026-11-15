# Buenas prácticas de NIST y CISA por proceso

Resumen en español de las guías del **NIST** (Instituto Nacional de Estándares y Tecnología de EE. UU.) y de **CISA** (Agencia de Ciberseguridad y Seguridad de Infraestructura de EE. UU.) aplicables a cada proceso de seguridad, con su relación con la [evaluación de madurez](../../maturity-assessment/).

## Por qué NIST y CISA
- Son **gratuitas, públicas** y se actualizan con frecuencia.
- Son la referencia más usada por reguladores y auditores de la región, incluso donde no son obligatorias.
- Varias se elaboran junto a agencias de otros países (Australia, Canadá, Reino Unido, Nueva Zelanda), lo que les da alcance internacional.

> Algunas directivas de CISA (las *Binding Operational Directives*, BOD) son obligatorias solo para agencias federales de EE. UU. Aquí se usan como **referencia de buenas prácticas**, no como requisito.

## Procesos

| Proceso | Guía | Madurez relacionada |
|---|---|---|
| Centro de operaciones de seguridad | [soc.md](soc.md) | [SOC](../../maturity-assessment/soc/) |
| Inteligencia de amenazas | [cti.md](cti.md) | [CTI](../../maturity-assessment/cti/) |
| Gestión de vulnerabilidades | [vulnerability-management.md](vulnerability-management.md) | [Vulnerabilidades](../../maturity-assessment/vulnerability-management/) |
| Cacería de amenazas | [threat-hunting.md](threat-hunting.md) | [Cacería](../../maturity-assessment/threat-hunting/) |
| Respuesta a incidentes | [incident-response.md](incident-response.md) | [Respuesta a incidentes](../../maturity-assessment/incident-response/) |
| Comunicaciones | [communications.md](communications.md) | [Comunicaciones](../../maturity-assessment/communications/) |

## El marco común: NIST CSF 2.0

El **Cybersecurity Framework 2.0** (febrero de 2024) organiza la ciberseguridad en seis funciones. Todas las guías de esta carpeta indican qué categorías del CSF cubren.

| Función | Propósito | Categorías |
|---|---|---|
| **Gobernar (GV)** | Estrategia, roles, políticas y supervisión de la ciberseguridad | GV.OC contexto · GV.RM gestión de riesgos · GV.RR roles y responsabilidades · GV.PO política · GV.OV supervisión · GV.SC cadena de suministro |
| **Identificar (ID)** | Conocer activos y riesgos | ID.AM activos · ID.RA evaluación de riesgos · ID.IM mejora |
| **Proteger (PR)** | Salvaguardas | PR.AA identidad y acceso · PR.AT concienciación · PR.DS datos · PR.PS plataformas · PR.IR resiliencia de la infraestructura |
| **Detectar (DE)** | Encontrar ataques en curso | DE.CM monitoreo continuo · DE.AE análisis de eventos adversos |
| **Responder (RS)** | Actuar ante un incidente | RS.MA gestión · RS.AN análisis · RS.CO comunicación · RS.MI mitigación |
| **Recuperar (RC)** | Restaurar operaciones | RC.RP ejecución del plan de recuperación · RC.CO comunicación de la recuperación |

## El punto de partida: CISA CPG 2.0

Los **Cross-Sector Cybersecurity Performance Goals 2.0** (diciembre de 2025) son el **mínimo recomendado** para cualquier organización de infraestructura crítica, sin importar su tamaño. Están alineados con el CSF 2.0, agregan la función Gobernar y cubren IT y OT. Cada objetivo indica el riesgo que reduce, su costo, impacto y dificultad, lo que ayuda a priorizar con presupuesto limitado. CISA ofrece una hoja de trabajo y un módulo de evaluación en su herramienta gratuita **CSET**.

**Recomendación para LATAM:** organizaciones pequeñas, empiecen por CISA **Cyber Essentials** y los **CPG**. Medianas y reguladas, usen el **CSF 2.0** como estructura y las guías de cada proceso para el detalle.

## Publicaciones transversales

| Publicación | Para qué |
|---|---|
| NIST CSF 2.0 | Marco general y lenguaje común con la dirección |
| NIST SP 800-53 Rev. 5 | Catálogo de controles detallado |
| NIST SP 800-55 | Medición y métricas de seguridad |
| CISA Cross-Sector CPG 2.0 | Mínimos priorizados |
| CISA Cyber Essentials | Punto de partida para pequeñas organizaciones y gobiernos locales |
| NSA/CISA *Top Ten Cybersecurity Misconfigurations* | Errores de configuración más frecuentes en redes grandes |
