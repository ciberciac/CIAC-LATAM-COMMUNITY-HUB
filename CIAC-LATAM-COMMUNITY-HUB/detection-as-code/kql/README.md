# KQL (Microsoft Sentinel / Defender XDR)

Un archivo `.kql` por detección o búsqueda, organizado por tabla o dominio: `endpoint/`, `identity/`, `email/`, `cloud/`.

Cabecera obligatoria:
```kql
// Título:            Borrado de shadow copies con vssadmin
// ATT&CK:            T1490
// Tabla:             DeviceProcessEvents
// Sigma equivalente: sigma/windows/proc_creation_win_vssadmin_borrado_shadow.yml
// Falsos positivos:  Software de copias de seguridad
// Estado:            experimental
// Autor / fecha:     @usuario / 2026-11-14
```
