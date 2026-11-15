# Metodología · Exposición organizacional

Ver la organización como la ve un atacante en la fase de reconocimiento (ATT&CK TA0043) para reducir su superficie de ataque.

## Alcance
Dominios y marcas de la organización, con autorización. Resultado: un informe priorizado de exposiciones con recomendaciones.

## Pasos

### 1. Activos de Internet
- [ ] Dominios y subdominios: registros públicos, certificados (crt.sh), DNS pasivo.
- [ ] Rangos IP y ASN propios.
- [ ] Servicios expuestos (Shodan, Censys): VPN, RDP, paneles de administración, bases de datos, equipos de borde.
- [ ] Versiones vulnerables con CVE conocidos (priorizar las del catálogo CISA KEV).

### 2. Configuración de correo
- [ ] SPF, DKIM y DMARC (política y alineación).
- [ ] Dominios parecidos registrados por terceros.

### 3. Información en código y documentos
- [ ] Repositorios públicos con nombre de la organización: secretos, configuraciones, rutas internas.
- [ ] Documentos públicos con metadatos (autores, rutas, versiones de software).
- [ ] Almacenamiento en la nube público asociado a la marca.

### 4. Credenciales y datos filtrados
- [ ] Servicios de notificación de filtraciones para los dominios corporativos.
- [ ] Menciones en sitios de filtración de grupos de extorsión y en foros.
- [ ] Credenciales de empleados en registros de *infostealers* (vía proveedores o servicios autorizados).
- **Sin descargar ni probar credenciales.** Se reportan para su rotación.

### 5. Personas y procesos (con criterio de proporcionalidad)
- [ ] Estructura organizacional y roles expuestos que facilitan phishing dirigido o BEC (finanzas, dirección, TI).
- [ ] Información de proveedores y tecnologías usadas publicada en ofertas de empleo.

## Entregable
| Hallazgo | Evidencia | Riesgo | Técnica ATT&CK habilitada | Recomendación | Prioridad |
|---|---|---|---|---|---|
| RDP expuesto en 203.0.113.x | Shodan, AAAA-MM-DD | Alto | T1133, T1110 | Retirar de Internet; acceso vía VPN con MFA | 🔴 |
