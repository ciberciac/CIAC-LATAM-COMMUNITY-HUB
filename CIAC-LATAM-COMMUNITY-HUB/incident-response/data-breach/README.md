# Playbook · Brecha de datos (Data Breach)

| | |
|---|---|
| **Qué es** | **Acceso no autorizado confirmado** a información por parte de un tercero, con o sin extracción demostrada |
| **Ejemplos** | Robo de base de datos de clientes, exfiltración previa a un ransomware (doble extorsión), acceso con credenciales robadas a un sistema con datos personales, empleado que extrae información sin autorización |
| **Severidad por defecto** | Alta (crítica si hay datos sensibles, de menores, financieros, de salud o volumen masivo) |
| **ATT&CK relacionado** | TA0009 Collection · TA0010 Exfiltration · T1567 Exfiltration Over Web Service · T1041 Exfiltration Over C2 Channel |

> ⏱️ **Los plazos legales corren desde que se conoce el incidente**, no desde que termina la investigación. Activa al área legal y al oficial de protección de datos en la primera hora. Varias leyes permiten una notificación preliminar que se completa después.

## 0. Preparación
- [ ] Inventario de bases de datos con datos personales, su responsable y la ley aplicable (registro de actividades de tratamiento).
- [ ] Plantillas aprobadas de notificación a autoridad y a titulares.
- [ ] Contratos con proveedores (encargados del tratamiento) que los obliguen a avisar de incidentes.
- [ ] Registro centralizado con retención suficiente para reconstruir accesos y transferencias.
- [ ] Asesoría legal y forense identificada de antemano.

## 1. Detección y análisis
- [ ] Abrir el registro del incidente y anotar la **fecha y hora de conocimiento** (inicia los plazos legales).
- [ ] Determinar el **vector de acceso** y la **línea de tiempo**: primer acceso, accesos a los datos, extracción.
- [ ] Determinar **qué datos y de cuántos titulares**: categorías de datos, si estaban cifrados, países de residencia de los titulares.
- [ ] Buscar evidencia de **exfiltración**: volumen de tráfico saliente, herramientas (rclone, MEGAsync, WinSCP), servicios en la nube, consultas masivas a bases de datos.
- [ ] Verificar si los datos están siendo **publicados o vendidos**: sitios de filtración de grupos de extorsión, foros, canales de mensajería. Sin interactuar ni pagar.
- [ ] Preservar evidencia con cadena de custodia: imágenes, registros de la base de datos, del firewall, del proxy, del EDR y de la nube.

## 2. Contención
- [ ] Cortar el acceso del atacante: deshabilitar cuentas, revocar sesiones y tokens, bloquear la infraestructura identificada.
- [ ] Bloquear el canal de exfiltración.
- [ ] Rotar credenciales del sistema afectado y de cuentas privilegiadas.
- [ ] Si el atacante contacta para extorsionar: no responder sin coordinación de dirección, legal y, si aplica, la aseguradora.

## 3. Erradicación
- [ ] Eliminar persistencia y herramientas del atacante.
- [ ] Cerrar el vector inicial (vulnerabilidad, configuración, credencial).
- [ ] Búsqueda de compromiso en sistemas relacionados ([threat-hunting](../../threat-hunting/)).

## 4. Recuperación
- [ ] Restablecer el servicio con controles reforzados (MFA, segmentación, registro de accesos a datos).
- [ ] Ofrecer a los titulares medidas de mitigación cuando corresponda: cambio de contraseñas, alertas de fraude, monitoreo de crédito.
- [ ] Monitoreo reforzado y vigilancia de la aparición de los datos en fuentes abiertas.

## Notificaciones en LATAM
Cada país define **a quién, en qué casos y en qué plazo** se notifica. La tabla es una guía inicial: **verifica siempre la norma vigente con el área legal**, porque cambia con frecuencia. Además de la autoridad de protección de datos pueden aplicar el regulador sectorial (financiero, telecomunicaciones, salud), el CSIRT nacional y contratos con clientes.

| País | Autoridad | Plazo de referencia | Norma | Verificado |
|---|---|---|---|---|
| 🇧🇷 Brasil | ANPD | 3 días hábiles desde el conocimiento, para incidentes con riesgo o daño relevante a los titulares; complemento hasta 20 días hábiles; plazo doble para agentes de pequeño porte | LGPD art. 48 · Resolución CD/ANPD 15/2024 | 2026-11 |
| 🇨🇴 Colombia | Superintendencia de Industria y Comercio (RNBD) | 15 días hábiles desde que se detecta y se pone en conocimiento del área encargada | Ley 1581 de 2012 · instrucciones de la SIC | 2026-11 |
| 🇲🇽 México | | | | Pendiente |
| 🇦🇷 Argentina | | | | Pendiente |
| 🇨🇱 Chile | | | | Pendiente |
| 🇵🇪 Perú | | | | Pendiente |
| 🇪🇨 Ecuador | | | | Pendiente |

> 🤝 **Contribución abierta:** si conoces la regulación de tu país, completa la fila con la fuente oficial y la fecha de verificación.

**Checklist de notificación**
- [ ] ¿Hay datos personales involucrados? ¿De residentes de qué países?
- [ ] ¿El incidente puede causar riesgo o daño relevante a los titulares?
- [ ] Notificación a la autoridad de protección de datos (y preliminar si falta información).
- [ ] Notificación al regulador sectorial y al CSIRT nacional si aplica.
- [ ] Comunicación a los titulares: clara, sin tecnicismos, con qué pasó, qué datos, qué hicimos y qué deben hacer.
- [ ] Denuncia ante la autoridad competente.
- [ ] Registro interno del incidente, aunque no sea notificable.

## 5. Lecciones aprendidas
- [ ] Revisión post-incidente en un máximo de dos semanas.
- [ ] Informe final con [`templates/incident-report.md`](../../templates/incident-report.md).
- [ ] Revisar minimización de datos: ¿necesitábamos guardar todo lo que se robó?

## Referencias
- NIST SP 800-61r3 · ISO/IEC 27035 · ISO/IEC 27701 · normas de protección de datos de cada país
