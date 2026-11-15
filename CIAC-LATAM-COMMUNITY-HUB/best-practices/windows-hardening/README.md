# Bastionado de Windows

## Hoja de ruta mínima

| # | Control | Prioridad | Mitiga |
|---|---|---|---|
| 1 | Desactivar SMBv1 | 🔴 | T1210 |
| 2 | Contraseñas únicas del administrador local con **Windows LAPS** | 🔴 | T1078.003, T1021.002 |
| 3 | Habilitar **Credential Guard** y protección LSA (RunAsPPL) | 🔴 | T1003.001 |
| 4 | Reglas de **Attack Surface Reduction** de Microsoft Defender (primero en modo auditoría) | 🔴 | T1204, T1059 |
| 5 | Registro de PowerShell (Script Block y Module Logging) y Sysmon | 🔴 | Visibilidad |
| 6 | Bloquear macros de Office descargadas de Internet | 🔴 | T1566.001 |
| 7 | Desactivar LLMNR y NBT-NS | 🟡 | T1557.001 |
| 8 | Firma SMB y LDAP obligatoria; channel binding en LDAP | 🟡 | T1557 |
| 9 | Modelo de administración por niveles (tiering) en Active Directory | 🟡 | T1078.002 |
| 10 | Control de aplicaciones con App Control for Business o AppLocker | 🟢 | T1204.002 |

## Guías de esta carpeta
<!-- Agrega aquí cada guía con su enlace -->

## Referencias
- CIS Microsoft Windows Benchmarks
- Microsoft Security Baselines (Security Compliance Toolkit)
- Microsoft: protección de Active Directory y modelo de acceso empresarial
