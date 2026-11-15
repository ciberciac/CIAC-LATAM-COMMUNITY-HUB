# Playbook · Business Email Compromise (BEC)

| | |
|---|---|
| **Severidad por defecto** | Alta (crítica si hubo transferencia) |
| **ATT&CK principal** | T1078.004 Cloud Accounts · T1114.003 Email Forwarding Rule · T1534 Internal Spearphishing · T1656 Impersonation |

> ⏱️ **Si hubo una transferencia fraudulenta, el tiempo es crítico.** Contacta de inmediato a tu banco para solicitar la retención o reversión de los fondos y presenta la denuncia. Las primeras horas determinan si se recupera el dinero.

## 0. Preparación
- [ ] **Verificación fuera de banda** obligatoria para cambios de cuenta bancaria de proveedores o pagos urgentes: llamada a un número ya conocido, nunca al que viene en el correo.
- [ ] MFA en todo el correo y bloqueo de autenticación heredada.
- [ ] Alertas por reglas de reenvío externo y por inicios de sesión desde países inusuales.
- [ ] Contacto directo con el área de fraude del banco.

## 1. Detección y análisis
- [ ] Identificar cuentas comprometidas: inicios de sesión anómalos, viajes imposibles, nuevos métodos MFA.
- [ ] Revisar **reglas de bandeja** (reenvío, mover a carpetas ocultas, eliminar respuestas).
- [ ] Revisar aplicaciones OAuth y dispositivos registrados.
- [ ] Buscar correos enviados por el atacante: a proveedores, clientes o personal de finanzas.
- [ ] Determinar si hubo **pérdida económica**, monto y cuentas destino.
- [ ] Distinguir: ¿cuenta propia comprometida, cuenta del proveedor comprometida o dominio parecido (*typosquatting*)?

## 2. Contención
- [ ] Restablecer contraseña, **revocar todas las sesiones y tokens**, eliminar MFA y dispositivos desconocidos.
- [ ] Eliminar reglas de bandeja y aplicaciones maliciosas.
- [ ] Bloquear dominios parecidos y remitentes del atacante.
- [ ] Avisar a contrapartes afectadas (proveedores, clientes) por un canal verificado.

## 3. Erradicación
- [ ] Revisar otras cuentas con el mismo patrón de acceso.
- [ ] Confirmar que no haya persistencia en la nube (aplicaciones, delegaciones de buzón, permisos de envío como).

## 4. Recuperación
- [ ] Seguimiento con el banco y las autoridades.
- [ ] Revisar y reforzar el proceso de pagos.

## 5. Lecciones aprendidas
- [ ] ¿Qué control de proceso falló? (verificación de cambios bancarios, doble aprobación).
- [ ] Capacitación específica para finanzas, compras y dirección.

## Referencias
- NIST SP 800-61r3 · FBI IC3: Business Email Compromise · Microsoft: respuesta a compromiso de cuentas en Microsoft 365
