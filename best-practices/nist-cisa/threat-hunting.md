# Cacería de Amenazas · NIST y CISA

**CSF 2.0:** DE.CM monitoreo continuo · DE.AE análisis de eventos adversos · ID.RA-03 amenazas identificadas · ID.IM mejora

## NIST

| Publicación | Prácticas clave |
|---|---|
| **SP 800-53 Rev. 5 · RA-10 Threat Hunting** | Establecer y mantener una capacidad de cacería para buscar indicadores de compromiso y detectar, seguir y desarticular amenazas que evaden los controles existentes, con una frecuencia definida por la organización |
| **SP 800-53 Rev. 5** | SI-4 monitoreo (insumo de la cacería) · PM-16 conciencia de amenazas (insumo de hipótesis) |
| **SP 800-61 Rev. 3** | Reconoce la cacería como fuente de detección de incidentes y de mejora |

## CISA (con agencias aliadas)

| Recurso | Prácticas clave |
|---|---|
| **Avisos conjuntos** sobre actores como los que usan técnicas *living off the land* | Incluyen consultas y comportamientos concretos para cazar; base para hipótesis |
| **Best Practices for Event Logging and Threat Detection** | La detección de *living off the land* requiere línea base de comportamiento normal y registros con detalle suficiente (línea de comandos, procesos padre) |
| **Priority Logs for SIEM Ingestion** | Qué telemetría necesitas para poder cazar |
| **Best Practices for MITRE ATT&CK Mapping** y **Decider** | Formular hipótesis y documentar hallazgos con técnicas ATT&CK |

## Lista de verificación

| Práctica | Fuente | Madurez |
|---|---|---|
| Capacidad de cacería establecida con frecuencia definida | SP 800-53 RA-10 | TH-01 |
| Hipótesis basadas en inteligencia y avisos actuales | PM-16 · avisos de CISA | TH-03, TH-04 |
| Telemetría con detalle suficiente (línea de comandos, proceso padre, autenticación) | CISA logging · Priority Logs | TH-05 |
| Línea base de comportamiento normal para detectar abuso de herramientas legítimas | CISA logging | TH-06 |
| Hallazgos documentados con técnicas ATT&CK | CISA ATT&CK Mapping | TH-07 |
| Hallazgos convertidos en detecciones y mejoras | CSF ID.IM · SP 800-61r3 | TH-08 |

Ver también los frameworks de [threat-hunting](../../threat-hunting/frameworks/) (TaHiTI, MaGMa, PEAK).
