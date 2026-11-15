# MITRE ATT&CK

Mapeos de amenazas observadas en Latinoamérica al marco [MITRE ATT&CK](https://attack.mitre.org) (Enterprise).

## Estructura
```
MITRE-ATTACK/
├── mapeos/<amenaza>.md          ← técnica por técnica, con evidencia
└── navigator/<amenaza>.json     ← capa para ATT&CK Navigator
```

## Cómo mapear bien
- Mapea **comportamientos observados**, no capacidades teóricas de la herramienta.
- Usa siempre el **ID más específico** (sub-técnica `T1566.001` antes que `T1566`).
- Cada técnica con su **evidencia** (qué se vio) y su **fuente**.
- Indica la **versión de ATT&CK** usada.
- Relaciona cada técnica con detecciones de [`detection-as-code`](../../detection-as-code/) cuando existan.

Plantilla: [`_plantilla-mapeo.md`](_plantilla-mapeo.md) · Visualizar capas: https://mitre-attack.github.io/attack-navigator/
