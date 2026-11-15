# Playbook · Fuga de datos (Data Leak)

| | |
|---|---|
| **Qué es** | Exposición **no intencionada** de información: no hay (todavía) evidencia de un atacante que la haya robado |
| **Ejemplos** | Bucket o carpeta compartida pública, base de datos expuesta a Internet, credenciales en un repositorio de código, archivo enviado al destinatario equivocado, datos de la empresa que aparecen publicados en un foro, un *paste* o un canal de Telegram |
| **Severidad por defecto** | Media (alta si hay datos personales sensibles, financieros o credenciales) |
| **ATT&CK relacionado** | T1530 Data from Cloud Storage · T1552 Unsecured Credentials · T1213 Data from Information Repositories |

> **Fuga vs. brecha.** Si durante el análisis aparece evidencia de que un tercero **accedió o extrajo** los datos, el caso pasa a ser una [brecha de datos](../data-breach/). En la duda, trata la exposición como si hubiera sido aprovechada hasta demostrar lo contrario.

## 0. Preparación
- [ ] Inventario de dónde están los datos sensibles y quién es su dueño.
- [ ] Monitoreo de exposición: escaneo de la superficie externa, buckets públicos, secretos en repositorios (secret scanning), menciones de la marca y dominios en fuentes abiertas ([OSINT](../../threat-intelligence/OSINT/)).
- [ ] Contacto del área legal y del oficial de protección de datos.

## 1. Detección y análisis
- [ ] **Confirmar** la exposición sin descargar más datos de los necesarios para verificarla.
- [ ] Identificar **qué datos** quedaron expuestos: tipo (personales, sensibles, financieros, credenciales, propiedad intelectual) y volumen aproximado.
- [ ] Determinar **desde cuándo** estuvo expuesto y **quién pudo acceder**:
  - Registros de acceso del recurso (logs de almacenamiento en la nube, del servidor, del repositorio).
  - Si el recurso fue indexado por buscadores o motores como Shodan o Censys.
- [ ] Si los datos aparecieron **publicados por terceros**: registrar la evidencia (captura, URL, hash, fecha UTC) sin interactuar con quien los publicó ni pagar por acceder.
- [ ] Clasificar: ¿hay evidencia de acceso no autorizado? → si es sí, activar el playbook de **brecha de datos**.

## 2. Contención
- [ ] **Cerrar la exposición:** quitar el acceso público, apagar el servicio expuesto, retirar el archivo, revocar el enlace compartido.
- [ ] **Rotar inmediatamente** toda credencial, token o llave expuesta, aunque ya se haya borrado: el historial de Git y las copias en caché la conservan.
- [ ] Solicitar la **retirada** del contenido publicado por terceros (al proveedor de la plataforma, al buscador para desindexar).
- [ ] Preservar la evidencia antes de cambiar configuraciones: capturas de la configuración y registros de acceso.

## 3. Erradicación
- [ ] Eliminar la causa raíz: configuración por defecto insegura, proceso manual sin control, falta de revisión.
- [ ] Limpiar el historial del repositorio si contenía secretos (y aun así rotarlos).
- [ ] Revisar recursos similares: si un bucket estaba público, revisar todos.

## 4. Recuperación
- [ ] Verificar que el recurso ya no es accesible desde Internet.
- [ ] Monitorear el uso de las credenciales rotadas y la aparición de los datos en fuentes abiertas durante al menos 30 días.

## Notificación
Aunque no haya atacante confirmado, **una exposición de datos personales puede ser un incidente notificable**. Evalúa con legal según la [tabla de la brecha de datos](../data-breach/README.md#notificaciones-en-latam).

## 5. Lecciones aprendidas
- [ ] Control preventivo que habría evitado la fuga (política que impida recursos públicos, secret scanning con bloqueo, DLP, revisión de permisos).
- [ ] Informe con [`templates/incident-report.md`](../../templates/incident-report.md).

## Referencias
- NIST SP 800-61r3 · OWASP Secrets Management Cheat Sheet · CIS Controls v8.1 (Control 3: Protección de datos)
