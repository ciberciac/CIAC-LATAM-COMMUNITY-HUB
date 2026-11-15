# Cacería · <Nombre>

> Plantilla basada en la plantilla de investigación de TaHiTI. Anonimiza todo dato de la organización antes de publicar.

| | |
|---|---|
| **ID** | HUNT-AAAA-NNN |
| **Estado** | Backlog · En curso · Probada · Refutada · No concluyente · Fallida |
| **Tipo** | Hipótesis · Línea base · Asistida por modelos · Situacional |
| **Disparador** | Inteligencia · ATT&CK · Incidente · Cacería previa · Brecha de cobertura (MaGMa) |
| **Prioridad** | Alta · Media · Baja |
| **Cazador(es) · fechas** | @usuario · AAAA-MM-DD → AAAA-MM-DD |

## 1. Resumen (abstract)
Qué se quiere investigar y por qué, en dos o tres líneas.

## 2. Contexto de inteligencia
Actor, campaña o técnica que motiva la cacería; relevancia para el sector y país. Enlaces a [`threat-profiles`](../../threat-intelligence/threat-profiles/).

## 3. Hipótesis
> Si **[actor/comportamiento]** está presente en **[alcance]**, entonces observaremos **[evidencia]** en **[fuente de datos]**.

## 4. Alcance

| | |
|---|---|
| Sistemas | Estaciones Windows / servidores / nube |
| Período | Últimos 30 días |
| Técnicas ATT&CK | T1053.005 |
| Fuentes de datos | Sysmon EID 1, Security 4698, EDR |

## 5. Técnicas de análisis
Consultas, apilamiento (*stacking*), agrupación, línea de tiempo, visualización, modelos.

## 6. Consultas
```kql
// consulta utilizada
```

## 7. Resultados
Qué se encontró, qué se descartó y por qué. Falsos positivos identificados.

## 8. Validación de la hipótesis
**Resultado:** Probada · Refutada · No concluyente · Fallida
**Justificación:**

## 9. Traspasos

| Proceso | Acción | Enlace |
|---|---|---|
| Respuesta a incidentes | | |
| Detección (nuevo caso de uso / regla) | | [`detection-as-code`](../../detection-as-code/) |
| Inteligencia de amenazas | | |
| Gestión de vulnerabilidades / configuración | | |
| Registro (nuevas fuentes o campos) | | |

## 10. Lecciones aprendidas
Qué aprendimos del entorno, de los datos y del proceso.

## 11. Métricas
- Tiempo de permanencia del hallazgo (si aplica):
- Detecciones creadas o actualizadas:
- Brechas de visibilidad identificadas:
