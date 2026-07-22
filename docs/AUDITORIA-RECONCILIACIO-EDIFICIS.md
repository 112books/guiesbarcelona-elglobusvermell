# Auditoria de dades d'edificis — reconciliació de recomptes i coordenades

**Data de creació:** 2026-07-22
**Propòsit:** Document intern que recull la investigació sobre la discrepància de recomptes d'edificis (564 / 671 / 656) i l'auditoria de coordenades GPS, a partir de l'anàlisi dels dumps SQL disponibles.

---

## Resum

| Font | Recompte | Estat |
|------|----------|-------|
| Dump SQL (16 feb 2026) | 552 edificis reals | ✅ Auditat, coordenades netes |
| Dump SQL — total amb camp `egv_location` | 564 | ✅ Explicat (552 edificis + 9 Textos + 3 pàgines) |
| WordPress en viu (jul 2026) | 671 publicats | ⚠️ ~110-119 entrades noves des del dump, no auditades |
| "656" (xifra verbal de Xavi) | — | ❌ Càlcul incorrecte (671 − categories − tags) |

**Conclusió principal:** el dump de febrer 2026 està 100% net — cap dels 552 edificis reals hi manca coordenades. El problema de coordenades absents, si existeix, només pot afectar les ~110-119 fitxes afegides a WordPress entre febrer i juliol 2026, no capturades al dump.

---

## 1. Fonts de dades disponibles

Es van localitzar dos dumps SQL a `docs/documents originals/`:

| Fitxer | Mida | Data | Utilitat |
|--------|------|------|----------|
| `guiesbcn-elglobusvermell-20260216.sql` | 18,4 MB | 16 feb 2026 | ✅ Dump complet MySQL/WordPress (38 taules) — únic utilitzable |
| `Backup-PROD-260616/globus_vermell_260616.sql` | 280 KB | 15 jun 2026 | ❌ Dump PostgreSQL 17.8, sense relació amb WordPress — descartat |

El fitxer de juny és un `pg_dump` d'un projecte totalment diferent (probablement desat per error a la mateixa carpeta de còpies de seguretat). Tota l'anàlisi es basa exclusivament en el dump de febrer.

---

## 2. Estructura de la base de dades WordPress

