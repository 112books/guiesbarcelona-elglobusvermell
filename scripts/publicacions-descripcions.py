#!/usr/bin/env python3
"""Afegeix description i foto (portada) al front matter dels bundles de publicació.

Les descripcions es deriven de data/publicacions.yaml (títol + any d'edició).
La foto apunta a la portada corresponent de static/img/publicacions/ si existeix.
Idempotent: no toca els bundles que ja tenen description.
"""
import os

BASE = "content/ca/publicacions"

DESCR = {
    "gatcpac": "Plànol-guia de l'arquitectura d'avantguarda a Barcelona (1928-1939): el GATCPAC i el racionalisme, amb els edificis més representatius del període.",
    "interiors-illa": "La xarxa de jardins interiors d'illa de l'Eixample: més de 70 espais verds recuperats dins la trama de Cerdà, amb la història de cada jardí i del seu nom.",
    "poblenou": "El patrimoni industrial del Poblenou: fàbriques, xemeneies i naus de l'antic barri fabril de Barcelona.",
    "50-75": "Arquitectura Moderna a Barcelona, 1950-1975: els edificis del creixement de la ciutat entre el Moviment Modern i el desenvolupisme.",
    "mercats": "Els mercats de Barcelona: la xarxa de mercats municipals i no alimentaris de la ciutat, de la Boqueria als encants.",
    "barceloneta": "La Barceloneta: història, arquitectura i art públic del barri marítim de Barcelona.",
    "marina": "La Marina del Port i del Prat Vermell: el passat industrial i la transformació urbana del sud de Barcelona.",
    "tapies": "La Barcelona de Tàpies: itinerari per l'obra de l'artista i la seva relació amb la ciutat.",
    "masies": "Masies de Barcelona: el patrimoni rural i agrícola que ha sobreviscut dins la ciutat. Plànol-guia en preparació.",
    "biblioteques": "Biblioteques de Barcelona: de les biblioteques populars de la Mancomunitat als nous equipaments de lectura. Plànol-guia en preparació.",
    "new-babylon": "New Babylon Barcelona: plànol-guia d'art i urbanisme. En preparació.",
    "76-08": "De l'esperança a la crisi. 1975-2008: l'arquitectura de la Barcelona de la democràcia. Plànol-guia en preparació.",
    "09-25": "La revolució tranquil·la. 2010-2025: l'arquitectura recent de Barcelona. Plànol-guia en preparació.",
}


def main():
    if not os.path.isdir(BASE):
        raise SystemExit(f"No trobo {BASE}")

    for slug in sorted(os.listdir(BASE)):
        fitxer = os.path.join(BASE, slug, "_index.md")
        if not os.path.isfile(fitxer):
            continue
        if slug not in DESCR:
            print(f"SKIP  {slug}: sense descripció definida")
            continue

        text = open(fitxer, encoding="utf-8").read()
        parts = text.split("---")
        if len(parts) < 2 or "description:" in parts[1]:
            print(f"JA    {slug}: ja té description")
            continue

        foto = f"/img/publicacions/{slug}.jpg"
        insertar = [f'description: "{DESCR[slug]}"']
        if os.path.isfile(f"static{foto}"):
            insertar.append(f'foto: "{foto}"')
        else:
            print(f"NOTE  {slug}: sense portada a static{foto}")

        lines = text.split("\n")
        out = []
        insertat = False
        for ln in lines:
            out.append(ln)
            if not insertat and ln.startswith("title:"):
                out.extend(insertar)
                insertat = True
        if not insertat:
            print(f"WARN  {slug}: no trobo la línia title:")
            continue

        open(fitxer, "w", encoding="utf-8").write("\n".join(out))
        print(f"OK    {slug}")


if __name__ == "__main__":
    main()
