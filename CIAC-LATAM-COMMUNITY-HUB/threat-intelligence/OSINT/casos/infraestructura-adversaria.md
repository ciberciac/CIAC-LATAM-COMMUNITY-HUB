# Metodología · Infraestructura adversaria

Investigar dominios, IPs y certificados de una campaña para encontrar más infraestructura, entender al actor y generar detecciones.

## Punto de partida
Un indicador de un incidente, de un correo de phishing o de un informe público.

## Pasos
1. **Registro:** RDAP/WHOIS, fecha de creación, registrador, servidores DNS. Dominios recién creados son una señal.
2. **Resolución histórica:** DNS pasivo para ver a qué IPs apuntó y qué otros dominios comparten esas IPs.
3. **Certificados:** crt.sh y Censys para encontrar otros dominios con el mismo certificado, emisor o patrón de nombres.
4. **Servicios y huellas:** puertos, *banners*, títulos HTML, *favicon hash*, huellas TLS (JARM/JA4) para encontrar servidores con la misma configuración.
5. **Contenido:** urlscan.io y Wayback Machine para ver el sitio sin visitarlo; recursos compartidos entre sitios (kits de phishing).
6. **Reputación y malware:** VirusTotal, URLhaus, ThreatFox: muestras que contactan a la infraestructura.
7. **Agrupar y evaluar:** qué relaciones son fuertes (mismo certificado único) y cuáles débiles (hosting compartido).

## Resultado
- Lista de infraestructura relacionada con su nivel de confianza.
- Patrones reutilizables para detectar infraestructura futura (convenciones de nombres, configuraciones).
- Aportes a [`IOC-analysis`](../../IOC-analysis/) y [`threat-profiles`](../../threat-profiles/).

> Recuerda la [OPSEC](../opsec-del-investigador.md): consulta servicios que ya escanearon la infraestructura antes de conectarte directamente.
