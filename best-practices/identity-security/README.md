# Seguridad de identidades

## Hoja de ruta mínima

| # | Control | Prioridad | Mitiga |
|---|---|---|---|
| 1 | MFA para todo acceso remoto, correo y VPN | 🔴 | T1078, T1110 |
| 2 | MFA resistente a phishing (FIDO2 / passkeys) para administradores | 🔴 | T1557, T1111 |
| 3 | Bloquear autenticación heredada (IMAP, POP, SMTP AUTH básico) | 🔴 | T1110.003 |
| 4 | Inventario y revisión periódica de cuentas privilegiadas y de servicio | 🔴 | T1078 |
| 5 | Baja de cuentas el mismo día del retiro de la persona | 🔴 | T1078 |
| 6 | Acceso condicional por ubicación, dispositivo y riesgo | 🟡 | T1078 |
| 7 | Contraseñas largas + verificación contra listas filtradas, sin rotación forzada arbitraria (NIST SP 800-63B) | 🟡 | T1110 |
| 8 | Acceso privilegiado justo a tiempo (PIM/PAM) | 🟢 | T1078.002 |

## Guías de esta carpeta
<!-- Agrega aquí cada guía con su enlace -->

## Referencias
- NIST SP 800-63B (Digital Identity Guidelines)
- CISA: Implementing Phishing-Resistant MFA