- Els edificis s'emmagatzemen com a `post_type='post'` estàndard (no un custom post type).
- `wp_posts`: 2065 files totals (AUTO_INCREMENT 2293 → ~228 IDs eliminats amb el temps).
- 561 posts publicats (`post_status='publish'`) al dump de febrer.
- Coordenades GPS emmagatzemades a `wp_postmeta` com a camps personalitzats: `egv_location_lat` i `egv_location_lon` (prefix `egv_` = plugin/tema propi d'El Globus Vermell). També hi ha `egv_blob_color` i `egv_blob_background_color` per a l'estil dels marcadors al mapa.
- Taxonomia molt senzilla: 18 termes totals (9 categories de guia + 1 categoria "Textos" + 4 tags transversals).
- `wp_postmeta`: 5436 files parsejades (vs. AUTO_INCREMENT 7871 → ~2435 metadades eliminades històricament).

### Categories de guia (9) i comptadors

| Categoria | Posts |
|-----------|-------|
| Masies | 96 |
| Arquitectura Moderna 1950-75 | 88 |
| Eixample Jardins | 81 |
| Poblenou Industrial | 81 |
| Barceloneta | 63 |
| Biblioteques | 51 |
| Mercats | 43 |
| Avantguarda 1928-38 | 46 |
| Marina/Prat Vermell | 21 |

La suma (570) supera els 561 publicats perquè alguns edificis pertanyen a més d'una categoria/guia simultàniament.

### Tags transversals (4)

Espai públic (86), Nomenclàtor femení (46), Art públic (21), Dones arquitectes (17).

### Categoria no-edifici: "Textos" (9 posts)

Són articles editorials d'introducció, un per cada guia temàtica (IDs: 68, 83, 90, 103, 142, 154, 1302, 1676, 2025). Cadascun està doblement categoritzat: "Textos" + la seva categoria de guia pròpia. No representen edificis i no tenen coordenades (esperat i correcte).

**Recompte real d'edificis al dump:** 561 publicats − 9 Textos = **552 edificis**.

---

## 3. Explicació de la xifra "564"

`egv_location_lat` i `egv_location_lon` apareixen exactament **564 vegades** cadascun al dump. Aquest és l'origen de la xifra "564" citada anteriorment — **no és** el nombre de posts publicats, sinó el nombre de fitxes (posts + pàgines) amb el camp de coordenades.

Desglossament dels 564:

- **552** edificis reals (tots amb coordenades vàlides)
- **9** posts "Textos" (introduccions editorials, coordenades buides — correcte)
- **3** pàgines de WordPress: `Presentació` (ID 213), `En paper` (ID 215), `Crèdits` (ID 219) — també amb el camp buit

---

## 4. Auditoria de coordenades — resultat

✅ **Cap edifici del dump de febrer 2026 té coordenades absents.**

- Els 552 edificis reals tenen `egv_location_lat` i `egv_location_lon` no buits.
- Totes les coordenades validen dins el rang geogràfic de Barcelona (lat 41,0–41,6 / lon 1,9–2,4).
- Cap coordenada duplicada, corrupta o placeholder entre edificis; l'única "duplicació" és el parell buit (`''`, `''`) compartit pels 9 Textos.

**Implicació:** si hi ha edificis sense coordenades avui, només poden ser entre els que es van afegir a WordPress **després** del dump de febrer.

---

## 5. Explicació de la xifra "671" (WordPress en viu, juliol 2026)

Confirmat directament per Xavi: WordPress té actualment 671 entrades publicades.

- Diferència amb el dump: 671 − 552 = **~119 edificis nous** afegits entre febrer i juliol 2026.
- Aquestes ~110-119 fitxes noves **no s'han pogut auditar** perqure no existeixen al dump local — cal accés a WordPress en viu (usuari admin o exportació/BD actualitzada) per revisar-ne les coordenades.

---

## 6. Explicació de la xifra "656" (verbal, Xavi)

Xavi la va calcular com 671 menys categories i tags, assumint que el comptador de WordPress els inclou. **Aquest càlcul és incorrecte**: el comptador de "publicats" de WordPress ja exclou els termes de taxonomia (categories/tags no compten com a posts). La xifra "656" no té una correspondència real a la base de dades i es considera un error de càlcul, no una tercera font de veritat.

Nota addicional: la categoria de guia "1975-2008" no existeix al dump; la categoria "2009-2025" existeix però amb 0 posts (buida en el moment del dump).

---

## 7. Historial de publicació

- Primer post publicat: 2021-09-21. Últim post del dump: 2025-12-16 (el dump no conté res publicat el 2026).
- **410 dels 561 posts (73%)** es van crear en una importació massiva a l'octubre de 2021 — llançament inicial del lloc amb dataset pre-poblat.
- Només 151 posts afegits en més de 4 anys posteriors: setembre 2023 (20), **febrer 2024 (93 — segona guia important)**, març 2024 (1), desembre 2025 (6), més entrades soltes.
- Les ~110-119 fitxes que falten per auditar (dump → WP en viu) es van publicar totes després del desembre de 2025.

---

## 8. Properes passes

1. **Xavi/Jorge han de facilitar accés a WordPress en viu** (usuari admin o exportació/BD actualitzada de juliol 2026).
2. Amb aquest accés, auditar coordenades de les ~110-119 fitxes noves (post-febrer 2026) amb el mateix mètode de validació geogràfica aplicat aquí.
3. Verificar si les categories "1975-2008" i "2009-2025" s'han creat/poblat a WordPress en viu des de febrer.
4. Un cop confirmat l'accés, represa de la migració amb `scripts/importa-edificis-wp.py` i `scripts/importa-edificis-sql.py` (eines existents).

---

## 9. Referències

- Dump analitzat: `docs/documents originals/guiesbcn-elglobusvermell-20260216.sql`
- Scripts de migració relacionats: `scripts/importa-edificis-sql.py`, `scripts/importa-edificis-wp.py`, `scripts/importa-text-publicacions.py`, `scripts/geocodifica-edificis.py`
- Correu pendent a Xavi amb aquest resum (esborrany, pendent d'aprovació de Joan) — recull la mateixa reconciliació en llenguatge de client.
