# Duplicats de migració — diagnosi i proposta

Data: 2026-10-01
Abast: fitxes d'element duplicades detectades durant la migració del WordPress.
Regla ferma del projecte: **cap discrepància no es resol esborrant**. Cal corregir
o afegir contra el WordPress en producció abans de tocar res.

Aquest document recull els tres casos oberts i una acció recomanada per a cada un.
Cap acció destructiva no s'ha aplicat encara.

---

## 1. Navas 238 / 240 / genèrica

Fitxers:

- `content/ca/elements/edifici-dhabitatges-carrer-navas-238.md`
  - adreca: Navas de Tolosa, 238
  - any: 1931
  - arquitectes: Juan José Olazabal
  - lat/long: 41.4134026 / 2.1895928
- `content/ca/elements/edifici-dhabitatges-carrer-navas-240.md`
  - adreca: Navas de Tolosa, 240
  - any: 1931
  - arquitectes: Joan Baca
  - lat/long: 41.4135148 / 2.1895829
- `content/ca/elements/edifici-dhabitatges-carrer-navas.md` (genèrica)
  - adreca: C. de las Navas de Tolosa, 240
  - any: 1931
  - arquitectes: Juan José Olazabal
  - lat/long: 41.4134713 / 2.1894638
  - publicacions: gatcpac

Diagnosi: la fitxa genèrica és un **mal merge** de la 238 i la 240. Pren
l'adreça de la 240 però l'arquitecte de la 238, i la coordenada és intermèdia.
Les tres es renderitzen avui (cap consta com a invisible; la nota antiga deia
"invisible" i no és cert).

Acció recomanada (pendent de confirmació):

1. Mantenir 238 i 240 com a fitxes canòniques (són dos edificis reals i
   diferenciats, tal com els llista el client).
2. Eliminar la genèrica del contingut i reaprofitar el seu URL amb un
   `aliases` a la fitxa 240 (o a la 238, segons quin edifici sigui el bo).
3. No esborrar cap dada: abans de retirar-la cal confirmar al WordPress en viu
   quin arquitecte i quina coordenada corresponen a cada número.

Decisió necessària: confirmar que la genèrica es pot redirigir i a quina de les
dues fitxes.

---

## 2. Casa unifamiliar (plaça Mons)

Fitxers:

- `content/ca/elements/casa-unifamiliar-placa-mons.md`
  - adreca: Pl. Mons / G. Bécquer
  - any: 1931
  - arquitectes: Ricard de Churruca, Germà Rodríguez Arias
  - lat/long: 41.4136086 / 2.1446363
- `content/ca/elements/casa-unifamiliar.md` (genèrica)
  - adreca: Pl. Mons / C. de G. Bécquer
  - any: 1931
  - arquitectes: Raimon Duran i Reynals
  - lat/long: **NaN / NaN**
  - publicacions: gatcpac

Diagnosi: mateixa adreça, **arquitectes diferents**. No és un duplicat net:
és un conflicte de dades. La genèrica té coordenades invàlides (NaN) i per això
no surt al mapa.

Acció recomanada (pendent de confirmació):

1. Verificar al WordPress viu quin arquitecte és el correcte (Churruca/Rodríguez
   Arias o Duran i Reynals).
2. Si és el mateix edifici, fusionar la dada bona dins `casa-unifamiliar-placa-mons`
   i redirigir la genèrica amb `aliases`.
3. Si són dos edificis diferents, completar la genèrica amb títol propi, adreça
   exacta i coordenades.

Decisió necessària: quin arquitecte i si són una o dues fitxes.

---

## 3. Pavelló de la República (CRAI UB)

Fitxers:

- `content/ca/elements/pavello-de-la-republica-de-1937-replica.md`
  - title: Pavelló de la República de 1937 (rèplica)
  - adreca: Av. del Cardenal Vidal i Barraquer, 34-36
  - any: 1937
  - arquitectes: Josep Lluís Sert, Luis Lacasa
  - lat/long: 41.4267353 / 2.1500109
  - publicacions: gatcpac
  - temes_transversals: art-public
  - foto: pavello-de-la-republica-de-1937-replica.jpg
- `content/ca/elements/pavello-de-la-republica-biblioteca-crai-ub.md`
  - title: Pavelló de la República - Biblioteca CRAI UB
  - adreca: (buida)
  - any: (buit)
  - arquitectes: (buits)
  - lat/long: 41.4306986 / 2.1513175
  - publicacions: biblioteques, gatcpac
  - districte: Horta-Guinardó
  - foto: pavello-de-la-republica-biblioteca-crai-ub.jpg
  - intervencions: el camp `any` conté tota la narració en lloc d'un any
    (frontmatter malmès)

Diagnosi: descriuen **el mateix edifici** (la rèplica de 1992 que acull el CRAI
Biblioteca del Pavelló de la República de la UB). La segona fitxa ve del plànol
de biblioteques i la primera del d'avantguarda. La segona té el frontmatter
malmès i li falten adreça, any i arquitectes; la primera és la correcta.

Acció recomanada (pendent de confirmació):

1. Fusionar a `pavello-de-la-republica-de-1937-replica`: afegir `biblioteques`
   a `publicacions`, afegir el `districte`, i reaprofitar la segona fotografia
   com a `fotos_addicionals`.
2. Conservar la narració de la intervenció (treure-la del camp `any` malmès i
   posar-la a `intervencions[].descripcio`).
3. Redirigir l'URL de la fitxa de biblioteca amb `aliases`.

Decisió necessària: confirmar la fusió i si es conserven les dues fotos.

---

## Estat

- Cap fitxa s'ha esborrat.
- Aquests tres casos queden **pendents de confirmació** de Joan i, si cal, de
  Xavi contra el WordPress en producció.
