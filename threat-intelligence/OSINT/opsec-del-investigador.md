# OPSEC del investigador

Investigar deja rastro: visitas en registros de servidores, consultas que alertan al objetivo, cuentas vinculadas a tu identidad real.

## Controles mínimos
- [ ] **Entorno aislado:** máquina virtual dedicada (o distribución especializada) que se revierte a un estado limpio.
- [ ] **Navegador separado** sin sesiones personales ni corporativas, sin extensiones innecesarias.
- [ ] **Red:** VPN o salida dedicada; nunca investigar infraestructura adversaria desde la red corporativa.
- [ ] **No interactuar** con la infraestructura del atacante si no es necesario: prefiere servicios que ya la escanearon (urlscan.io, Shodan, Censys, sandboxes).
- [ ] **Escaneos públicos con cuidado:** al enviar una URL a un servicio público, puede quedar visible para todos, incluido el atacante. Usa el modo privado cuando exista o evita enviar URLs con datos de la víctima.
- [ ] **Identidades de investigación** (si la política de tu organización lo permite): separadas de las personales, sin interacción con personas reales.
- [ ] **Higiene de archivos:** no abras documentos descargados fuera del entorno aislado.
- [ ] **Registro de actividad:** anota qué consultaste, cuándo y desde dónde.

## Señales de que te expusiste
- El contenido del sitio cambia o desaparece tras tus visitas.
- Te bloquean por IP o geolocalización.
- Recibes contacto inesperado relacionado con la investigación.
