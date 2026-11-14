# Mail final a Xavi — 14 de novembre 2026

---

Bon dia, Xavi,

He revisat totes les observacions que has enviat dels dos últims mails. Són molt útils i concretes. He analitzat cada punt — on està el problema, per què passa, com ho solventarem i quins riscos de regressió podríem tenir. Tot sense tocar res del projecte. Et deixo explicat punt per punt.

La **pèrdua de dades del llistat d'arquitectes** és el que més ens preocupa ara mateix. Et l'adreso primer.

---

## 1. PÈRDUA DE DADES: Llistat d'arquitectes esborrat

El llistat que havies començat a fer dels 92 arquitectes orfes va desaparèixer i has hagut de tornar a começar.

**Per què probablement ha passat:**
- L'editor de Sveltia pot tenir un buffer temporal que no es desa si la sessió es tanca malament
- Els canvis potser no estaven guardats al servidor en una actualització automàtica
- Possiblement hi ha un bug de persistència de dades que no estàvem monitoritzant

**Com ho solventarem:**
Dilluns investigarem on exactament es guarden les dades mentre estàs editant. Veurem si hi ha un historial o backup que recuperar. Crearem un protocol perquè en el futur facis backup dels llistats importants (exportar a Markdown localment, por exemple). Si l'editor de Sveltia no té suficient robustesa per a aquesta tasca, ho avaluarem.

**Impacte i risc:**
Crítico. No podem perdre treball. Però la solució és procedimental, no canvis de codi que trenquin altra cosa.

---

## 2. Canviar nom d'edifici/element — passa alguna cosa?

N'has canviat uns quants i et preguntes si trencarà algo.

**Per què pot passar:**
Els links interns poden funcionar de dues maneres: usant el nom (slug) de l'element, o usant un ID intern. Si usen slug, renombrar-lo trencarà els links. Si usen ID, els links seguiran funcionant.

**Com ho solventarem:**
Dilluns verificarem exactament com estan implementats els links. Si has canviat noms i algo s'ha trencat, ho corregim. Documentarem la regla per a futures reanomenacions.

**Impacte i risc:**
Baix. Si es necessita arreglament, és local als elements que has canviat.

---

## 3. Intervencions: afegir tipus "ús actual" i "nom actual"

Seria útil poder especificar no només la intervenció, sinó també l'ús actual o nom actual de l'edifici.

**Per què és útil:**
Molts edificis han canviat de funció o de nom, i això és informació important per als visitants.

**Com ho solventarem:**
Dilluns parlarem amb El Globus Vermell sobre quins tipus d'intervencions necessiteu exactament. Possiblement ampliar la llista: construcció, reforma, ús actual, nom actual, etc. Decidir si és un dropdown de opcions fixes, o si permet afegir-ne de noves.

**Impacte i risc:**
Medi. Comporta canviar el schema de dades (editor + frontmatter). Si es fa correctament, sense trencar intervencions existents, és segur. Cal verificació completa post-canvi.

---

## 4. Disposició visual quan no tenim arquitecte

Quan una intervenció no té arquitecte assignat, el layout es desplaça i es veu trencat.

