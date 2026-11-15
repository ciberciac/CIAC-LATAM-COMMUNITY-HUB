# Madurez · Cacería de Amenazas

**Modelo de referencia:** Hunting Maturity Model · TaHiTI · PEAK

Mide la capacidad de cacería con el **Hunting Maturity Model** (HM0–HM4) y las prácticas de **TaHiTI** y **PEAK**. Requisito previo: un monitoreo básico funcionando (dominio SOC en nivel 2 o más).

## Autoevaluación

Califica cada criterio con la [escala común 0–4](../escala-y-metodo.md). 🔴 = imprescindible incluso para equipos pequeños.

| ID | Área | Criterio | Evidencia esperada | Referencia | Actual | Objetivo |
|---|---|---|---|---|---|---|
| TH-01 | Organización | 🔴 La cacería tiene mandato y tiempo asignado, no solo cuando sobra tiempo | Asignación formal de horas o personas | SOC-CMM · Servicio de cacería | | |
| TH-02 | Organización | Metodología adoptada y documentada (TaHiTI, PEAK u otra) | Procedimiento de cacería | TaHiTI · PEAK | | |
| TH-03 | Iniciar | Backlog priorizado de cacerías con disparadores de inteligencia y de brechas de cobertura | Backlog con prioridades | TaHiTI · Fase Iniciar | | |
| TH-04 | Cazar | 🔴 Hipótesis documentadas y mapeadas a técnicas ATT&CK | Plantillas de cacería completas | TaHiTI · MITRE ATT&CK | | |
| TH-05 | Datos | 🔴 Telemetría disponible (endpoint, identidad, red, nube) con retención suficiente para cazar hacia atrás | Inventario de fuentes y retención | SOC-CMM · Tecnología | | |
| TH-06 | Cazar | Técnicas de análisis más allá de buscar IOCs: apilamiento, línea base, estadística, modelos | Consultas y cuadernos de análisis | PEAK · Hunting Maturity Model | | |
| TH-07 | Finalizar | Cada cacería se documenta con su resultado (probada, refutada, no concluyente, fallida) | Repositorio de cacerías | TaHiTI · Fase Finalizar | | |
| TH-08 | Finalizar | Las cacerías exitosas se convierten sistemáticamente en detecciones | Reglas con referencia a la cacería de origen | Hunting Maturity Model · HM4 | | |
| TH-09 | Finalizar | Traspaso a respuesta a incidentes, inteligencia y gestión de vulnerabilidades | Registros de traspaso | TaHiTI · Traspaso | | |
| TH-10 | Medición | Métricas de valor: permanencia del atacante, detecciones creadas, brechas de visibilidad | Informe de métricas | TaHiTI · Métricas | | |

**Puntaje del dominio** (promedio): ____ / 4

## Referencias
- Hunting Maturity Model (Sqrrl, David Bianco)
- [TaHiTI](../../threat-hunting/frameworks/tahiti.md) y herramienta *MaGMa for threat hunting*
- [PEAK](../../threat-hunting/frameworks/peak.md)
