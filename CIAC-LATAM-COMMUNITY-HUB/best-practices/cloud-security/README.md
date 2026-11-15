# Seguridad en la nube

## Hoja de ruta mínima

| # | Control | Prioridad | Mitiga |
|---|---|---|---|
| 1 | MFA resistente a phishing para cuentas administrativas; cuenta raíz/global admin sin uso diario | 🔴 | T1078.004 |
| 2 | Registro de auditoría activado y retenido (CloudTrail, Azure Activity/Entra logs, Cloud Audit Logs) | 🔴 | Visibilidad |
| 3 | Sin almacenamiento público por defecto (S3, Blob, GCS) | 🔴 | T1530 |
| 4 | Sin llaves de acceso de larga duración; usar roles e identidades administradas | 🔴 | T1552.005 |
| 5 | Alertas de presupuesto y uso anómalo (criptominería) | 🟡 | T1496 |
| 6 | Servicios de postura nativos (Security Hub, Defender for Cloud, Security Command Center) | 🟡 | Configuración insegura |
| 7 | Revisión de aplicaciones OAuth con permisos amplios en M365 / Workspace | 🟡 | T1528 |
| 8 | Copias de seguridad inmutables o en cuenta separada | 🟡 | T1485, T1490 |

## Guías de esta carpeta
<!-- aws/, azure/, gcp/, m365/, workspace/ -->

## Referencias
- CIS Benchmarks de AWS, Azure, Google Cloud y Microsoft 365
- Modelo de responsabilidad compartida de cada proveedor
