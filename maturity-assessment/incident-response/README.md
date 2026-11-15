# Madurez · Respuesta a Incidentes

**Modelo de referencia:** SIM3 (Open CSIRT Foundation) · NIST SP 800-61r3

Basado en **SIM3** de la Open CSIRT Foundation, que evalúa los equipos de respuesta en cuatro cuadrantes: Organización (O), Humano (H), Herramientas (T) y Procesos (P). SIM3 v1 tiene 44 parámetros y la versión v2 interina (2023) añade uno más; aquí se seleccionan los más relevantes para organizaciones de la región.

## Autoevaluación

Califica cada criterio con la [escala común 0–4](../escala-y-metodo.md). 🔴 = imprescindible incluso para equipos pequeños.

| ID | Área | Criterio | Evidencia esperada | Referencia | Actual | Objetivo |
|---|---|---|---|---|---|---|
| IR-01 | Organización | 🔴 Mandato del equipo de respuesta aprobado por la dirección | Documento de mandato | SIM3 · O-1 | | |
| IR-02 | Organización | Comunidad atendida y alcance definidos (qué unidades, sistemas, filiales) | Documento de alcance | SIM3 · O-2 | | |
| IR-03 | Organización | 🔴 Autoridad y responsabilidades del equipo definidas (qué puede decidir: aislar, apagar, bloquear) | Matriz RACI aprobada | SIM3 · O-3 y O-4 | | |
| IR-04 | Procesos | 🔴 Clasificación de incidentes y criterios de severidad | Esquema de clasificación | SIM3 · Procesos · NIST SP 800-61r3 | | |
| IR-05 | Procesos | 🔴 Playbooks para los incidentes más probables (ransomware, phishing, BEC, fuga y brecha de datos) | Playbooks vigentes | NIST SP 800-61r3 | | |
| IR-06 | Procesos | 🔴 Escalamiento a la dirección y al área legal con criterios y tiempos | Procedimiento de escalamiento | SIM3 · P-1 | | |
| IR-07 | Herramientas | Herramientas de detección, contención y análisis forense disponibles y probadas | Inventario de herramientas | SIM3 · T-9 y T-10 | | |
| IR-08 | Procesos | Preservación de evidencia y cadena de custodia | Procedimiento y formatos | ISO/IEC 27037 | | |
| IR-09 | Personas | Formación y simulacros al menos una vez al año (incluido un ejercicio de mesa con la dirección) | Registros de ejercicios y lecciones | SIM3 · H-4 y H-5 | | |
| IR-10 | Personas | Código de conducta del equipo y resiliencia del personal (suplentes, guardias) | Código firmado, cuadro de guardias | SIM3 · H-1 y H-2 | | |
| IR-11 | Personas | Relación con el CSIRT nacional, pares del sector y comunidades de la región | Contactos verificados y membresías | SIM3 · H-7 | | |
| IR-12 | Procesos | Lecciones aprendidas y métricas de cada incidente relevante | Informes post-incidente | NIST SP 800-61r3 | | |
| IR-13 | Organización | Apoyo externo contratado o identificado (respuesta, forense, legal, seguro) | Contratos o acuerdos vigentes | NIST SP 800-61r3 | | |

**Puntaje del dominio** (promedio): ____ / 4

## Referencias
- SIM3, Open CSIRT Foundation: https://opencsirt.org · autoevaluación oficial: https://sim3-check.opencsirt.org
- NIST SP 800-61r3 · ISO/IEC 27035 · ISO/IEC 27037 (evidencia digital)
- FIRST CSIRT Services Framework
