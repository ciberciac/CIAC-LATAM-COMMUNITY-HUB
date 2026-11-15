# Laboratorios DFIR

Ejercicios prácticos de análisis forense y respuesta a incidentes, reproducibles y con solución.

| Carpeta | Enfoque |
|---|---|
| [windows](windows/) | Registros de eventos, artefactos del sistema, memoria, Active Directory |
| [linux](linux/) | Logs, persistencia, análisis de servidores web comprometidos |
| [api-security](api-security/) | Análisis de logs de API y ataques del OWASP API Security Top 10 |

## Reglas de los laboratorios
- **Datos sintéticos o anonimizados.** Nunca evidencias reales de clientes o empleadores.
- **Sin malware activo.** Se simulan artefactos; si un laboratorio necesita una muestra, se enlaza a su fuente pública y se indica el hash.
- **Reproducible:** el laboratorio indica cómo obtener o generar los datos.
- **Solución separada** en `solucion.md`, para que se pueda practicar sin verla.
- Archivos de más de 20 MB → publicar como *Release* o en almacenamiento externo, con hash SHA-256.

## Estructura de un laboratorio
```
dfir-labs/windows/AAAA-nombre-del-lab/
├── README.md       ← escenario, objetivos, herramientas, preguntas
├── datos/          ← evidencias sintéticas o instrucciones para generarlas
└── solucion.md     ← respuestas y razonamiento
```
Plantilla: [`_plantilla-lab.md`](_plantilla-lab.md)
