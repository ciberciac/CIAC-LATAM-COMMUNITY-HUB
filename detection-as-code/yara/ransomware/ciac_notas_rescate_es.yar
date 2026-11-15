rule CIAC_Nota_Rescate_ES
{
    meta:
        author       = "CIAC LATAM Community"
        description  = "Frases frecuentes de notas de rescate en español junto a instrucciones de pago o contacto por Tor"
        date         = "2026-11-14"
        reference    = "https://github.com/ciberciac/CIAC-LATAM-COMMUNITY-HUB"
        hash         = ""
        mitre_attack = "T1486"
        status       = "experimental"
        license      = "DRL 1.1"

    strings:
        $es1 = "sus archivos han sido cifrados" ascii wide nocase
        $es2 = "tus archivos han sido cifrados" ascii wide nocase
        $es3 = "sus datos han sido robados" ascii wide nocase
        $es4 = "tus datos han sido robados" ascii wide nocase
        $es5 = "para recuperar sus archivos" ascii wide nocase
        $c1  = ".onion" ascii wide nocase
        $c2  = "bitcoin" ascii wide nocase
        $c3  = "tor browser" ascii wide nocase

    condition:
        filesize < 200KB and 1 of ($es*) and 1 of ($c*)
}
