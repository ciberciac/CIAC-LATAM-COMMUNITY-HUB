# Cacería de amenazas (Threat Hunting)

Búsqueda proactiva de actividad maliciosa que evadió los controles existentes, con el objetivo de **reducir el tiempo de permanencia del atacante** (*dwell time*) y mejorar continuamente la detección.

## Estructura

```
threat-hunting/
├── frameworks/          ← metodologías de referencia explicadas en español
│   ├── tahiti.md          TaHiTI: cacería dirigida por inteligencia
│   ├── magma.md           MaGMa: gestión de casos de uso de detección
│   └── peak.md            PEAK: hipótesis, línea base y modelos
├── hunts/               ← cacerías documentadas por la comunidad
│   └── _plantilla-hunt.md
└── backlog.md           ← ideas de cacería abiertas para que alguien las tome
```

## ¿Qué framework uso?

| Framework | Origen | Enfoque | Ideal para |
|---|---|---|---|
| [TaHiTI](frameworks/tahiti.md) | FI-ISAC Países Bajos (sector financiero), 2018 | Cacería estructurada disparada y enriquecida por inteligencia de amenazas | Equipos con función CTI y sectores regulados (banca, energía, gobierno) |
| [MaGMa](frameworks/magma.md) | FI-ISAC Países Bajos, 2017 | Gestión de casos de uso de monitoreo: de los riesgos del negocio a las reglas | Saber **qué ya se detecta** para no cazar lo que el SIEM ya cubre, y medir cobertura |
| [PEAK](frameworks/peak.md) | Splunk SURGe, 2023 | Tres tipos de cacería: por hipótesis, por línea base y asistida por modelos | Equipos que quieren combinar hipótesis con análisis de datos y anomalías |

Se complementan: **MaGMa** dice dónde están las brechas de detección, **TaHiTI** organiza la cacería a partir de la inteligencia, y **PEAK** amplía las técnicas de análisis. Todos usan **MITRE ATT&CK** como lenguaje común.

## Tipos de cacería

| Tipo | Punto de partida | Ejemplo |
|---|---|---|
| **Estructurada (por hipótesis)** | Inteligencia, una técnica ATT&CK o un hallazgo previo | "Un actor que ataca banca en la región usa tareas programadas para persistir en estaciones de trabajo" |
| **No estructurada (por datos)** | Exploración de datos y anomalías | Procesos que se ejecutan una sola vez en todo el parque |
| **Situacional** | Un evento externo | Vulnerabilidad explotada masivamente en un equipo de borde que usamos |

## Pirámide del dolor
Prioriza cacerías en la parte alta (herramientas y TTP). Buscar hashes o IPs es rápido pero el atacante los cambia en minutos; un comportamiento es mucho más difícil de cambiar.

## Modelo de madurez de cacería (*Hunting Maturity Model*)

| Nivel | Nombre | Característica |
|---|---|---|
| HM0 | Inicial | Solo alertas automáticas, sin cacería |
| HM1 | Mínimo | Búsquedas de IOCs a partir de inteligencia |
| HM2 | Procedimental | Sigue procedimientos de cacería creados por otros |
| HM3 | Innovador | Crea sus propios procedimientos y análisis |
| HM4 | Líder | Automatiza las cacerías exitosas como detecciones |

## Del hallazgo a la detección
Toda cacería termina con un **traspaso**: incidente a [incident-response](../incident-response/), nueva regla a [detection-as-code](../detection-as-code/), nueva inteligencia a [threat-intelligence](../threat-intelligence/), o recomendación a [best-practices](../best-practices/).
