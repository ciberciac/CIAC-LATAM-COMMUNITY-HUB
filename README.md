<div align="center">

# CIAC LATAM Community Hub

**Conocimiento abierto de ciberseguridad hecho por y para Latinoamérica**

[Web](https://landing.ciac.lat) · [Telegram](https://t.me/ciberciac) · [WhatsApp](https://whatsapp.com/channel/0029Va6OjVKA89Mj7w8xde06) · [Cómo contribuir](CONTRIBUTING.md)

![TLP:CLEAR](https://img.shields.io/badge/TLP-CLEAR-white?style=flat-square)
![Licencia contenido](https://img.shields.io/badge/contenido-CC%20BY%204.0-blue?style=flat-square)
![Licencia reglas](https://img.shields.io/badge/reglas-DRL%201.1-green?style=flat-square)

</div>

🇪🇸 Buenas prácticas, inteligencia de amenazas, detecciones, playbooks de respuesta a incidentes y laboratorios DFIR, adaptados a la realidad de las organizaciones de la región.
🇧🇷 Conteúdo aberto de cibersegurança para a América Latina. Contribuições em português são bem-vindas.
🇬🇧 Open cybersecurity knowledge for Latin America. Contributions in English are welcome.

## Contenido

| Sección | Qué encontrarás | Marcos de referencia |
|---|---|---|
| [best-practices](best-practices/) | Guías de bastionado, configuración segura y desarrollo seguro con IA | CIS Benchmarks, CIS Controls v8.1, NIST CSF 2.0, OWASP Top 10 for LLM, NIST AI RMF |
| [threat-intelligence](threat-intelligence/) | Análisis de hipótesis, mapeo ATT&CK, análisis de IOCs y perfiles de amenazas | ACH, MITRE ATT&CK, Modelo de Diamante, escala Almirantazgo |
| [detection-as-code](detection-as-code/) | Reglas y consultas listas para usar y adaptar | Sigma, KQL, XQL, YARA, Suricata |
| [incident-response](incident-response/) | Playbooks paso a paso para los incidentes más frecuentes en la región | NIST SP 800-61r3, ISO/IEC 27035 |
| [dfir-labs](dfir-labs/) | Laboratorios prácticos de análisis forense y respuesta | Escenarios reproducibles con datos sintéticos |
| [templates](templates/) | Plantillas de informes y evaluaciones | ISO/IEC 27005, NIST SP 800-30 |

## ¿Por qué un hub para LATAM?

La mayoría del material de referencia está en inglés y pensado para organizaciones con presupuestos y equipos grandes. Este repositorio busca:

- Contenido **en español y portugués**, con terminología consistente.
- Ejemplos basados en **amenazas que sí se ven en la región**: troyanos bancarios, phishing que suplanta entidades locales, ransomware contra gobierno, salud y manufactura, fraude BEC en comercio exterior.
- Recomendaciones **aplicables por equipos pequeños**, indicando qué es imprescindible y qué es deseable.
- Referencias a **marcos internacionales**, para que todo sea comparable y auditable.

## Cómo participar

1. Lee la [guía de contribución](CONTRIBUTING.md).
2. Busca issues con la etiqueta `good first issue` o `ayuda-buscada`.
3. Propón ideas y nuevas iniciativas en **Discussions**.
4. Abre un Pull Request.

Toda persona que contribuye aparece en [CONTRIBUTORS.md](CONTRIBUTORS.md).

## Licencias

| Contenido | Licencia |
|---|---|
| Todo el repositorio, salvo lo indicado abajo | [CC BY 4.0](LICENSE): uso libre, incluso comercial, citando a *CIAC LATAM Community Hub* |
| `detection-as-code/` | [Detection Rule License 1.1](detection-as-code/LICENSE.md) |

## Aviso

Contenido con fines defensivos y educativos, publicado como **TLP:CLEAR**. Prueba siempre los cambios y las detecciones en un entorno controlado antes de aplicarlos en producción.
