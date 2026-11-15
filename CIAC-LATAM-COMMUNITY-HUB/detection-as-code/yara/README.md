# YARA

Estructura: `ransomware/`, `stealers/`, `rats/`, `loaders/`, `troyanos-bancarios/`, `webshells/`.

- Un archivo `.yar` por familia o comportamiento; reglas con prefijo `CIAC_`.
- `meta` obligatorio: `author`, `description`, `date`, `reference`, `hash` (muestra de referencia, si existe), `mitre_attack`, `status`, `license = "DRL 1.1"`.
- Evita cadenas demasiado genéricas; incluye `filesize` y una condición estructural cuando sea posible.

Validar: `yara -w ruta/regla.yar /dev/null` o `python -c "import yara; yara.compile(filepath='ruta/regla.yar')"`.
