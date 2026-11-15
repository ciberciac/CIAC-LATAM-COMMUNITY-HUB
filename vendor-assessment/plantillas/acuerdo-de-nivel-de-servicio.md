# Estructura de acuerdo de nivel de servicio (SLA)

> Los tiempos son **ejemplos** para iniciar la negociación. Ajústalos a tu riesgo, presupuesto y regulación.

## Definiciones (deben estar en el contrato)
- **Tiempo de reconocimiento:** desde que se genera la alerta hasta que un analista la toma.
- **Tiempo de notificación:** desde que se confirma el incidente hasta que el cliente recibe la notificación con contexto.
- **Tiempo de inicio de contención:** desde la confirmación hasta la primera acción de contención (propia o del cliente con instrucciones).
- **Incidente confirmado:** criterio explícito de cuándo una alerta pasa a ser incidente.

## Matriz de severidad (ejemplo)

| Severidad | Criterio | Reconocimiento | Notificación | Inicio de contención | Canal |
|---|---|---|---|---|---|
| **Crítica** | Ransomware, exfiltración en curso, compromiso de cuentas privilegiadas | 15 min | 30 min | 1 h | Teléfono + ticket |
| **Alta** | Malware activo, acceso no autorizado confirmado | 30 min | 2 h | 4 h | Teléfono o mensajería + ticket |
| **Media** | Actividad sospechosa que requiere análisis | 2 h | 8 h | Según análisis | Ticket |
| **Baja** | Violaciones de política, eventos informativos | 8 h | Informe periódico | — | Informe |

## Indicadores mensuales
- Cumplimiento del SLA por severidad (%).
- Alertas atendidas, incidentes confirmados y falsos positivos.
- Fuentes de registro activas vs. contratadas, y tiempo sin recibir datos de cada fuente.
- Casos de uso nuevos o ajustados.
- Cobertura ATT&CK frente a la línea base acordada.

## Disponibilidad
- Disponibilidad de la plataforma y del portal del cliente.
- Aviso previo de mantenimientos.

## Incumplimientos
- Créditos o penalizaciones por incumplimiento reiterado.
- Derecho a terminar el contrato tras incumplimientos graves o repetidos.
