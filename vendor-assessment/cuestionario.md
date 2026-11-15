# Cuestionario de evaluación de proveedores de SOC y MSSP

48 preguntas en 10 secciones. ⛔ = **excluyente**: un puntaje menor que 2 descarta al proveedor, sin importar el puntaje total.

Califica cada respuesta con la escala 0–4 del [README](README.md#escala). **Sin evidencia, el puntaje máximo es 1.**

Para evaluar y comparar, usa la plantilla Excel [`plantillas/evaluacion-proveedores-ciac.xlsx`](plantillas/evaluacion-proveedores-ciac.xlsx). La versión para enviar al proveedor está en [`plantillas/cuestionario.csv`](plantillas/cuestionario.csv).

## A. Gobierno, certificaciones y cumplimiento · peso 10 %

| ID | Pregunta | Evidencia a solicitar | Señal de alerta | Referencia |
|---|---|---|---|---|
| PRV-A01 | ⛔ ¿Cuenta con un sistema de gestión de seguridad certificado o auditado por un tercero independiente? | Certificado ISO/IEC 27001 con alcance que incluya el SOC, o informe SOC 2 Tipo II reciente | El alcance del certificado no incluye el servicio de SOC; informe con más de 12 meses | ISO/IEC 27001 · AICPA SOC 2 |
| PRV-A02 | ¿El SOC tiene una evaluación de madurez reciente con un modelo reconocido? | Resultado de SOC-CMM (autoevaluación o certificación) u otro modelo con fecha y alcance | Afirma ser 'nivel 4' sin evidencia ni evaluador | SOC-CMM |
| PRV-A03 | ¿Tiene acreditaciones específicas de SOC, respuesta a incidentes o inteligencia? | Acreditaciones vigentes (p. ej. CREST SOC/CSIR, membresía FIRST, certificación SIM3 vía Trusted Introducer) | Logos de alianzas comerciales presentados como acreditaciones | CREST · FIRST · SIM3 |
| PRV-A04 | ¿Ha participado en pruebas independientes de detección de servicios gestionados? | Resultados publicados (p. ej. MITRE ATT&CK Evaluations, edición Managed Services) y su interpretación | Cita solo resultados del fabricante de su herramienta, no del servicio | MITRE ATT&CK Evaluations |
| PRV-A05 | ⛔ ¿Conoce y cumple la regulación sectorial del cliente (tercerización, ciberseguridad, nube) en su país? | Matriz de cumplimiento regulatorio y casos de clientes del mismo sector | Respuesta genérica sin mencionar normas locales | Regulador sectorial del país |
| PRV-A06 | ⛔ ¿Acepta auditorías del cliente o de su regulador sobre el servicio? | Cláusula de derecho de auditoría en el contrato modelo | Rechaza auditorías o solo ofrece un resumen comercial | FFIEC Apéndice D (MSSP) · NIST CSF 2.0 GV.SC |

## B. Personas y equipo · peso 10 %

| ID | Pregunta | Evidencia a solicitar | Señal de alerta | Referencia |
|---|---|---|---|---|
| PRV-B01 | ⛔ ¿El monitoreo es 24/7/365 con personal propio y analistas en español? | Cuadro de turnos, ubicación de los centros, idioma de atención | Fuera de horario solo hay alertas automáticas o personal de guardia de otro servicio | SOC-CMM · Personas |
| PRV-B02 | ¿Cuántos analistas por nivel atienden el servicio y cuál es la relación analista/clientes? | Organigrama del servicio y métricas de carga | No responde o la cifra cambia según quién pregunte | SOC-CMM · Personas |
| PRV-B03 | ¿Qué perfiles, certificaciones y formación continua tiene el equipo? | Matriz de competencias y plan de formación anual | Equipo concentrado en analistas junior sin supervisión senior | SOC-CMM · Personas |
| PRV-B04 | ¿Cuál es la rotación anual del personal del SOC y cómo asegura la continuidad del conocimiento? | Indicador de rotación y procedimientos de traspaso | Rotación alta sin documentación del entorno del cliente | SOC-CMM · Personas |
| PRV-B05 | ¿Asigna un responsable de servicio (gestor técnico) y un contacto de escalamiento ejecutivo? | Nombres y roles en la propuesta | Único punto de contacto es comercial | SOC-CMM · Servicios |

## C. Servicios y alcance · peso 5 %

| ID | Pregunta | Evidencia a solicitar | Señal de alerta | Referencia |
|---|---|---|---|---|
| PRV-C01 | ⛔ ¿Qué servicios incluye exactamente y cuáles son opcionales o con costo adicional? | Catálogo de servicios con descripción, límites y precios | 'Respuesta incluida' sin definir qué acciones cubre | FIRST CSIRT Services Framework · SOC-CMM · Servicios |
| PRV-C02 | ⛔ ¿Cómo se reparten responsabilidades entre el proveedor y el cliente (modelo RACI)? | Matriz RACI por proceso | Responsabilidades ambiguas en detección, contención o recuperación | SOC-CMM |
| PRV-C03 | ¿Ofrece modelos gestionado, co-gestionado e híbrido con el equipo interno? | Descripción de modelos y ejemplos | Solo un modelo rígido que no se adapta al equipo interno | SOC-CMM |

## D. Visibilidad y detección · peso 20 %

| ID | Pregunta | Evidencia a solicitar | Señal de alerta | Referencia |
|---|---|---|---|---|
| PRV-D01 | ⛔ ¿Qué fuentes de registro integrará y cuáles prioriza? | Lista de fuentes por fase: EDR, identidad, controladores de dominio, correo, red, nube, aplicaciones críticas | Integra solo el firewall o cobra cada fuente por separado sin plan | CISA Priority Logs for SIEM Ingestion |
| PRV-D02 | ⛔ ¿Cuál es la cobertura de detección medida contra MITRE ATT&CK para los actores de su sector y región? | Capa de ATT&CK Navigator con casos de uso y su estado | Cuenta 'reglas' en vez de mostrar cobertura de técnicas | MITRE ATT&CK · SOC-CMM |
| PRV-D03 | ¿Cómo se gestiona el ciclo de vida de los casos de uso (alta, ajuste, retiro) y con qué frecuencia? | Procedimiento y registro de cambios | Reglas genéricas del fabricante sin ajuste al entorno | MaGMa · SOC-CMM · Procesos |
| PRV-D04 | ¿Puede crear detecciones a medida para el entorno y las amenazas del cliente? | Ejemplos anonimizados y plazo típico de implementación | Solo usa contenido del fabricante | Detection as Code |
| PRV-D05 | ¿Cómo gestiona los falsos positivos y cuál es su tasa actual? | Métrica de falsos positivos y proceso de ajuste | No mide falsos positivos o los traslada al cliente | SOC-CMM · Procesos |
| PRV-D06 | ¿Detecta abuso de herramientas legítimas (living off the land) y amenazas en la nube y en identidad? | Casos de uso específicos y ejemplos | Detección basada solo en firmas e IOCs | CISA Best Practices for Event Logging and Threat Detection |
| PRV-D07 | ¿Acepta una prueba de concepto con emulación de técnicas antes de firmar? | Plan de prueba de concepto acordado | Rechaza cualquier prueba técnica previa | Ver plantilla de prueba de concepto |

## E. Respuesta y contención · peso 15 %

| ID | Pregunta | Evidencia a solicitar | Señal de alerta | Referencia |
|---|---|---|---|---|
| PRV-E01 | ⛔ ¿Qué acciones de contención puede ejecutar sin pedir autorización (aislar equipo, bloquear cuenta o IP)? | Matriz de acciones preautorizadas configurable por el cliente | Solo notifica; toda acción depende del cliente | NIST SP 800-61r3 |
| PRV-E02 | ¿Tiene playbooks por tipo de incidente (ransomware, BEC, fuga de datos) y los adapta al cliente? | Playbooks de ejemplo y proceso de adaptación | Playbooks genéricos sin contactos ni particularidades del cliente | NIST SP 800-61r3 · CISA Playbooks |
| PRV-E03 | ⛔ ¿Incluye respuesta a incidentes y análisis forense, o requiere un contrato aparte? | Alcance, horas incluidas y tiempos de activación | Respuesta 'incluida' que en la práctica es solo asesoría por correo | SIM3 · NIST SP 800-61r3 |
| PRV-E04 | ¿Preserva evidencia con cadena de custodia apta para procesos legales? | Procedimiento forense | Sin procedimiento de cadena de custodia | ISO/IEC 27037 · NIST SP 800-86 |
| PRV-E05 | ¿Coordina con el CSIRT nacional, autoridades y aseguradoras cuando el cliente lo requiere? | Experiencia y contactos | Desconoce a los actores locales de respuesta | SIM3 · H-7 |

## F. Inteligencia y cacería de amenazas · peso 10 %

| ID | Pregunta | Evidencia a solicitar | Señal de alerta | Referencia |
|---|---|---|---|---|
| PRV-F01 | ¿Usa inteligencia de amenazas regional (actores, campañas y fraude en Latinoamérica)? | Fuentes, ejemplos de informes y cómo se convierten en detecciones | Solo feeds globales sin contexto regional | CTI-CMM |
| PRV-F02 | ¿Realiza cacería de amenazas proactiva con metodología y frecuencia definidas? | Metodología (TaHiTI, PEAK u otra), frecuencia e informes de ejemplo | 'Threat hunting' que en realidad es búsqueda automática de IOCs | NIST SP 800-53 RA-10 · TaHiTI |
| PRV-F03 | ¿Comparte indicadores y hallazgos con el cliente en formatos estándar y bajo TLP? | Ejemplos de entregables (STIX, CSV, informes) | No entrega indicadores o los entrega en formatos propietarios | NIST SP 800-150 · FIRST TLP 2.0 |
| PRV-F04 | ¿Monitorea exposición externa, filtraciones y suplantación de marca del cliente? | Alcance del servicio y ejemplos | No contemplado o con costo no informado | CTI-CMM |

## G. Datos, privacidad y regulación · peso 10 %

| ID | Pregunta | Evidencia a solicitar | Señal de alerta | Referencia |
|---|---|---|---|---|
| PRV-G01 | ⛔ ¿En qué países se almacenan y procesan los datos y registros del cliente? | Ubicaciones de centros de datos, nube y analistas | No puede precisar ubicaciones o cambia de proveedor de nube sin aviso | Leyes de protección de datos del país |
| PRV-G02 | ⛔ ¿Cómo cumple la ley de protección de datos del país del cliente, incluidas las transferencias internacionales? | Acuerdo de tratamiento de datos y mecanismo de transferencia | Sin acuerdo de tratamiento de datos | Leyes de protección de datos del país |
| PRV-G03 | ⛔ ¿Quién accede a los datos del cliente, cómo se controla y se registra ese acceso? | Política de acceso, MFA, registros de acceso disponibles para el cliente | Cuentas compartidas o acceso permanente sin registro | NIST SP 800-53 AC · CISA guía para MSP y clientes |
| PRV-G04 | ¿Cuánto tiempo retiene los registros y qué pasa con ellos al terminar el contrato? | Política de retención y de eliminación certificada | Retención indefinida o sin certificado de eliminación | ISO/IEC 27001 |
| PRV-G05 | ⛔ ¿Cómo y en qué plazo notifica al cliente un incidente que afecte al propio proveedor? | Cláusula de notificación con plazo | Sin compromiso de notificación de incidentes propios | NIST CSF 2.0 GV.SC · CISA CPG 2.0 |

## H. Tecnología e integración · peso 5 %

| ID | Pregunta | Evidencia a solicitar | Señal de alerta | Referencia |
|---|---|---|---|---|
| PRV-H01 | ¿Qué plataformas usa (SIEM, EDR/XDR, SOAR) y quién es dueño de las licencias? | Arquitectura y modelo de licenciamiento | Licencias a nombre del proveedor que no se pueden transferir | SOC-CMM · Tecnología |
| PRV-H02 | ¿Se integra con las herramientas existentes del cliente sin obligar a reemplazarlas? | Lista de integraciones soportadas | Exige cambiar toda la tecnología del cliente | SOC-CMM · Tecnología |
| PRV-H03 | ¿El cliente tiene acceso de lectura a la consola, los registros y las reglas? | Demostración del portal o consola | Caja negra: el cliente solo ve informes | CISA SIEM/SOAR guidance |
| PRV-H04 | ⛔ ¿Cómo protege su propia infraestructura y el acceso remoto a los entornos de clientes? | Arquitectura de acceso, MFA, segmentación por cliente | Mismo acceso o credenciales para varios clientes | CISA/Five Eyes · guía de protección de MSP y sus clientes |

## I. Niveles de servicio, métricas y reportes · peso 10 %

| ID | Pregunta | Evidencia a solicitar | Señal de alerta | Referencia |
|---|---|---|---|---|
| PRV-I01 | ⛔ ¿Qué tiempos comprometen por severidad (reconocimiento, notificación, inicio de contención)? | SLA con definiciones y penalizaciones | SLA solo de 'disponibilidad de la plataforma' | Ver plantilla de SLA |
| PRV-I02 | ¿Qué métricas reporta y con qué frecuencia? | Informe de ejemplo: alertas, incidentes, tiempos, falsos positivos, cobertura | Informes con volumen de eventos sin análisis | SOC-CMM · Procesos |
| PRV-I03 | ¿Hay reuniones periódicas de servicio y un plan de mejora acordado? | Calendario de revisiones y ejemplo de acta | Contacto solo cuando hay incidentes o renovación | SOC-CMM · Servicios |
| PRV-I04 | ¿Entrega informes ejecutivos comprensibles para la dirección? | Informe ejecutivo de ejemplo | Solo informes técnicos | NIST CSF 2.0 GV.OV |

## J. Continuidad, terceros y salida · peso 5 %

| ID | Pregunta | Evidencia a solicitar | Señal de alerta | Referencia |
|---|---|---|---|---|
| PRV-J01 | ⛔ ¿Usa subcontratistas para el servicio? ¿Cuáles, dónde y con qué controles? | Lista de subcontratistas y cláusulas aplicables | Subcontrata el monitoreo fuera de horario sin informarlo | FFIEC Apéndice D (MSSP) · NIST SP 800-161r1 |
| PRV-J02 | ¿Tiene plan de continuidad del propio SOC (sede alterna, trabajo remoto, caída de la plataforma)? | Plan de continuidad y última prueba | Sin pruebas de continuidad | ISO 22301 · NIST SP 800-34 |
| PRV-J03 | ⛔ ¿Qué incluye la salida del servicio: devolución de registros, reglas, casos de uso y documentación? | Cláusula y plan de salida | Reglas y casos de uso propiedad exclusiva del proveedor sin entrega | Buenas prácticas de tercerización |
| PRV-J04 | ¿Tiene seguro de responsabilidad cibernética y profesional? | Póliza vigente con montos | Sin seguro | Gestión de riesgo de terceros |
| PRV-J05 | ¿Puede dar referencias de clientes del mismo sector y país? | Dos o tres contactos de referencia | Ninguna referencia verificable en la región | Gestión de riesgo de terceros |
