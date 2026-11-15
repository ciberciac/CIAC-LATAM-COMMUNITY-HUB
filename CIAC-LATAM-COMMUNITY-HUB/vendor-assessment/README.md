# Evaluación de proveedores de SOC y MSSP

Herramientas para **seleccionar, contratar y supervisar** proveedores de servicios de seguridad gestionados: SOC tercerizado, MSSP, MDR (detección y respuesta gestionadas) o servicios de respuesta a incidentes. Pensado para organizaciones de Latinoamérica de cualquier tamaño, desde la que contrata su primer SOC hasta la entidad regulada que debe justificar la elección ante su supervisor.

## Contenido

| Archivo | Para qué |
|---|---|
| [cuestionario.md](cuestionario.md) | 48 preguntas en 10 secciones, con evidencia a solicitar, señales de alerta y referencias |
| [plantillas/cuestionario.csv](plantillas/cuestionario.csv) | Versión para enviar al proveedor y calificar |
| [plantillas/matriz-comparativa.csv](plantillas/matriz-comparativa.csv) y [pesos.csv](plantillas/pesos.csv) | Comparación ponderada de varias ofertas |
| [plantillas/prueba-de-concepto.md](plantillas/prueba-de-concepto.md) | Plan para probar la detección antes de firmar |
| [plantillas/acuerdo-de-nivel-de-servicio.md](plantillas/acuerdo-de-nivel-de-servicio.md) | Estructura de SLA con tiempos por severidad |
| [plantillas/clausulas-contractuales.md](plantillas/clausulas-contractuales.md) | Lista de verificación de cláusulas clave |
| [plantillas/revision-periodica.md](plantillas/revision-periodica.md) | Revisión trimestral y anual del servicio |
| [scripts/comparar_proveedores.py](scripts/comparar_proveedores.py) | Calcula el ranking ponderado y marca descalificaciones |

## Proceso

```
1. Requisitos  →  2. Preselección  →  3. Cuestionario  →  4. Verificación  →  5. Prueba de   →  6. Decisión  →  7. Contrato  →  8. Supervisión
   internos         (3–5 ofertas)      con evidencias      de evidencias      concepto           ponderada        y SLA          periódica
```

1. **Requisitos internos.** Antes de hablar con proveedores, define qué necesitas: activos y fuentes a monitorear, horario, qué acciones puede tomar el proveedor, regulación aplicable, presupuesto. Usa la [evaluación de madurez](../maturity-assessment/) para saber qué capacidades tienes y cuáles necesitas comprar.
2. **Preselección.** Descarta a quien no cumpla los criterios ⛔ básicos (cobertura 24/7, protección de datos, regulación sectorial).
3. **Cuestionario.** Envía la misma versión a todos y exige evidencia, no solo respuestas.
4. **Verificación.** Revisa certificados, pide demostraciones de la consola y llama a las referencias.
5. **Prueba de concepto.** Para contratos relevantes, mide la detección y el escalamiento con técnicas emuladas.
6. **Decisión.** Ajusta los pesos a tu realidad y calcula el ranking con la matriz.
7. **Contrato y SLA.** Lleva al contrato lo que el proveedor prometió en el cuestionario.
8. **Supervisión.** El servicio se gestiona, no solo se compra: revisión trimestral y reevaluación anual.

## Escala

Igual que la [evaluación de madurez](../maturity-assessment/escala-y-metodo.md):

| Puntaje | Significado para un proveedor |
|---|---|
| **0** | No lo ofrece o no responde |
| **1** | Lo afirma sin evidencia, o lo hace de forma informal |
| **2** | Lo hace de forma consistente y muestra documentación interna |
| **3** | Lo tiene formalizado, medido y lo demuestra con evidencia o en la prueba de concepto |
| **4** | Además lo audita un tercero o lo mejora de forma demostrable |

## Pesos sugeridos

| Sección | Peso |
|---|---|
| A. Gobierno, certificaciones y cumplimiento | 10 % |
| B. Personas y equipo | 10 % |
| C. Servicios y alcance | 5 % |
| D. Visibilidad y detección | 20 % |
| E. Respuesta y contención | 15 % |
| F. Inteligencia y cacería de amenazas | 10 % |
| G. Datos, privacidad y regulación | 10 % |
| H. Tecnología e integración | 5 % |
| I. Niveles de servicio, métricas y reportes | 10 % |
| J. Continuidad, terceros y salida | 5 % |

Ajusta los pesos a tu caso: una entidad financiera puede subir **A** y **G**; una organización sin equipo interno puede subir **E**. Define los pesos **antes** de recibir las ofertas, para que no se acomoden al proveedor preferido.

## Particularidades de la región

- **Idioma y horario:** atención 24/7 en español, en el huso horario del cliente.
- **Regulación local:** normas de protección de datos, reglas de tercerización y ciberseguridad del regulador sectorial (financiero, telecomunicaciones, energía), y obligaciones de notificación con plazos cortos.
- **Ubicación de los datos:** muchas leyes de la región exigen condiciones para transferir datos personales fuera del país.
- **Amenazas regionales:** troyanos bancarios, fraude BEC en comercio exterior, phishing que suplanta entidades locales, ransomware contra gobierno y salud. Pide ejemplos concretos.
- **Mercado:** muchos proveedores revenden la plataforma de un fabricante. Evalúa el **servicio** (personas, procesos, tiempos), no la herramienta.

## Marcos de referencia

| Referencia | Qué aporta |
|---|---|
| **SOC-CMM** | Modelo de madurez de SOC; algunos proveedores tienen certificación |
| **SIM3** y certificación de **Trusted Introducer** | Madurez de equipos de respuesta a incidentes |
| **ISO/IEC 27001** · **SOC 2 Tipo II** | Auditoría independiente de los controles del proveedor |
| **CREST** (SOC, respuesta a incidentes, inteligencia) | Acreditaciones específicas de servicios de seguridad |
| **MITRE ATT&CK Evaluations (Managed Services)** | Prueba pública de detección y reporte con emulación de un actor real |
| **FFIEC**, apéndice de tercerización sobre MSSP | Procedimientos de evaluación de MSSP pensados para el sector financiero |
| **NIST CSF 2.0 (GV.SC)** · **NIST SP 800-161r1** | Gestión de riesgo de la cadena de suministro |
| **CISA CPG 2.0** | Incluye objetivos para gestionar el riesgo de los proveedores de servicios gestionados |
| Guía conjunta de **CISA y agencias aliadas** para proteger a los MSP y sus clientes | Controles que el cliente debe exigir al MSP |
| **Reglamento (UE) 2025/37** · esquema de certificación de ENISA en desarrollo | Futura certificación europea de servicios de seguridad gestionados; referencia a seguir |

> Esta carpeta no reemplaza la revisión legal del contrato ni el proceso de compras de tu organización.
