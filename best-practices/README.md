# Buenas prácticas

Guías de configuración segura pensadas para equipos de la región, desde la pyme con una sola persona de TI hasta el SOC de una entidad financiera.

| Carpeta | Alcance |
|---|---|
| [windows-hardening](windows-hardening/) | Estaciones y servidores Windows, Active Directory |
| [linux-hardening](linux-hardening/) | Servidores Linux (Debian/Ubuntu, RHEL y derivados) |
| [cloud-security](cloud-security/) | AWS, Azure, Google Cloud y Microsoft 365 / Google Workspace |
| [identity-security](identity-security/) | Identidades, MFA, cuentas privilegiadas y acceso |
| [ai-secure-development](ai-secure-development/) | Programar con IA, construir aplicaciones y agentes con LLM, y usar IA en operaciones de seguridad |

## Cómo está organizada cada guía

1. **Contexto:** por qué importa y qué amenazas mitiga (con técnicas ATT&CK).
2. **Prioridad:** 🔴 imprescindible · 🟡 recomendado · 🟢 deseable.
3. **Implementación:** pasos o comandos probados, con la versión.
4. **Verificación:** cómo comprobar que quedó aplicado.
5. **Impacto:** qué se puede romper y cómo revertir.
6. **Referencias:** CIS Benchmark, CIS Controls v8.1, NIST, OWASP, guía del fabricante.

Para empezar una guía nueva copia [`_plantilla.md`](_plantilla.md).
