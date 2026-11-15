#!/usr/bin/env python3
"""Calcula puntajes de madurez a partir de plantillas/autoevaluacion.csv.

Uso:
  python calcular_madurez.py ruta/autoevaluacion.csv [--radar radar.png]

Genera una tabla en Markdown por dominio y, si está instalado matplotlib, un gráfico de radar.
"""
import argparse, csv, sys
from collections import defaultdict


def a_numero(valor):
    valor = (valor or "").strip().replace(",", ".")
    if not valor:
        return None
    n = float(valor)
    if not 0 <= n <= 4:
        raise ValueError(f"nivel fuera de la escala 0–4: {valor}")
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--radar", help="archivo PNG para el gráfico de radar")
    a = ap.parse_args()

    dominios = defaultdict(lambda: {"actual": [], "objetivo": [], "brechas": []})
    with open(a.csv, encoding="utf-8-sig", newline="") as f:
        for fila in csv.DictReader(f):
            actual, objetivo = a_numero(fila["nivel_actual"]), a_numero(fila["nivel_objetivo"])
            if actual is None:
                continue
            d = dominios[fila["dominio"]]
            d["actual"].append(actual)
            if objetivo is not None:
                d["objetivo"].append(objetivo)
                brecha = objetivo - actual
                if brecha > 0:
                    peso = 2 if fila["imprescindible"].strip().lower() == "si" else 1
                    d["brechas"].append((brecha * peso, fila["id"], fila["criterio"], actual, objetivo))

    if not dominios:
        sys.exit("No hay criterios calificados en la columna nivel_actual.")

    prom = lambda xs: sum(xs) / len(xs) if xs else None
    print("| Dominio | Criterios evaluados | Actual | Objetivo | Brecha |")
    print("|---|---|---|---|---|")
    for nombre, d in dominios.items():
        act, obj = prom(d["actual"]), prom(d["objetivo"])
        brecha = f"{obj - act:.1f}" if obj is not None else "—"
        print(f"| {nombre} | {len(d['actual'])} | {act:.1f} | {obj:.1f} | {brecha} |" if obj is not None
              else f"| {nombre} | {len(d['actual'])} | {act:.1f} | — | — |")

    print("\n## Brechas prioritarias (brecha × peso)\n")
    print("| Prioridad | ID | Criterio | Actual | Objetivo |")
    print("|---|---|---|---|---|")
    todas = sorted((b for d in dominios.values() for b in d["brechas"]), reverse=True)
    for p, i, c, act, obj in todas[:10]:
        print(f"| {p:.1f} | {i} | {c} | {act:g} | {obj:g} |")

    if a.radar:
        try:
            import math
            import matplotlib
            matplotlib.use("Agg")
            import matplotlib.pyplot as plt
        except ImportError:
            sys.exit("Para el radar instala matplotlib: pip install matplotlib")
        nombres = list(dominios)
        actual = [prom(dominios[n]["actual"]) for n in nombres]
        objetivo = [prom(dominios[n]["objetivo"]) or 0 for n in nombres]
        ang = [i / len(nombres) * 2 * math.pi for i in range(len(nombres))]
        ang += ang[:1]
        fig, ax = plt.subplots(figsize=(7, 7), subplot_kw={"polar": True})
        for serie, etiqueta in ((objetivo, "Objetivo"), (actual, "Actual")):
            valores = serie + serie[:1]
            ax.plot(ang, valores, label=etiqueta)
            ax.fill(ang, valores, alpha=0.15)
        ax.set_xticks(ang[:-1])
        ax.set_xticklabels(nombres, fontsize=8)
        ax.set_ylim(0, 4)
        ax.set_yticks([1, 2, 3, 4])
        ax.legend(loc="upper right", bbox_to_anchor=(1.25, 1.1))
        ax.set_title("Madurez por dominio (escala 0–4)")
        fig.tight_layout()
        fig.savefig(a.radar, dpi=150)
        print(f"\nRadar guardado en {a.radar}")


if __name__ == "__main__":
    main()
