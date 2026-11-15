# Madurez · Centro de Operaciones de Seguridad (SOC)

**Modelo de referencia:** SOC-CMM

Mide la capacidad del SOC propio o tercerizado en las cinco dimensiones del **SOC-CMM**: negocio, personas, procesos, tecnología y servicios.

## Autoevaluación

Califica cada criterio con la [escala común 0–4](../escala-y-metodo.md). 🔴 = imprescindible incluso para equipos pequeños.

| ID | Área | Criterio | Evidencia esperada | Referencia | Actual | Objetivo |
|---|---|---|---|---|---|---|
| SOC-01 | Negocio | 🔴 El SOC tiene un mandato aprobado por la dirección: alcance, servicios y autoridad | Documento de mandato o estatuto firmado | SOC-CMM · Negocio | | |
| SOC-02 | Negocio | Existe un catálogo de servicios con niveles de servicio acordados | Catálogo de servicios y SLA | SOC-CMM · Servicios | | |
| SOC-03 | Negocio | 🔴 Los requisitos regulatorios aplicables (regulador sectorial, protección de datos) están identificados | Matriz de requisitos regulatorios | SOC-CMM · Negocio | | |
| SOC-04 | Personas | Roles, perfiles de competencia y plan de carrera definidos (analistas L1/L2/L3, ingeniería de detección) | Descripciones de cargo y matriz de competencias | SOC-CMM · Personas | | |
| SOC-05 | Personas | Plan de formación con práctica (laboratorios, CTF, simulacros) | Plan anual de formación y registros | SOC-CMM · Personas | | |
| SOC-06 | Personas | Gestión de turnos, carga de trabajo y fatiga de alertas | Cuadro de turnos, métricas de carga | SOC-CMM · Personas | | |
| SOC-07 | Procesos | 🔴 Procedimientos de triage, análisis y escalamiento documentados | Procedimientos operativos vigentes | SOC-CMM · Procesos | | |
| SOC-08 | Procesos | Casos de uso de detección gestionados con ciclo de vida (alta, cambio, baja) | Inventario de casos de uso (p. ej. MaGMa) | SOC-CMM · Procesos · MaGMa | | |
| SOC-09 | Procesos | 🔴 Métricas operativas (tiempo de detección, de respuesta, falsos positivos) reportadas periódicamente | Tablero o informe mensual | SOC-CMM · Procesos | | |
| SOC-10 | Tecnología | 🔴 Fuentes de registro de los activos críticos integradas, con retención definida | Inventario de fuentes vs. activos críticos | SOC-CMM · Tecnología | | |
| SOC-11 | Tecnología | Plataformas de detección y respuesta (SIEM, EDR/XDR, SOAR) con automatizaciones documentadas | Arquitectura y catálogo de automatizaciones | SOC-CMM · Tecnología | | |
| SOC-12 | Servicios | Cobertura de detección medida contra las técnicas ATT&CK de actores relevantes para el sector y la región | Capa de ATT&CK Navigator con cobertura | SOC-CMM · Servicios · MITRE ATT&CK | | |
| SOC-13 | Servicios | Revisión periódica de capacidades y mejora continua a partir de incidentes y cacerías | Actas de revisión y plan de mejora | SOC-CMM · Servicios | | |

**Puntaje del dominio** (promedio): ____ / 4

## Referencias
- SOC-CMM: https://www.soc-cmm.com (herramienta oficial de autoevaluación en dos versiones, básica y avanzada)
- ITU-T X.1060: marco para construir y operar un centro de ciberdefensa
