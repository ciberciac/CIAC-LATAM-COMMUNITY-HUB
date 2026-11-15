# TaHiTI · Targeted Hunting integrating Threat Intelligence

| | |
|---|---|
| **Autoría** | Grupo de trabajo de threat hunting del FI-ISAC de Países Bajos (bancos neerlandeses y FinancialCERT) |
| **Versión** | 1.0 · diciembre de 2018 |
| **Licencia** | Creative Commons |
| **Documento oficial** | https://www.betaalvereniging.nl/en/safety/tahiti/ |

## Idea central
Cacería **dirigida** (siempre con una hipótesis y un objetivo claro) que **integra la inteligencia de amenazas** en tres momentos:

1. **Como punto de partida:** un informe sobre un actor que ataca tu sector y región dispara la cacería.
2. **Para contextualizar y guiar** la cacería: cuando aparece una técnica, la inteligencia ayuda a pivotar hacia técnicas relacionadas (ATT&CK, Modelo de Diamante).
3. **Como resultado:** la cacería genera nueva inteligencia que se comparte con la comunidad.

TaHiTI define la cacería como la búsqueda proactiva de actividad maliciosa, actual o histórica, que **evadió las defensas existentes**, y asume que el monitoreo de seguridad funciona correctamente. Se enfoca en la parte alta de la pirámide del dolor, sobre todo en TTP.

## Proceso: 3 fases

```
 INICIAR                       CAZAR                               FINALIZAR
 ┌───────────┐  ┌──────────┐   ┌──────────────┐  ┌──────────┐      ┌────────────┐  ┌──────────┐
 │ Disparador│→ │ Resumen  │ → │Definir/Refinar│⇄│ Ejecutar │  →   │ Documentar │→ │ Traspasar│
 └───────────┘  │ (backlog)│   └──────────────┘  └──────────┘      └────────────┘  └──────────┘
                └──────────┘          ↑ inconcluso ┘
```

### Fase 1 · Iniciar
- **Disparador:** inteligencia de amenazas, MITRE ATT&CK, incidentes previos, otras cacerías, gestión de vulnerabilidades, casos de uso de monitoreo, peticiones del negocio.
- **Resumen (abstract):** descripción breve de la investigación. No necesita todos los detalles.
- **Backlog:** el resumen se guarda en una lista priorizada. Basta un tablero (Jira, Planner, GitHub Projects) que permita elegir la próxima cacería más relevante.

### Fase 2 · Cazar
- **Definir / refinar:** el resumen se convierte en investigación. Se agregan fuentes de datos, técnicas de análisis, alcance y, sobre todo, la **hipótesis**. Una hipótesis mal definida lleva a resultados nulos o, peor, a conclusiones equivocadas.
- **Ejecutar:** se obtienen y analizan los datos (consultas, agrupaciones, estadística, aprendizaje automático). Es iterativo: si aparecen omisiones, se vuelve a refinar.
- **Validar la hipótesis:**
  - ✅ **Probada:** se encontró actividad maliciosa → se inicia respuesta a incidentes.
  - ❌ **Refutada:** no se encontró actividad maliciosa.
  - ❔ **No concluyente:** se ajustan parámetros y se repite.
  - ⚠️ **Fallida:** los datos necesarios no existen. Igual deja lecciones (brecha de visibilidad).

### Fase 3 · Finalizar
- **Documentar:** resultados, conclusiones, recomendaciones (prevención, registro, casos de uso, procesos) y **lecciones aprendidas**.
- **Traspasar** a otros procesos: respuesta a incidentes, monitoreo, inteligencia de amenazas, gestión de vulnerabilidades.

## Métricas sugeridas
Orientadas al **valor**, no solo al volumen:
- Tiempo de permanencia del atacante en los compromisos hallados.
- Incidentes iniciados a partir de cacerías.
- Casos de uso de monitoreo creados o actualizados.
- Inteligencia nueva generada.
- Recomendaciones de prevención emitidas.
- Vulnerabilidades o configuraciones inseguras descubiertas.

## Herramienta de apoyo
**MaGMa for threat hunting**: hoja de cálculo para documentar y medir las cacerías. Se integra con el [MaGMa Use Case Framework](magma.md) porque comparten lenguaje con el equipo de monitoreo.

## Aplicación en LATAM
- Usa como disparadores los informes regionales: actores que atacan banca, gobierno o energía en tu país.
- Comparte los TTP descubiertos (anonimizados) en [`threat-intelligence/threat-profiles`](../../threat-intelligence/threat-profiles/): así otra organización de la región puede iniciar su propia cacería.
- Documenta cada cacería con la [plantilla](../hunts/_plantilla-hunt.md), basada en la de TaHiTI.

## Referencias
- FI-ISAC NL (2018). *TaHiTI Threat Hunting Methodology*, v1.0.
