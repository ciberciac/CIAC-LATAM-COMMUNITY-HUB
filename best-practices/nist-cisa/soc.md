# Centro de Operaciones de Seguridad · NIST y CISA

**CSF 2.0:** DE.CM monitoreo continuo · DE.AE análisis de eventos adversos · PR.PS plataformas (generación de registros) · ID.IM mejora

## NIST

| Publicación | Prácticas clave |
|---|---|
| **SP 800-137** · Monitoreo continuo de la seguridad (ISCM) | Definir una estrategia de monitoreo basada en riesgo; establecer métricas y frecuencias; analizar, responder y revisar la estrategia periódicamente |
| **SP 800-92** · Gestión de registros (y su revisión 1, en borrador, como guía de planificación) | Política de registro: qué se registra, cuánto se retiene, quién accede; centralizar; proteger la integridad de los registros; sincronizar la hora |
| **SP 800-53 Rev. 5** | AU (auditoría y registro): eventos auditables, revisión y análisis (AU-6), protección (AU-9) · SI-4 monitoreo del sistema · CA-7 monitoreo continuo · IR-4 manejo de incidentes |

## CISA (con agencias aliadas)

| Guía | Prácticas clave |
|---|---|
| **Best Practices for Event Logging and Threat Detection** (2024, liderada por el ACSC de Australia) | Política de registro aprobada por la dirección; registro centralizado y correlacionado; almacenamiento seguro e íntegro; detección de técnicas *living off the land* comparando contra una línea base |
| **Implementing SIEM and SOAR Platforms** (mayo de 2025, guías para ejecutivos y para técnicos) | Definir alcance y casos de uso antes de comprar; personal dedicado y formado; implementar SIEM antes que SOAR; probar las automatizaciones para que no interrumpan la operación |
| **Priority Logs for SIEM Ingestion** (mayo de 2025) | Priorizar fuentes: EDR, dispositivos de red, controladores de dominio, sistemas operativos Windows/Linux, nube, sistemas de identidad; no usar el SIEM como depósito de todos los registros |
| **Logging Made Easy (LME)** | Solución gratuita de CISA para centralizar registros en organizaciones con pocos recursos |

## Lista de verificación

| Práctica | Fuente | Madurez |
|---|---|---|
| Política de registro aprobada (qué, cuánto tiempo, quién accede) | SP 800-92 · CISA logging | SOC-10 |
| Fuentes prioritarias integradas: EDR, controladores de dominio, identidad, red, nube | CISA Priority Logs | SOC-10 |
| Hora sincronizada en todos los sistemas | SP 800-92 | SOC-10 |
| Registros protegidos contra modificación y borrado | SP 800-53 AU-9 · CISA logging | SOC-10 |
| Casos de uso definidos antes de ampliar la plataforma | CISA SIEM/SOAR | SOC-08 |
| Automatizaciones probadas y documentadas | CISA SIEM/SOAR | SOC-11 |
| Personal dedicado y formado para operar la plataforma | CISA SIEM/SOAR | SOC-04, SOC-05 |
| Métricas de monitoreo revisadas periódicamente | SP 800-137 | SOC-09 |
| Detección de abuso de herramientas legítimas (*living off the land*) con línea base | CISA logging | SOC-12 |

## Para equipos pequeños
Empieza por centralizar EDR, controladores de dominio y correo/identidad en la nube (LME es una opción gratuita), con 90 días de retención como mínimo.
