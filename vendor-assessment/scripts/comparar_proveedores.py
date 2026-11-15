#!/usr/bin/env python3
"""Compara proveedores con la matriz ponderada.

Uso:
  python comparar_proveedores.py ../plantillas/matriz-comparativa.csv ../plantillas/pesos.csv

- Cada columna después de 'excluyente' es un proveedor, con puntajes de 0 a 4.
- Un criterio excluyente con puntaje menor que 2 descalifica al proveedor.
- El total se expresa de 0 a 100.
"""
import csv, sys
from collections import defaultdict

FIJAS = ["seccion", "id", "criterio", "excluyente"]


def num(v):
    v = (v or "").strip().replace(",", ".")
    if not v:
        return None
    n = float(v)
    if not 0 <= n <= 4:
        raise ValueError(f"puntaje fuera de 0–4: {v}")
    return n


def main(matriz, pesos_csv):
    with open(pesos_csv, encoding="utf-8-sig", newline="") as f:
        pesos = {r["seccion"]: float(r["peso"]) for r in csv.DictReader(f)}
    with open(matriz, encoding="utf-8-sig", newline="") as f:
        lector = csv.DictReader(f)
        proveedores = [c for c in lector.fieldnames if c not in FIJAS]
        filas = list(lector)

    resultados = {}
    for p in proveedores:
        por_seccion, descalificado, sin_puntaje = defaultdict(list), [], 0
        for r in filas:
            n = num(r[p])
            if n is None:
                sin_puntaje += 1
                n = 0.0
            por_seccion[r["seccion"]].append(n)
            if r["excluyente"].strip().lower() == "si" and n < 2:
                descalificado.append(r["id"])
        total_pesos = sum(pesos.get(s, 0) for s in por_seccion)
        total = sum(pesos.get(s, 0) * (sum(v) / len(v)) / 4 for s, v in por_seccion.items()) / total_pesos * 100
        resultados[p] = (total, descalificado, sin_puntaje,
                         {s: sum(v) / len(v) for s, v in por_seccion.items()})

    print("| Proveedor | Puntaje (0–100) | Estado | Criterios sin puntaje |")
    print("|---|---|---|---|")
    for p, (t, d, s, _) in sorted(resultados.items(), key=lambda x: (bool(x[1][1]), -x[1][0])):
        estado = "Descalificado: " + ", ".join(d) if d else "Habilitado"
        print(f"| {p} | {t:.1f} | {estado} | {s} |")

    secciones = list(next(iter(resultados.values()))[3])
    print("\n| Sección | " + " | ".join(proveedores) + " |")
    print("|---|" + "---|" * len(proveedores))
    for s in secciones:
        print(f"| {s} | " + " | ".join(f"{resultados[p][3][s]:.1f}" for p in proveedores) + " |")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
