# T03 — Menú sempre en text al desktop, sense icones en fer scroll

**Data:** 2026-09-30
**Estat:** Aplicat

## 1. Tasca demanada

> "A la web no ens agrada que el menú es converteixi en icones quan fas scroll. Preferim que sigui sempre text. Al mòbil ja entenem que seran les icones."

Font: correu Xavi, secció GENERAL, feedback 30/9/2026.

Nota: Joan no comparteix el criteri (prefereix el comportament compacte en scroll), però s'aplica per decisió del client.

## 2. Solució prevista

Eliminar les 2 regles CSS que en estat `is-scrolled` amagaven el text del menú i mostraven les icones al desktop. El comportament de mòbil (icones sempre) es manté intacte via media query pròpia.

## 3. Estat de l'execució

Aplicat el 2026-09-30.

## 4. Fitxers modificats

### `themes/guiesbcn-elglobusvermell/assets/css/main.css`

**Eliminades les línies 205-206:**
```css
/* ELIMINAT */
.site-header.is-scrolled .nav-label { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0,0,0,0); white-space: nowrap; border-width: 0; }
.site-header.is-scrolled .nav-icon  { display: flex; }
```

**No modificat (comportament mòbil, correcte):**
```css
@media (max-width: 36rem) {
  .nav-label { position: absolute; ... }  /* icones al mòbil, sempre */
  .nav-icon  { display: flex; }
}
```

El JavaScript de `main.js` no s'ha tocat: la classe `is-scrolled` es continua afegint en scroll (controla alçada del header i mida del logo), però ja no amaga el text del menú.

## 5. Resultat final

- Desktop: text del menú sempre visible, tant en repòs com en scroll.
- Mòbil (≤576px): icones sempre visibles (comportament original preservat).

## 6. Aprovació

Pendent de validació Xavi.
