# PEAK · Preparar, Ejecutar y Actuar con Conocimiento

| | |
|---|---|
| **Nombre original** | *Prepare, Execute, Act with Knowledge* |
| **Autoría** | Splunk SURGe (David Bianco y equipo) |
| **Año** | 2023 |
| **Antecedentes** | Evoluciona el ciclo de cacería de Sqrrl (2015) y el Hunting Maturity Model |

## Tres tipos de cacería

| Tipo | Cómo funciona | Ejemplo |
|---|---|---|
| **Por hipótesis** | Se formula una suposición comprobable sobre actividad del atacante | "Hay cuentas de servicio iniciando sesión de forma interactiva" |
| **Por línea base** (análisis exploratorio de datos) | Se caracteriza lo normal y se buscan desviaciones | Distribución de procesos hijos de `w3wp.exe` en servidores web |
| **Asistida por modelos (M-ATH)** | Se usan modelos estadísticos o de aprendizaje automático para encontrar candidatos | Clasificador de dominios generados algorítmicamente (DGA) |

## Tres fases

1. **Preparar:** elegir el tema, investigar (inteligencia, ATT&CK), formular la hipótesis o el objetivo, definir alcance y datos.
2. **Ejecutar:** recolectar y analizar los datos; refinar; escalar a respuesta a incidentes si aparece algo crítico.
3. **Actuar:** preservar la cacería (consultas y datos), documentar, **crear detecciones** y comunicar los resultados.

El **conocimiento** (del negocio, del entorno, de la amenaza y de cacerías anteriores) atraviesa las tres fases: de ahí el *with Knowledge*.

## Cuándo usarlo
- Equipos que quieren ir más allá de las hipótesis y aprovechar el análisis de datos.
- Entornos con buena telemetría centralizada.
- Combinado con TaHiTI: TaHiTI organiza el flujo con la inteligencia; PEAK aporta los tipos de análisis.

## Referencias
- Splunk SURGe. *The PEAK Threat Hunting Framework* (2023).
