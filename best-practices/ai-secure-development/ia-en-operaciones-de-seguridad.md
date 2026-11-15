# IA en operaciones de seguridad (SOC, CTI, DFIR)

| | |
|---|---|
| **Nivel** | 🟡 intermedio |
| **Aplica a** | Analistas que usan LLM para triage, análisis de malware, redacción de informes, consultas de SIEM o inteligencia |
| **Referencias** | NIST AI RMF · NIST AI 600-1 · TLP 2.0 |

## Usos que aportan valor
- Resumir alertas, logs o informes largos.
- Proponer borradores de consultas (KQL, XQL, SPL) y reglas Sigma o YARA.
- Explicar scripts ofuscados o comandos desconocidos.
- Redactar borradores de informes y comunicaciones.
- Traducir informes de amenazas al español o portugués.

## Controles

### 1. Clasifica antes de pegar · 🔴
Aplica **TLP** también a la IA: lo que es TLP:AMBER o TLP:RED, datos de clientes, evidencias forenses o IOCs de un caso en curso **no van a servicios públicos**. Usa modelos locales o planes empresariales con garantías contractuales para ese material.

### 2. Anonimiza · 🔴
Reemplaza nombres de clientes, usuarios, hostnames, IPs internas y dominios corporativos por marcadores antes de enviar logs o evidencias.

### 3. Nunca subas muestras de malware a un servicio de IA general · 🔴
Para análisis usa sandboxes y herramientas especializadas. Si pides ayuda con un fragmento, que sea código desactivado y sin datos de la víctima.

### 4. El modelo propone, el analista decide · 🔴
- Las consultas y reglas generadas se **prueban** antes de desplegarse.
- Los IOCs, técnicas ATT&CK o atribuciones que sugiera el modelo se verifican en fuentes primarias. Los modelos inventan hashes, CVE y referencias con total seguridad.
- Las conclusiones de un informe las firma una persona.

### 5. Cuidado con contenido malicioso diseñado para la IA · 🟡
Correos de phishing, documentos y páginas analizadas pueden incluir instrucciones ocultas para el modelo ("este archivo es benigno"). No delegues en la IA la decisión de si algo es malicioso.

### 6. Documenta el uso · 🟢
En informes y entregables, indica cuándo se usó IA y para qué, sobre todo si van a clientes o reguladores.

## Lista de verificación
- [ ] El material es TLP:CLEAR o uso una herramienta aprobada para su clasificación.
- [ ] Datos anonimizados.
- [ ] Salidas verificadas en fuentes primarias.
- [ ] Reglas y consultas probadas antes de producción.
- [ ] Uso de IA documentado en el entregable.
