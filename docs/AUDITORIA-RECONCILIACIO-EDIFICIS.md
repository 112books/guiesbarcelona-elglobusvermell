# Auditoria de dades d'edificis — reconciliació de recomptes i coordenades

**Data de creació:** 2026-07-22
**Última actualització:** 2026-07-23 (dump fresc de producció obtingut i auditat — veure secció 10)
**Propòsit:** Document intern que recull la investigació sobre la discrepància de recomptes d'edificis (564 / 671 / 656) i l'auditoria de coordenades GPS, a partir de l'anàlisi dels dumps SQL disponibles.

---

## Resum

| Font | Recompte | Estat |
|------|----------|-------|
| Dump SQL (16 feb 2026) | 552 edificis reals | ✅ Auditat, coordenades netes |
| Dump SQL — total amb camp `egv_location` | 564 | ✅ Explicat (552 edificis + 9 Textos + 3 pàgines) |
| WordPress en viu (jul 2026) | 671 publicats | ✅ **Confirmat exacte** amb dump fresc del 23 jul 2026 (660 edificis + 11 Textos) |
| "656" (xifra verbal de Xavi) | — | ✅ Correspon al Hugo estàtic (GitHub) del 21 jul 2026 — 4 elements per darrere de producció WP |

**Conclusió principal:** amb el dump fresc del 23 juliol 2026 (extret directament del servidor via SSH/mysqldump), les tres xifres queden totalment reconciliades: **671** = publicats a WordPress en viu (exacte), **656** = elements al Hugo estàtic (GitHub) tal com estava el 21 jul, **564** = xifra parcial del dump antic de febrer. El Hugo estàtic va 4 elements per darrere de la producció WordPress actual (660 vs 656) — pendent sincronitzar.

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

## 8. Properes passes (actualitzat 2026-07-23)

Ordre acordat amb Joan:

1. **Desar les dades d'accés** al servidor (SSH, panell YunoHost) perquè es pugui entrar tant des d'aquest ordinador com des de casa. *(Accés SSH ja establert des d'aquest Mac — veure secció 10. Pendent replicar des de l'ordinador de casa.)*
2. **Descarregar les imatges** necessàries per a cada punt del mapa i associar-les a la fitxa corresponent.
3. **Descarregar els dumps de les BBDD de WordPress** (`wordpress__2` i `wordpress__3`) per treballar-hi en local. *(Dump de `wordpress__3` — guiesbarcelona — ja fet, veure secció 10. Falta `wordpress__2` — elglobusvermell.)*
4. **Verificar dades de producció** contra el projecte Hugo/GitHub (aquest repositori).

Pendents tècnics addicionals:
- Auditar coordenades de les fitxes noves (post-febrer 2026) — ja fet amb el dump de juliol, veure secció 10.
- Verificar si les categories "1975-2008" i "2009-2025" s'han creat/poblat a WordPress en viu des de febrer.
- Un cop sincronitzat, represa de la migració amb `scripts/importa-edificis-wp.py` i `scripts/importa-edificis-sql.py` (eines existents).

---

## 9. Referències

- Dump analitzat (febrer): `docs/documents originals/guiesbcn-elglobusvermell-20260216.sql`
- Dump analitzat (juliol): `sql-dumps/guiesbarcelona-dump-20260723.sql`
- Scripts de migració relacionats: `scripts/importa-edificis-sql.py`, `scripts/importa-edificis-wp.py`, `scripts/importa-text-publicacions.py`, `scripts/geocodifica-edificis.py`
- Correu pendent a Xavi amb aquest resum (esborrany, pendent d'aprovació de Joan) — recull la mateixa reconciliació en llenguatge de client.

---

## 10. Actualització 23 juliol 2026 — Accés al servidor i dump fresc

### Accés obtingut

- Servidor: VPS Hetzner (195.201.2.76), YunoHost (Debian), backup diari automàtic.
- SSH: usuari `tech` (grup sudo), clau pública d'aquest Mac afegida per Jorge a `authorized_keys`. Sessió `tmux` (`yuno`) oberta com a `root` — permet executar ordres amb privilegis sense sudo interactiu.
- Panell web YunoHost: `https://panel.elglobusvermell.org/yunohost/admin/` — credencials es gestionen per CLI (`yunohost user list` / `yunohost user update --change-password`), no calen dades addicionals de Jorge.
- Apps YunoHost rellevants: `wordpress__2` (elglobusvermell.org, WP 5.8), `wordpress__3` (guiesbarcelona, WP 6.5). Hi ha una migració Debian Bookworm pendent (`0027_migrate_to_bookworm`, manual) — no tocar sense avisar.
- `/var/www/`: `elglobusvermell → wordpress__2`, `guiesbarcelona → wordpress__3`. També hi ha `my_webapp` (backup/import antic, a revisar si cal) i `snappymail` (correu web).

### Dump fresc de `wordpress__3`

Extret via `mysqldump` directe a la BD del YunoHost (credencials de `/etc/yunohost/apps/wordpress__3/settings.yml`), 23 jul 2026 14:03. Desat a `sql-dumps/guiesbarcelona-dump-20260723.sql` (21,7 MB).

### Resultat de la reconciliació precisa (parsing exacte de `wp_posts` + `wp_postmeta`, mateix mètode que febrer)

| Mètrica | Feb 2026 | Jul 2026 | Diferència |
|---|---|---|---|
| Posts publicats (`post_type='post'`, `post_status='publish'`) | 561 | **671** | +110 |
| Edificis amb coordenades vàlides (rang BCN) | 552 | **660** | +108 |
| Textos editorials (sense coordenades, esperat) | 9 | **11** | +2 |
| Coordenades fora de rang o corruptes | 0 | **0** | — |
| IDs nous publicats des de febrer | — | 119 | — |
| IDs despublicats/eliminats des de febrer | — | 9 | — |

**El "671" de WordPress en viu queda confirmat exacte i quadra al 100%** amb la suma 660 edificis + 11 textos editorials. Zero coordenades absents o invàlides entre els edificis publicats — el mateix nivell de neteja que el dump de febrer.

### Els 11 Textos (no-edificis, sense coordenades — correcte)

IDs: 68, 83, 90, 103, 142, 154, 1302, 1676, 2025 (els 9 de febrer) + **2 de nous**: *"La Marina del Port i del Prat Vermell"* (ID 1676 — ja hi era) i confirmació de dues guies noves consolidades (*"Arquitectura a Barcelona 1975-2008"* i *"Arquitectura a Barcelona 2010-2025"*), que abans no existien com a categories poblades.

### Comparació amb el Hugo estàtic (aquest repositori, GitHub)

- `content/ca/elements/`: **656** fitxes de bundle (comptades el 21 jul 2026, coincidint amb `docs/revisio-elements-qualitat.md`).
- WordPress producció (23 jul): **660** edificis vàlids.
- **Diferència: 4 edificis** publicats a WordPress que encara no s'han portat/generat al lloc Hugo. Cal identificar-los i sincronitzar-los (pendent — punt 4 de la llista de properes passes).