**Per què passa:**
Probable: el CSS de `.fitxa-dada` (estil de les files d'informació a la fitxa) no maneja bé les cel·les buides o falta spacing.

**Com ho solventarem:**
Revisar el CSS de `.fitxa-dada` en `main.css`. Assegurar que funciona igual si hi ha arquitecte o no. Testejar fitxes sense arquitecte (per exemple, obres d'art on no hi ha arquitecte, només autoria).

**Impacte i risc:**
Baix-medi. CSS simple, però afecta moltes fitxes. Cal verificar visually que no canviem cap altra cosa.

---

## 5. Format de text disparell

Alguns elements tienen format inconsistent (HTML mix amb Markdown mix amb text pla).

**Per què passa:**
Migració de WordPress amb formats barrejats, o l'editor genera formats diferents segons l'entrada.

**Com ho solventarem:**
Audit: verificar tots els camps de text (descripció, intervencions, etc.). Estandaritzar a un format (preferiblement Markdown). Assegurar que el template renderitza correctament.

**Impacte i risc:**
Alt. Afecta 310+ fitxes. Cal audit complet i verificació post-migració. Però si es fa correctament, no trenca res.

---

## 6. Llistat d'edificis a publicacions no apareix (GATCPAC)

A GATCPAC no surt el llistat d'edificis. Mostra: "Encara no hi ha fitxes d'elements importades per aquesta publicació."

**Per què passa (possibles causes):**
1. GATCPAC potser no té elements associats a ella
2. Els elements sí que tienen `publicacions: [gatcpac]`, però el template no els trova per algun motiu

**Com ho solventarem:**
Dilluns farem audit: quants elements tienen `publicacions: ["gatcpac"]` al seu frontmatter? Si en té, debugarem per què no apareixen. Si no en té, és comportament correcte (mostra "sense fitxes").

**Impacte i risc:**
Molt baix. Probablement issue de dades, no de codi.

---

## 7. Línia vertical a esquerra de biografies d'arquitectes

La línia blava (o del color accent) a l'esquerra de cada biografia no agrada.

**On està exactament:**
CSS `main.css`, línia 601, classe `.arquitecte-bio`

```
border-left: 3px solid var(--color-accent);
```

**Per què la tenim:**
Element de disseny visual com a accent / decoració a les biografies.

**Com ho solventarem:**
Eliminar aquesta línia CSS. La solució és una sola línia.

**Impacte i risc:**
Molt baix. Es trenca res, és purament estètic. Cal screenshot before/after per confirmar.

---

## 8. Línia vertical a llistat d'arquitectes + falta de compacitat

Quan es llisten elements amb els seus arquitectes, surt una línia vertical. A més, les tres informacions (nom element, adreça, arquitectes) està molt separades.

**On està exactament:**
CSS `main.css`, línies 1273-1289, classe `.llistat-element-arquitectes`

```
border-left: 2px solid var(--color-border, #e0e0e0);
padding-left: 1.5rem;  <-- causa separació
```

**Per què passa:**
Línia decorativa lateral + padding excessiu causa espai.

**Com ho solventarem:**
Eliminar `border-left: 2px`. Reduir `padding-left` (actualment 1.5rem, podria ser 0.5rem). Ajustar `margin-top` per compactat. La solució és 2-3 línies CSS.

**Impacte i risc:**
Baix. CSS simple. Cal verificar visually que la compacitat millora sense perdre legibilitat.

---

## 9. Arquitecte a llistat no porta a fitxa individual

Quan cliques en un arquitecte dins d'un llistat d'elements, no vas a la fitxa de l'arquitecte (exemple: `/arquitectes/josep-lluis-sert-i-lopez/`), sinó a la pàgina general `/arquitectes/`.

**On està exactament:**
JavaScript `mapa.js`, línia 1084

```javascript
arqLink.href = arqUrls[idx] || ((window.SITE_BASE || '/') + 'arquitectes/');
```

Quan `arqUrls[idx]` és undefined (no existeix URL per a aquell arquitecte en l'array), fa fallback a `/arquitectes/` general.

**Per què passa:**
Possible mismatch entre el nombre de noms d'arquitectes i el nombre d'URLs generades.

**Com ho solventarem:**
Generar la URL en JavaScript si `arqUrls[idx]` és undefined (usant la mateixa lògica que Hugo fa). O assegurar que `arqUrls` sempre coincideix exactament amb `arquitectes` (verificar template).

**Impacte i risc:**
Baix. El JavaScript pot generar la URL en temps real sense problemes. Cal testejar que 20-30 clicks d'arquitectes van al lloc correcte.

---

## 10. Canvi copiar portada

Frasse actual: "Una eina crítica per llegir Barcelona a través de la seva arquitectura, l'art..."

Canvi: "Una eina crítica per llegir Barcelona a través de l'arquitectura, l'art..." (eliminar "seva")

**On està:**
`content/ca/_index.md`, línia 3 — el camp `tagline`

**Com ho solventarem:**
Canvi directe, una paraula.

**Impacte i risc:**
Nul. Canvi purament de contingut, sense dependències.

---

## 11. Franja color + text negre a temes/publicacions

Apareix una franja de color (exemple: blau a Biblioteques) dalt de la pàgina de la publicació. El títol no és completament negre.

**On està exactament:**
CSS `main.css`, línies 2392-2406

```
.publicacio-banda {
  background: var(--pub-color, var(--color-accent));  <-- franja
}

.publicacio-cap h1 {
  color: color-mix(in srgb, var(--pub-color, var(--color-text)), #000 45%);
                                                                       <-- no és 100% negre
}
```

**Per què passa:**
El color-mix barreja el pub-color (blau, verd, etc.) amb negre al 45%, resultant en un gris-azulat o gris-verdós, no negre pur.

**Com ho solventarem:**
Canviar el color h1 a `#000` (negre pur). Decidir si mantenir la franja de color o eliminar-la. Cal verificar contrast WCAG si canviem.

**Impacte i risc:**
Baix. CSS simple. Però es tracta d'una decisió de disseny, així que necessita aprovació del client (El Globus Vermell).

---

## 12. Enllaços relacionats: selecció i estètica

Primers, no saps com estan triats els enllaços relacionats que surten sota del plànol.
Segons, quan el nom de l'element és molt llarg, la fila es trenca estèticament.

**Per què passa:**
Probablement hi ha una lògica de selecció (automàtica o manual) que genera els relacionats. I el CSS potser no maneja bé text llarg (falta word-wrap o overflow handling).

**Com ho solventarem:**
Dilluns documentarem com es seleccionen els relacionats exactament. Revisar CSS per veure com es comporta el text long (truncar, wrap, reduir font, etc.). Decidir quin comportament és millor amb El Globus Vermell.

**Impacte i risc:**
Baix. Possiblement pure CSS fix, aïllat a aquest component.

---

## RESUM

He analitzat cada punt de manera que entenem exactament:
- Què està malament i per què
- On està el codi (línies exactes)
- Com ho solventarem sense trencar altra cosa
- Quins riscos de regressió podríem tenir
- Quines verificacions cal fer post-fix

Tot documented sense tocar absolutament res del projecte. Els punts críticos (link arquitecte, pèrdua de dades) es prioritzen. Els canvis de disseny (línies CSS, text negre) es fan amb aprovació del client. La resta es fan quan tingui sentit.

---

## DILLUNS A NAU BÒSTIK (10:00)

Podem revisar en pantalla tots aquests punts, validar que el nostre análisis de causes és correcte, i prioritzar l'ordre de fixatge. Així mateix, pots confirmar quins dels canvis de disseny te semblen correctes.

Jo tinc que sortir al dentista a les 13, però tornaré sobre les 5. Si et va bé aquesta hora dilluns?

Seguim!

