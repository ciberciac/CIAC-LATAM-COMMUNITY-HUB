# Mapeo ATT&CK – <Amenaza o campaña>

| | |
|---|---|
| **Versión ATT&CK** | vXX |
| **Países / sectores** | CO, EC · financiero |
| **Autor/a · fecha** | @usuario · AAAA-MM-DD |

| Táctica | Técnica | Evidencia observada | Fuente | Detección |
|---|---|---|---|---|
| Acceso inicial | T1566.001 Spearphishing Attachment | Correo que suplanta una entidad tributaria con adjunto comprimido | [1] | — |
| Ejecución | T1204.002 Malicious File | El usuario ejecuta un script dentro del adjunto | [1] | — |
| Comando y control | T1105 Ingress Tool Transfer | Descarga de un RAT desde un servicio de alojamiento público | [1] | [sigma/...](../../../detection-as-code/sigma/) |

## Fuentes
1. ...
