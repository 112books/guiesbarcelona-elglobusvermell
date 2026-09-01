# Verificació diària dels números del web

**Execució:** 01/09/2026 13:40 UTC · **Font pública:** https://112books.github.io/guiesbarcelona-elglobusvermell/

## Resultat: ✅ tot coincideix

| Xifra de portada | Publicat | Segons el repo | Estat |
|---|---|---|---|
| Edificis documentats | 659 | 659 | ✓ |
| Guies de camp | 13 | 13 | ✓ |
| Arquitectes i estudis | 274 | 274 | ✓ |
| Anys d'arquitectura | 1928–2026 | 1928–2026 | ✓ |

## Què vol dir cada xifra

- **Edificis documentats**: fitxes d'element *amb coordenades* (així les conta la portada). Les fitxes sense coordenades no compten, encara que existeixin.
- **Guies de camp**: guies del projecte (entrades de `data/publicacions.yaml`). No totes tenen pàgina pròpia al web: New Babylon i La Barcelona de Tàpies són només «en paper».
- **Arquitectes i estudis**: termes de la taxonomia Hugo — els noms que surten al camp `arquitectes` de les fitxes (i les fitxes curades de `/arquitectes/`).
- **Anys d'arquitectura**: 1928 és un valor editorial fix (hi ha masies anteriors — debat intern de l'equip); el segon any és l'any en curs.

## Referències del contingut

- Fitxes d'element: **660** (amb publicacions: 660; esborranys: 0)
- Amb coordenades: **659** — sense: 1 (flors-de-la-rambla.md)
- Noms d'arquitecte a les fitxes: **274** · pàgines de publicació creades: 13

## Històric (últims 14 dies)

| Data | Edificis | Guies | Arquitectes | Anys |
|---|---|---|---|---|
| 2026-09-01 | 659 | 13 | 274 | 1928–2026 |

---

*Generat per `scripts/verifica-numeros-web.py` (execució diària automàtica). Cap xifra de la portada no és hardcoded: totes es calculen al build; això verifica que el que es publica coincideix amb el contingut.*
