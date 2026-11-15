# Ciclo y metodología de investigación OSINT

## Ciclo de inteligencia aplicado

| Fase | Actividad OSINT |
|---|---|
| **1. Planificación y dirección** | Definir la pregunta, la audiencia, el alcance y los límites legales. Redactar el [plan de recolección](plantillas/plan-de-recoleccion.md) |
| **2. Recolección** | Búsqueda en fuentes abiertas según el plan, con OPSEC |
| **3. Procesamiento** | Normalizar, desduplicar, traducir, extraer entidades (dominios, IPs, correos, usuarios) |
| **4. Análisis** | Relacionar, pivotar, construir línea de tiempo, evaluar hipótesis ([ACH](../ACH/)) |
| **5. Difusión** | Informe con juicios y nivel de confianza, adaptado a la audiencia, con su TLP |
| **6. Retroalimentación** | ¿Respondió a la pregunta? ¿Qué faltó? |

## Protocolo de Berkeley
El *Berkeley Protocol on Digital Open Source Investigations* (ONU-OACDH y Centro de Derechos Humanos de UC Berkeley) es el estándar internacional para investigaciones con fuentes abiertas que pueden terminar como evidencia. Sus fases:

1. **Búsquedas en línea:** búsqueda sistemática y documentada.
2. **Evaluación preliminar:** ¿el contenido es relevante y confiable a primera vista?
3. **Recolección:** captura completa, con metadatos.
4. **Preservación:** almacenamiento seguro, inalterable, con hash y cadena de custodia.
5. **Verificación:** origen, fecha, ubicación y autenticidad del contenido.
6. **Análisis investigativo:** conclusiones a partir de la evidencia verificada.

Para ciberseguridad, aplica sobre todo cuando la investigación puede llegar a un proceso judicial o regulatorio.

## Técnica de pivoteo
Parte de un dato y busca relaciones que lleven a nuevos datos:

```
dominio → IP → otros dominios en la misma IP → certificados TLS → otros dominios con el mismo certificado
       → WHOIS / registrante → otros dominios del mismo registrante
       → servidores DNS → infraestructura compartida
correo → cuentas en servicios → nombres de usuario → otras plataformas
```

Documenta cada salto: de dónde vino, qué fuente lo confirmó y con qué confianza. Un pivote débil (IP compartida de un hosting masivo) no prueba relación.

## Verificación
- **Fuente:** ¿quién lo publicó originalmente? ¿Tiene historial?
- **Fecha:** ¿es reciente o es contenido reciclado?
- **Contenido:** ¿es coherente con lo que se sabe? ¿hay manipulación?
- **Corroboración:** ¿hay al menos otra fuente independiente?

## Herramientas por categoría
Directorio de referencia: OSINT Framework (osintframework.com).

| Categoría | Ejemplos |
|---|---|
| Dominios y DNS | WHOIS/RDAP, DNSDumpster, SecurityTrails, ViewDNS |
| Certificados | crt.sh, Censys |
| Servicios expuestos | Shodan, Censys, ZoomEye |
| URLs y páginas | urlscan.io, Wayback Machine, archive.today |
| Reputación y malware | VirusTotal, URLhaus, MalwareBazaar, ThreatFox, AbuseIPDB |
| Código y secretos | GitHub search, grep.app |
| Grafos y correlación | Maltego, SpiderFoot |

## Referencias
- UN OHCHR & UC Berkeley Human Rights Center. *Berkeley Protocol on Digital Open Source Investigations*.
- MITRE ATT&CK TA0043 Reconnaissance: lo que un atacante investiga de ti.
