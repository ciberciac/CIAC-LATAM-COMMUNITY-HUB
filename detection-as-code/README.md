# Detection as Code

Detecciones versionadas, revisadas y probadas como código. Licencia: [DRL 1.1](LICENSE.md).

| Carpeta | Formato | Plataforma |
|---|---|---|
| [sigma](sigma/) | Sigma (YAML) | Independiente: se convierte a cualquier SIEM con pySigma |
| [kql](kql/) | Kusto Query Language | Microsoft Sentinel, Defender XDR |
| [xql](xql/) | XQL | Cortex XDR / XSIAM |
| [yara](yara/) | YARA | Archivos y memoria |
| [suricata](suricata/) | Reglas Suricata | IDS/IPS de red |

## Ciclo de vida

```
experimental  →  test  →  stable
   (nueva)      (probada en   (usada por 2+ organizaciones
                 laboratorio)   sin falsos positivos relevantes)
```

## Requisitos de toda detección
- Técnica **MITRE ATT&CK** asociada.
- **Autor/a, fecha** y **referencias**.
- **Falsos positivos** conocidos.
- **Origen de datos** necesario (qué log o telemetría).
- Probada: indica plataforma y versión.

## Prioridad: Sigma primero
Si la lógica se puede expresar en Sigma, escríbela en Sigma y, si quieres, agrega la versión KQL o XQL. Así una misma detección sirve a toda la comunidad, sin importar su SIEM.

```bash
pip install sigma-cli
sigma plugin install microsoft365defender   # o splunk, elasticsearch, ...
sigma convert -t microsoft365defender sigma/windows/<regla>.yml
```

Los PR que tocan `sigma/` o `yara/` se validan automáticamente.
