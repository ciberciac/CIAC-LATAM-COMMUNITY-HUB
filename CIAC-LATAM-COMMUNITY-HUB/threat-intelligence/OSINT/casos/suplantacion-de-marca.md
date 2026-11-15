# Metodología · Suplantación de marca

Detectar sitios de phishing, perfiles falsos y aplicaciones que usan la marca de una organización, uno de los vectores más frecuentes contra banca, comercio y gobierno en la región.

## Fuentes a monitorear
- **Dominios:** registros nuevos parecidos a la marca (variaciones, caracteres homógrafos, dominios de país), transparencia de certificados.
- **Redes sociales:** perfiles y anuncios que imitan a la marca o a su atención al cliente.
- **Tiendas de aplicaciones** y sitios de descarga de APK.
- **Mensajería:** canales y grupos que usan el nombre de la organización.
- **Buscadores:** anuncios pagados que suplantan el sitio oficial.

## Flujo
1. **Detección:** alerta de un dominio o perfil sospechoso.
2. **Verificación:** captura vía urlscan.io, comparación con el sitio oficial, ¿captura credenciales o datos de tarjeta?
3. **Clasificación:** phishing activo · en preparación (dominio estacionado) · uso legítimo de terceros · falso positivo.
4. **Acción:**
   - Bloqueo interno (correo, proxy, DNS).
   - Solicitud de baja al registrador, al hosting, a la plataforma o a la tienda.
   - Reporte a listas de bloqueo públicas y al CSIRT nacional.
   - Aviso a clientes si la campaña es masiva.
5. **Seguimiento:** verificar la baja y vigilar reapariciones con el mismo patrón.

## Registro
| Fecha | Tipo | Indicador (desactivado) | Estado | Solicitud de baja | Resultado |
|---|---|---|---|---|---|
