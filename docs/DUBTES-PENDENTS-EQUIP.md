# Dubtes pendents per comentar amb l'equip d'El Globus Vermell

**Data:** 2026-07-27
**Propòsit:** Recull de preguntes obertes acumulades durant la migració WordPress → Hugo, per revisar en una reunió/comentari amb l'equip (Xavi, Jorge). No són bloquejos tècnics — són decisions de producte/contingut que necessiten la seva opinió.

---

## 1. Correspondència entre "publicacions" (en paper) i categories del mapa

**Verificat avui:** el menú hamburguesa del WordPress en viu té exactament **11 categories** (les que corresponen a guies amb edificis geolocalitzats):

1. Arquitectura d'avantguarda. 1928-1939
2. Arquitectura Moderna. 1950-1975
3. De l'esperança a la crisi. 1975-2008
4. La revolució tranquil·la. 2010-2025
5. Mercats
6. Biblioteques
7. Masies
8. Eixample: Jardins interiors d'illa
9. Poblenou: Patrimoni industrial
10. Barceloneta: Arquitectura i art públic
11. La Marina del Port i del Prat Vermell

Al Hugo, la secció "En paper" en té **13**: les 11 anteriors + **"New Babylon Barcelona"** i **"La Barcelona de Tàpies"**. Aquestes dues ja estan marcades a `data/publicacions.yaml` com a itineraris d'art (`camps: null`) que no segueixen l'esquema d'edifici — i, en efecte, **no apareixen enlloc al menú/mapa del WordPress actual**.

**Pregunta per l'equip:** New Babylon i Tàpies són publicacions purament "en paper" (llibre/itinerari imprès, sense pins al mapa interactiu), o s'espera que en algun moment tinguin la seva pròpia capa al mapa com la resta? Si mai hi ha d'haver pins, calen edificis/parades geolocalitzades per aquestes dues guies — actualment no n'hi ha cap al WordPress.

---

## 2. Accés a la "pàgina final" de cada categoria/sub-mapa des del mapa

Cada categoria té una pàgina pròpia d'introducció editorial (els "Textos", p. ex. *"La revolució tranquil·la 2010-2025"*, *"Mercats de Barcelona"*...). Al mapa interactiu, ara mateix no hi ha una via clara per accedir-hi des del botó/capa de categoria.

**Opcions a valorar:**
- Icona "i" (informació) a cada botó de categoria/capa → obre la pàgina introductòria.
- Accedir-hi des del menú "En paper" únicament (sense enllaç directe des del mapa).
- Un tap/clic llarg sobre el nom de la capa a la llegenda del mapa.

**Restricció clau: mobile-first.** La solució ha de ser còmoda amb el dit en pantalles petites — evitar hover-only, textos petits o zones de tap massa reduïdes. Cal decidir quin patró volem abans de dissenyar-ho.

---

## 3. Imatges pendents dels edificis

Estat actual (verificat 2026-07-27, extret directament del dump de la base de dades de WordPress, no d'un crawling — veure metodologia a `scripts/images-from-dump.py`):

| | Quantitat |
|---|---|
| Edificis amb foto | 209 / 656 |
| Edificis sense foto (total) | 447 / 656 |
| ...dels quals: **confirmat que no tenen cap imatge pujada a WordPress** | 443 |
| ...dels quals: no s'han pogut aparellar amb cap post de WP (estat desconegut) | 4 |

Llistat complet, element per element, amb publicació i estat: `docs/images-pendents.md`.

Els 443 no és un problema tècnic: **simplement no tenen cap imatge pujada al WordPress**. Per completar-los caldria que algú de l'equip pengi fotos noves (a WordPress o directament al Hugo).

**Pregunta per l'equip:** qui s'encarrega de buscar/pujar aquestes ~443 fotos? Té sentit prioritzar per guia (p. ex. completar primer Marina o Biblioteques, que ja tenen bona part fotografiada — 80% i 72% respectivament — enfront de Masies, amb només un 2%)?

Els 4 casos sense aparellar (probablement canvis de nom/slug al WordPress):
- `casa-unifamiliar`
- `edifici-dhabitatges-carrer-navas`
- `jardins-dagusti-centelles`
- `placa-dolors-piera-isabel-vila`

Caldria revisar-los a mà al WordPress per confirmar si encara existeixen amb un altre nom.

---

## 4. Accés i gestió del servidor

- **DNS del domini**: pendent decidir si el gestiona en Joan (migrant-lo a Dinahosting) o en Jorge des de joker.com. Ara mateix no s'ha tocat res.
- **Accés SSH des de casa**: només configurat des d'un ordinador fins ara. Pendent replicar-ho des de l'altre.
- **WP Cerber** (plugin de seguretat del WordPress) bloqueja qualsevol accés automatitzat a pàgines renderitzades, independentment de la IP d'origen — val la pena que l'equip tècnic ho sàpiga per si cal alguna vegada fer excepcions puntuals per feina legítima (nosaltres ho hem resolt treballant directament amb els dumps de la BD, sense tocar les pàgines en viu).
- **`/var/www/my_webapp`**: Jorge no estava segur de què era (backup/import antic?) — pendent de confirmar si es pot eliminar o s'ha de conservar.

---

## 5. Reconciliació de recomptes (ja resolt, per registre)

El dubte original sobre els recomptes 564/671/656 ja està resolt (veure `docs/AUDITORIA-RECONCILIACIO-EDIFICIS.md`): 671 és el WordPress en viu (660 edificis + 11 textos editorials), 656 és el Hugo estàtic — 4 edificis per darrere de producció, pendents de sincronitzar.

---

## Resum de decisions que necessitem de l'equip

- [ ] New Babylon / Tàpies: publicació en paper només, o futura capa de mapa?
- [ ] Patró d'accés a la pàgina d'introducció de cada categoria des del mapa (icona "i", altra via)
- [ ] Qui s'encarrega de les ~443 fotos pendents, i amb quina prioritat
- [ ] DNS: qui el gestiona a partir d'ara
- [ ] Confirmar què és `/var/www/my_webapp` al servidor
