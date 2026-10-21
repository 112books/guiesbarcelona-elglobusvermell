#!/usr/bin/env python3
"""Redimensiona automaticament les imatges que superen el limit.

Pensat per a la build (CI): els editors pugen les fotos tal com les tenen i el
sistema les ajusta abans de publicar-les, de manera que el web no serveixi mai
imatges desproporcionades.

Criteris (es poden canviar per parametres):
  - amplada maxima: 1600 px
  - pes maxim: 400 KB

Si una imatge supera qualsevol dels dos limits, es redimensiona (mantenint la
proporcio) i es recomprimeix en JPEG progressiu. Si baixant la qualitat encara
no n'hi ha prou, es va reduint l'amplada de 10 en 10 % fins a 1000 px.

Us:
  python3 scripts/redimensiona-imatges.py                # aplica els canvis
  python3 scripts/redimensiona-imatges.py --dry-run      # nomes informa
  python3 scripts/redimensiona-imatges.py --carpetes static/img/elements
"""
import argparse
import io
import os
import sys

from PIL import Image

BASES = ["static/img/elements", "static/img/publicacions"]
EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp")


def mida_llegible(kb):
    return f"{kb / 1024:.0f} MB" if kb >= 1024 else f"{kb:.0f} KB"


def processa(cami, max_amplada, max_pes_kb, qualitat, qualitat_min, max_amplada_min, dry_run):
    pes_original = os.path.getsize(cami)
    try:
        with Image.open(cami) as img:
            amplada, alcada = img.size
    except Exception as e:  # imatge corrupta o format no suportat
        print(f"AVIS: no puc obrir {cami}: {e}", file=sys.stderr)
        return None

    supera_amplada = amplada > max_amplada
    supera_pes = pes_original > max_pes_kb * 1024
    if not (supera_amplada or supera_pes):
        return None

    if dry_run:
        return (cami, pes_original, pes_original, (amplada, alcada), (amplada, alcada), True)

    with Image.open(cami) as img:
        if img.mode not in ("RGB", "L"):
            img = img.convert("RGB")
        if supera_amplada:
            nova_alcada = max(1, round(alcada * max_amplada / amplada))
            img = img.resize((max_amplada, nova_alcada), Image.LANCZOS)

        # 1) baixem qualitat fins al minim; 2) si encara passa, reduïm amplada.
        q = qualitat
        treball = img
        limit = max_pes_kb * 1024
        while True:
            buf = io.BytesIO()
            treball.save(buf, format="JPEG", quality=q, optimize=True, progressive=True)
            dades = buf.getvalue()
            if len(dades) <= limit:
                break
            if q > qualitat_min:
                q = max(qualitat_min, q - 5)
                continue
            a, h = treball.size
            if a <= max_amplada_min:
                break
            nova_a = max(max_amplada_min, round(a * 0.9))
            treball = treball.resize((nova_a, max(1, round(h * nova_a / a))), Image.LANCZOS)
            q = qualitat

        # Si el resultat no és més petit que l'original (casos rars), no toquem res.
        if len(dades) >= pes_original:
            return None

        nou_cami = os.path.splitext(cami)[0] + ".jpg"
        with open(nou_cami + ".tmp", "wb") as fp:
            fp.write(dades)
        os.replace(nou_cami + ".tmp", nou_cami)
        if nou_cami != cami and os.path.exists(cami):
            os.remove(cami)  # p. ex. un .png gran que passa a .jpg
        with Image.open(nou_cami) as img2:
            nova_mida = img2.size
    return (nou_cami, pes_original, len(dades), (amplada, alcada), nova_mida, False)


def main():
    ap = argparse.ArgumentParser(description="Redimensiona les imatges que superen el limit.")
    ap.add_argument("--carpetes", nargs="+", default=BASES, help="carpetes a revisar")
    ap.add_argument("--max-amplada", type=int, default=1600, help="amplada maxima en px (per defecte 1600)")
    ap.add_argument("--max-pes", type=int, default=400, help="pes maxim en KB (per defecte 400)")
    ap.add_argument("--qualitat", type=int, default=82, help="qualitat JPEG inicial (per defecte 82)")
    ap.add_argument("--qualitat-min", type=int, default=65, help="qualitat JPEG minima (per defecte 65)")
    ap.add_argument("--max-amplada-min", type=int, default=1000, help="amplada minima si cal reduir mes (per defecte 1000)")
    ap.add_argument("--dry-run", action="store_true", help="no modifica cap fitxer")
    args = ap.parse_args()

    canviades = 0
    estalvi = 0
    revisades = 0
    for base in args.carpetes:
        if not os.path.isdir(base):
            continue
        for nom in sorted(os.listdir(base)):
            if not nom.lower().endswith(EXTENSIONS):
                continue
            revisades += 1
            cami = os.path.join(base, nom)
            r = processa(cami, args.max_amplada, args.max_pes, args.qualitat, args.qualitat_min, args.max_amplada_min, args.dry_run)
            if not r:
                continue
            canviades += 1
            nou_cami, abans, despres, mida_abans, mida_despres, dry = r
            estalvi += abans - despres
            accio = "reduiria" if dry else "reduïda"
            print(
                f"{accio}: {os.path.basename(nou_cami)}  {mida_llegible(abans / 1024)} -> {mida_llegible(despres / 1024)}"
                f"  ({mida_abans[0]}x{mida_abans[1]} -> {mida_despres[0]}x{mida_despres[1]})"
            )

    print(
        f"\n{revisades} imatges revisades · {canviades} {'per reduir' if args.dry_run else 'reduïdes'}"
        f" · estalvi {mida_llegible(estalvi / 1024)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
