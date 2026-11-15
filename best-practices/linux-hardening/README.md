# Bastionado de Linux

## Hoja de ruta mínima

| # | Control | Prioridad | Mitiga |
|---|---|---|---|
| 1 | SSH solo con llaves, sin acceso directo de `root` | 🔴 | T1110, T1021.004 |
| 2 | Actualizaciones de seguridad automáticas o con ventana definida | 🔴 | T1190 |
| 3 | Cortafuegos local con política por defecto de denegar (nftables/ufw/firewalld) | 🔴 | T1046 |
| 4 | `sudo` con mínimo privilegio y registro; sin `NOPASSWD` general | 🔴 | T1548.003 |
| 5 | Auditoría con `auditd` y envío de logs a un servidor central | 🔴 | Visibilidad |
| 6 | SELinux o AppArmor en modo *enforcing* | 🟡 | T1068 |
| 7 | Montar `/tmp` y `/dev/shm` con `noexec,nosuid,nodev` | 🟡 | T1059.004 |
| 8 | Eliminar servicios y paquetes innecesarios | 🟡 | Superficie de ataque |
| 9 | Monitoreo de integridad de archivos (AIDE) | 🟢 | T1565.001 |

## Guías de esta carpeta
<!-- Agrega aquí cada guía con su enlace -->

## Referencias
- CIS Distribution Independent Linux y benchmarks por distribución
- DISA STIG para RHEL y Ubuntu
