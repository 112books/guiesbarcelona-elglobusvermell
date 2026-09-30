# T02 — Ordre del menú de navegació

**Data:** 2026-09-30
**Estat:** Aplicat

## 1. Tasca demanada

> "L'ordre del menú hauria de ser: Presentació, Mapa, En paper, Arquitectes, Contacte"

Font: correu Xavi, secció GENERAL, feedback 30/9/2026.

## 2. Solució prevista

Modificar els valors `weight` al fitxer de configuració del menú (`config/_default/hugo.toml`). Canvi de dades pur, sense tocar plantilles HTML.

## 3. Estat de l'execució

Aplicat el 2026-09-30.

## 4. Fitxers modificats

### `config/_default/hugo.toml`

**Abans:**
```toml
[[languages.ca.menus.main]]
  name   = "Mapa"
  url    = "/mapa/"
  weight = 1

[[languages.ca.menus.main]]
  name   = "Presentació"
  url    = "/presentacio/"
  weight = 2
```

**Després:**
```toml
[[languages.ca.menus.main]]
  name   = "Presentació"
  url    = "/presentacio/"
  weight = 1

[[languages.ca.menus.main]]
  name   = "Mapa"
  url    = "/mapa/"
  weight = 2
```

Els ítems En paper (3), Arquitectes (4) i Contacte (5) no han canviat.

## 5. Resultat final

Ordre nou: Presentació · Mapa · En paper · Arquitectes · Contacte

## 6. Aprovació

Pendent de validació Xavi.
