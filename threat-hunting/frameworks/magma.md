# MaGMa · Use Case Framework

| | |
|---|---|
| **Nombre** | **Ma**nagement, **G**rowth and **M**etrics & **a**ssessment |
| **Autoría** | FI-ISAC de Países Bajos, basado en el marco de ABN AMRO y aportes de otros bancos |
| **Versión** | 1.0 · noviembre de 2017 |
| **Licencia** | Creative Commons |
| **Documento y herramienta** | https://www.betaalvereniging.nl/en/safety/magma/ |

## Para qué sirve
Un **caso de uso de monitoreo** es la combinación de una amenaza que queremos detectar con la lógica, los datos y la respuesta para hacerlo. Cuando un SOC tiene cientos de reglas, MaGMa ayuda a responder:

- ¿Por qué existe cada regla? ¿Qué riesgo del negocio cubre?
- ¿Qué amenazas **no** estamos cubriendo?
- ¿Qué tan maduro y efectivo es cada caso de uso?
- ¿Cuándo hay que cambiarlo o retirarlo?

Aunque nació en banca, está diseñado para cualquier sector.

## Modelo en capas

| Capa | Pregunta | Contenido |
|---|---|---|
| **Negocio** | ¿Por qué monitoreamos esto? | Impulsores del negocio: riesgos, cumplimiento regulatorio, fraude, continuidad |
| **Amenaza** | ¿Qué queremos detectar? | Casos de uso organizados en tres niveles de detalle: de descriptores de amenaza de alto nivel a casos concretos. Las implementaciones actuales los mapean a técnicas de **MITRE ATT&CK** |
| **Visibilidad** | ¿Cómo lo detectamos? | Fuentes de datos, reglas de detección, procedimientos de respuesta |

La trazabilidad entre capas permite explicar a la dirección qué riesgo cubre cada regla, y al equipo técnico qué datos faltan para cubrir un riesgo.

## Ciclo de vida del caso de uso
1. **Alta:** nace de un impulsor del negocio, de inteligencia, de un incidente o de una **cacería** (TaHiTI).
2. **Cambio:** por cambios en el negocio, en la regulación, en la infraestructura o por razones operativas (falsos positivos, nuevas fuentes).
3. **Baja:** cuando ya no se necesita, se retira de forma ordenada en todas las capas.

## Métricas y madurez
La herramienta MaGMa UCF (hoja de cálculo) permite medir, por caso de uso, su nivel de implementación y efectividad, y agregar los resultados para obtener la **cobertura** por impulsor de negocio o por categoría de amenaza.

## Relación con la cacería
- Antes de cazar, MaGMa muestra qué está **cubierto por detección automática**, para no gastar esfuerzo en lo que ya se detecta.
- Las brechas de cobertura son disparadores naturales de cacerías TaHiTI.
- Una cacería exitosa termina como **nuevo caso de uso** en MaGMa y como regla en [`detection-as-code`](../../detection-as-code/).

## Aplicación en LATAM
- En la capa de negocio incluye la regulación local: protección de datos personales, normas de ciberseguridad del regulador financiero y obligaciones sectoriales de tu país.
- Usa la cobertura por técnica ATT&CK de los actores que atacan tu sector en la región como métrica principal.

## Referencias
- FI-ISAC NL (2017). *MaGMa Use Case Framework*, v1.0, y herramienta MaGMa UCF.
