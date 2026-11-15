# Suricata

- Un archivo `.rules` por familia o campaña.
- `sid` en el rango **9400000–9499999**, reservado para esta comunidad. Registra el tuyo en [`sid-registro.csv`](sid-registro.csv) para no repetir.
- `msg` con prefijo `CIAC`, `classtype` adecuado, `reference:url,...;`
- `metadata: mitre_technique_id Txxxx, created_at AAAA_MM_DD, status experimental;`

Validar: `suricata -T -S archivo.rules -c /etc/suricata/suricata.yaml`
