# Evaluación de madurez

Herramientas para medir y mejorar la madurez de las capacidades de ciberseguridad, basadas en modelos internacionales y adaptadas a la realidad de las organizaciones latinoamericanas: equipos pequeños, presupuestos limitados y regulación en evolución.

## Dominios

| Dominio | Modelo de referencia principal | Evaluación |
|---|---|---|
| [SOC](soc/) | **SOC-CMM** (Security Operations Center Capability Maturity Model) | 13 criterios |
| [Inteligencia de amenazas](cti/) | **CTI-CMM** (Cyber Threat Intelligence Capability Maturity Model) | 12 criterios |
| [Gestión de vulnerabilidades](vulnerability-management/) | **CIS Control 7**, **NIST SP 800-40r4**, **SSVC** | 11 criterios |
| [Cacería de amenazas](threat-hunting/) | **Hunting Maturity Model**, **TaHiTI**, **PEAK** | 10 criterios |
| [Respuesta a incidentes](incident-response/) | **SIM3** de la Open CSIRT Foundation, **NIST SP 800-61r3** | 13 criterios |
| [Comunicaciones](communications/) | **SIM3** (P-2, H-6), **NIST CSF 2.0** (RS.CO), **ISO 22361** | 12 criterios |

## Cómo usarlo

1. **Lee la [escala y el método](escala-y-metodo.md).** Todos los dominios usan la misma escala de 0 a 4 para poder compararlos.
2. **Copia la [hoja de autoevaluación](plantillas/autoevaluacion.csv)** (se abre en Excel o Google Sheets) y califica cada criterio con evidencia.
3. **Define el nivel objetivo** según el perfil de tu organización (ver abajo). No todo tiene que llegar a 4.
4. **Calcula los resultados** con [`scripts/calcular_madurez.py`](scripts/calcular_madurez.py) o en la hoja de cálculo.
5. **Prioriza las brechas** y arma la [hoja de ruta](plantillas/hoja-de-ruta.md).
6. **Comunica** con el [informe de madurez](plantillas/informe-madurez.md).
7. **Repite** cada 12 meses, o tras un cambio importante o un incidente grave.

## Niveles objetivo sugeridos por perfil

| Perfil | Ejemplo | Objetivo general | Prioridad |
|---|---|---|---|
| **Pequeña** | Pyme, ONG, municipio pequeño; TI de 1 a 3 personas, sin SOC propio | **1–2** | Los criterios marcados 🔴 en cada dominio |
| **Mediana** | Empresa con área de seguridad, SOC tercerizado o propio pequeño | **2–3** | Todos los criterios 🔴 en nivel 3 |
| **Regulada o crítica** | Banca, seguros, energía, telecomunicaciones, salud, gobierno central | **3–4** | Todos los criterios en 3; los regulatorios en 4 |

> Una organización pequeña con un SOC tercerizado también puede usar esta evaluación: califica lo que **exiges y verificas** de tu proveedor. Para seleccionar o supervisar proveedores usa [`vendor-assessment`](../vendor-assessment/).

## Por qué estos modelos

- **SOC-CMM** y **SIM3** son los modelos más usados en el mundo para SOC y equipos de respuesta. SIM3 es la base de la certificación de Trusted Introducer y del enfoque de madurez de ENISA para CSIRT nacionales.
- **CTI-CMM** es un modelo comunitario y neutral respecto a proveedores, inspirado en el C2M2, que mide la inteligencia por el valor que entrega a otras áreas.
- Gestión de vulnerabilidades, cacería y comunicaciones no tienen un modelo único dominante; aquí se combinan las referencias más reconocidas.

Las buenas prácticas de **NIST y CISA** para cerrar las brechas de cada dominio están en [`best-practices/nist-cisa`](../best-practices/nist-cisa/).

Esta evaluación es una **versión simplificada y en español**. Para una evaluación formal o certificación, usa las herramientas oficiales de cada modelo (enlaces en cada dominio).
