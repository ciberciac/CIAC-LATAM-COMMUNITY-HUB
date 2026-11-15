# Respuesta a incidentes

Playbooks para los incidentes más frecuentes en la región, estructurados según el ciclo de **NIST SP 800-61r3** (alineado con NIST CSF 2.0) e **ISO/IEC 27035**.

| Playbook | Cuándo usarlo |
|---|---|
| [ransomware](ransomware/) | Cifrado de archivos, notas de rescate o amenaza de publicación de datos |
| [phishing](phishing/) | Correo malicioso reportado o detectado, con o sin clic |
| [business-email-compromise](business-email-compromise/) | Cuenta de correo comprometida o fraude de pagos por suplantación |
| [data-leak](data-leak/) | Exposición no intencionada de datos: recurso público, credenciales en código, datos publicados por terceros |
| [data-breach](data-breach/) | Acceso no autorizado confirmado a datos, con o sin exfiltración demostrada; incluye notificaciones legales |

## Fases de cada playbook

| Fase | Pregunta clave |
|---|---|
| 0. Preparación | ¿Qué debe existir **antes** del incidente? |
| 1. Detección y análisis | ¿Qué pasó, desde cuándo y qué alcance tiene? |
| 2. Contención | ¿Cómo detengo la propagación sin destruir evidencia? |
| 3. Erradicación | ¿Cómo elimino al atacante y su persistencia? |
| 4. Recuperación | ¿Cómo vuelvo a operar de forma segura? |
| 5. Lecciones aprendidas | ¿Qué cambio para que no se repita? |

## Notificaciones en LATAM
Cada país tiene obligaciones distintas (autoridad de protección de datos, reguladores sectoriales como el financiero, CSIRT nacional). Todo playbook incluye un paso para **verificar con el área legal** qué notificaciones aplican y en qué plazo. Directorio de equipos de respuesta: https://www.first.org/members/teams/

Para documentar el incidente usa [`templates/incident-report.md`](../templates/incident-report.md).
