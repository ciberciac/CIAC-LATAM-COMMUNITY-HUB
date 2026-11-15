# Análisis de IOCs

Guías y casos de análisis de indicadores de compromiso: cómo validarlos, enriquecerlos, darles contexto y decidir si sirven para bloquear.

## Pirámide del dolor
Prioriza indicadores difíciles de cambiar para el atacante: hashes e IPs se reemplazan en minutos; herramientas y TTPs, no. Un buen análisis siempre conecta el IOC con un comportamiento.

## Flujo de análisis

1. **Validar:** ¿el formato es correcto? ¿no es un servicio legítimo masivo (CDN, nube, acortador)?
2. **Enriquecer:** reputación, WHOIS y registro, DNS pasivo, certificados, geolocalización, relación con otras muestras.
3. **Contextualizar:** campaña, familia, técnica ATT&CK, primera y última vez visto.
4. **Valorar:** confianza, vigencia esperada y riesgo de falso positivo.
5. **Decidir el uso:** bloqueo, detección, solo búsqueda (*hunting*) o solo contexto.

## Fuentes abiertas útiles
VirusTotal · MalwareBazaar · URLhaus · ThreatFox · AbuseIPDB · Shodan · Censys · crt.sh · urlscan.io · AlienVault OTX

## Formato de intercambio
Para compartir indicadores usa [`_plantilla-iocs.csv`](_plantilla-iocs.csv) y documenta el caso con [`_plantilla-analisis.md`](_plantilla-analisis.md).

> En Markdown, desactiva los indicadores (`dominio[.]com`, `hxxps://`). En el CSV van con su valor real.
