# Sigma

Estructura por plataforma: `windows/`, `linux/`, `macos/`, `cloud/`, `network/`, `web/`.

**Nombre de archivo** (convención SigmaHQ): `<categoria>_<plataforma>_<comportamiento>.yml`
Ejemplo: `proc_creation_win_vssadmin_borrado_shadow.yml`

**Campos obligatorios:** `title`, `id` (UUID v4 nuevo), `status`, `description`, `references`, `author`, `date`, `tags` (`attack.<tactica>`, `attack.tXXXX`), `logsource`, `detection`, `falsepositives`, `level`.

**Validar antes del PR:**
```bash
pip install sigma-cli
sigma check sigma/
```

Especificación: https://sigmahq.io/docs/basics/rules.html
