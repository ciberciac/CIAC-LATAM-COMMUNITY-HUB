# Playbook · Ransomware

| | |
|---|---|
| **Severidad por defecto** | Crítica |
| **ATT&CK principal** | T1486 Data Encrypted for Impact · T1490 Inhibit System Recovery · T1567 Exfiltration Over Web Service |
| **Roles** | Líder de incidente, equipo técnico, legal, comunicaciones, dirección |

## 0. Preparación
- [ ] Copias de seguridad **offline o inmutables**, con restauración probada.
- [ ] Inventario de activos críticos y orden de recuperación acordado con el negocio.
- [ ] Contactos fuera de banda (teléfonos, mensajería alternativa): el correo puede estar comprometido.
- [ ] Contratos vigentes: respuesta a incidentes, seguro cibernético, asesoría legal.
- [ ] Este playbook impreso o disponible fuera de la red corporativa.

## 1. Detección y análisis
- [ ] Confirmar el incidente: notas de rescate, extensiones nuevas, alertas de EDR, cifrado masivo.
- [ ] **Identificar la variante:** nota de rescate, extensión, ID Ransomware (https://id-ransomware.malwarehunterteam.com).
- [ ] Determinar alcance: equipos, servidores, cuentas y ubicaciones afectadas.
- [ ] Buscar **exfiltración previa** (doble extorsión): tráfico saliente inusual, herramientas como rclone, MEGAsync, WinSCP.
- [ ] Establecer el **paciente cero** y la línea de tiempo: acceso inicial frecuente → VPN sin MFA, RDP expuesto, phishing, vulnerabilidad en equipo de borde.
- [ ] Abrir el registro del incidente y activar el comité de crisis.

## 2. Contención
- [ ] **Aislar** equipos afectados de la red (desde el EDR o desconectando el cable). **No apagar** si se puede evitar: se pierde la memoria.
- [ ] Bloquear el acceso remoto (VPN, RDP) hasta confirmar que no es el vector.
- [ ] Deshabilitar cuentas comprometidas y **restablecer credenciales privilegiadas**, incluida la cuenta `krbtgt` (dos veces, con intervalo) si el dominio está comprometido.
- [ ] Proteger las copias de seguridad: desconectarlas y verificar que no estén cifradas.
- [ ] Preservar evidencia: imagen de memoria y disco de equipos clave, logs de firewall, VPN, EDR y controlador de dominio.

## 3. Erradicación
- [ ] Eliminar persistencia: tareas programadas, servicios, GPO maliciosas, cuentas creadas por el atacante.
- [ ] Retirar herramientas del atacante (Cobalt Strike, AnyDesk, etc.).
- [ ] Cerrar el vector de acceso inicial (parche, MFA, cierre de puertos).
- [ ] Búsqueda de compromiso en todo el entorno con los IOCs y TTPs identificados.

## 4. Recuperación
- [ ] Restaurar desde copias **verificadas como limpias**, en el orden acordado.
- [ ] Reconstruir en lugar de "limpiar" los sistemas críticos cuando sea posible.
- [ ] Revisar descifradores gratuitos en **No More Ransom** (https://www.nomoreransom.org).
- [ ] Monitoreo reforzado durante al menos 30 días.

## Decisión sobre el pago
No es una decisión técnica. Involucra a dirección, legal y aseguradora. Considerar: el pago no garantiza el descifrado ni la eliminación de los datos robados, puede tener implicaciones legales (sanciones) y financia nuevos ataques.

## Comunicación y notificaciones
- [ ] Verificar con legal las notificaciones obligatorias en tu país y sector (protección de datos, regulador, CSIRT nacional) y sus plazos.
- [ ] Comunicación interna y externa coordinada por un único vocero.
- [ ] Denuncia ante la autoridad competente.

## 5. Lecciones aprendidas
- [ ] Reunión post-incidente en un máximo de dos semanas.
- [ ] Informe final con [`templates/incident-report.md`](../../templates/incident-report.md).
- [ ] Actualizar detecciones, este playbook y el plan de copias de seguridad.

## Referencias
- NIST SP 800-61r3 · CISA #StopRansomware Guide · No More Ransom
