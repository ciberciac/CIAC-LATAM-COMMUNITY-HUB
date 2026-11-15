# Plan de prueba de concepto (PoC)

Objetivo: medir con hechos lo que el proveedor afirma sobre detección, escalamiento y respuesta.

## Condiciones
- [ ] Entorno acotado y autorizado: equipos de prueba o un segmento definido, nunca producción crítica sin aprobación.
- [ ] Autorización escrita de la dirección y de TI, con fechas y responsables.
- [ ] Mismas condiciones para todos los proveedores evaluados.
- [ ] El proveedor conoce el período de la prueba, pero **no** el momento ni las técnicas exactas.

## Duración sugerida
2 a 4 semanas: una para integrar fuentes, el resto para operar y emular.

## Escenarios de emulación
Usa herramientas de emulación de código abierto (como Atomic Red Team o MITRE Caldera) en equipos de prueba. Elige técnicas de actores relevantes para tu sector y región.

| # | Escenario | Técnicas ATT&CK de ejemplo | Esperado |
|---|---|---|---|
| 1 | Ejecución de script desde un adjunto | T1204.002, T1059.001 | Detección y notificación |
| 2 | Persistencia con tarea programada | T1053.005 | Detección |
| 3 | Volcado de credenciales | T1003.001 | Detección y contención según la matriz preautorizada |
| 4 | Herramienta de acceso remoto no autorizada | T1219 | Detección |
| 5 | Borrado de instantáneas de volumen | T1490 | Detección crítica y escalamiento inmediato |
| 6 | Inicio de sesión anómalo en la nube y regla de reenvío de correo | T1078.004, T1114.003 | Detección y notificación |

## Qué medir

| Métrica | Proveedor A | Proveedor B | Proveedor C |
|---|---|---|---|
| Escenarios detectados / total | | | |
| Tiempo desde la ejecución hasta la notificación (por escenario) | | | |
| Calidad de la notificación: contexto, técnica, impacto, recomendación | | | |
| Acciones de contención ejecutadas correctamente | | | |
| Falsos positivos generados durante la prueba | | | |
| Calidad del informe final | | | |

Registra los resultados en la sección **D** y **E** de la matriz comparativa.
