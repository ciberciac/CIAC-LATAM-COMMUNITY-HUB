# Playbook · Phishing

| | |
|---|---|
| **Severidad por defecto** | Media (alta si hubo clic con ingreso de credenciales o ejecución) |
| **ATT&CK principal** | T1566.001 Attachment · T1566.002 Link · T1204 User Execution · T1078 Valid Accounts |

## 0. Preparación
- [ ] Botón o buzón para que los usuarios reporten correos sospechosos.
- [ ] SPF, DKIM y **DMARC** configurados (idealmente `p=reject`).
- [ ] Capacidad de buscar y eliminar correos en todos los buzones.
- [ ] Concientización periódica con ejemplos locales: entidades tributarias, bancos, servicios de mensajería, facturación electrónica.

## 1. Detección y análisis
- [ ] Obtener el correo **original con cabeceras** (no reenviado).
- [ ] Analizar remitente, ruta de entrega, resultado SPF/DKIM/DMARC.
- [ ] Analizar enlaces y adjuntos en entorno aislado (urlscan.io, sandbox). **No abrir en el equipo del analista.**
- [ ] Determinar el alcance: ¿cuántos lo recibieron? ¿quién hizo clic, ingresó credenciales o ejecutó el adjunto?

## 2. Contención
- [ ] Eliminar el correo de todos los buzones.
- [ ] Bloquear remitente, dominio, URLs y hashes en correo, proxy y EDR.
- [ ] Si se ingresaron credenciales: **restablecer contraseña, revocar sesiones y tokens**, revisar MFA registrados.
- [ ] Si se ejecutó un adjunto: aislar el equipo y pasar a análisis de endpoint.

## 3. Erradicación
- [ ] Revisar reglas de bandeja creadas por el atacante y aplicaciones OAuth autorizadas.
- [ ] Analizar el equipo afectado y eliminar el malware o reconstruirlo.

## 4. Recuperación
- [ ] Devolver el acceso al usuario con MFA verificado.
- [ ] Monitorear inicios de sesión de las cuentas afectadas durante 30 días.

## 5. Lecciones aprendidas
- [ ] ¿Por qué pasó el filtro? Ajustar reglas de correo.
- [ ] Compartir el caso (anonimizado) en [`threat-intelligence/IOC-analysis`](../../threat-intelligence/IOC-analysis/).
- [ ] Retroalimentar al usuario que reportó: refuerza el comportamiento.

## Referencias
- NIST SP 800-61r3 · CISA: Phishing Guidance
