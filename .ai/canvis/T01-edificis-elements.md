# T01 — Terminologia: "edificis" → "elements"

**Data:** 2026-09-30
**Estat:** Aplicat

## Motiu

El projecte documenta edificis, espai públic i obres d'art. El terme "edificis" excloïa dues categories. El terme correcte és "elements".

## Abast

Canvis només al text visible per l'usuari (etiquetes, botons, frases UI, atributs aria). No s'han tocat noms de variables internes de codi (Go, JavaScript, CSS).

---

## Canvis aplicats

### `themes/guiesbcn-elglobusvermell/layouts/404.html`

**Línia 13**
```
- Mapa dels edificis
+ Mapa dels elements
```

**Línia 14**
```
- Cerca un edifici al llistat alfabètic
+ Cerca un element al llistat alfabètic
```

---

### `themes/guiesbcn-elglobusvermell/layouts/publicacions/term.html`

**Línia 24**
```
- Encara no hi ha fitxes d'edificis importades per aquesta publicació.
+ Encara no hi ha fitxes d'elements importades per aquesta publicació.
```

---

### `themes/guiesbcn-elglobusvermell/layouts/arquitectes/term.html`

**Línia 55** (atribut aria-label, llegit per lectors de pantalla)
```
- aria-label="Mapa d'edificis de [nom arquitecte]"
+ aria-label="Mapa d'elements de [nom arquitecte]"
```

---

### `themes/guiesbcn-elglobusvermell/layouts/index.html`

**Línia 88** (xifres de la portada)
```
- edificis documentats
+ elements documentats
```

**Línia 122** (bloc guia destacada)
```
- Un edifici de la guia
+ Un element de la guia
```

**Línia 128** (botó guia destacada)
```
- Veure tots els edificis de la guia →
+ Veure tots els elements de la guia →
```

**Línia 145** (targetes de guia)
```
- [N] edificis
+ [N] elements
```

**Línia 160** (bloc arquitecte destacat)
```
- edificis documentats
+ elements documentats
```

**Línia 162** (botó arquitecte destacat)
```
- Veure tots els edificis →
+ Veure tots els elements →
```

**Línia 173** (bloc recursos educatius)
```
- fitxes d'edificis
+ fitxes d'elements
```

**Línia 183** (bloc accés al mapa)
```
- El mapa, la porta d'entrada a tots els edificis
+ El mapa, la porta d'entrada a tots els elements
```

**Línia 212** (JavaScript — text dinàmic guia destacada)
```
- guia.count + ' edificis documentats'
+ guia.count + ' elements documentats'
```

---

## No modificat (intern, no visible)

- Variables Go: `$totalEdificis`, `$edificis`
- Claus de dades JS: `guia.edificis`, `var edifici`
- Classes CSS: `publicacio-edificis`, `pa-guia-dest-edifici`, etc.
- IDs HTML: `pa-dest-edifici`, `pa-dest-edifici-link`, etc.
- Comentaris de plantilla Go

---

## Fitxers modificats

- `themes/guiesbcn-elglobusvermell/layouts/404.html`
- `themes/guiesbcn-elglobusvermell/layouts/publicacions/term.html`
- `themes/guiesbcn-elglobusvermell/layouts/arquitectes/term.html`
- `themes/guiesbcn-elglobusvermell/layouts/index.html`
