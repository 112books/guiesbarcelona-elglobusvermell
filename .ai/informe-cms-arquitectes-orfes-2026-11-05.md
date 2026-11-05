# Informe — Arquitectes sense fitxa (punts 1, 2 i 3 del mail d'en Xavi)

**Data:** 5/11/2026 (tarda)
**Estat:** anàlisi feta · pla aprovat per Joan (opció A amb llista de verificació) · **cap canvi de dades aplicat encara**
**Relacionat:** `docs/2026-11-05-mail-xavi-fitxes-i-questionari.md` (triatge) · `docs/2026-11-05-mail-resposta-xavi.md` (resposta enviada 17:36) · `REGISTRE-CANVIS-FITXES.md` #17

---

## 1. Els tres punts, en paraules d'en Xavi

1. **El camp «Arquitectes» ha desaparegut** de les fitxes.
2. **Un cop afegida una intervenció, no se'n pot editar cap camp.**
3. **Arquitectes fantasma que no es poden esborrar** (ex.: Biblioteca Arús, «Bassegoda i Musté» i «Amigó»).

La hipòtesi de treball (encara no confirmada a l'editor) és una de sola per als tres punts: el camp és un `relation` de Sveltia amb `value_field: title`. **Un nom que no coincideix exactament amb el títol d'una fitxa d'arquitecte no es pot mostrar**, i per tant la fila es veu buida i no hi ha manera d'esborrar-lo des de l'editor.

## 2. Què s'ha pogut verificar avui

- **CI verd** del commit `aa31e0a2` (punt 4, fitxes d'arquitecte fantasma): `Deploy → Producció (GitHub Pages)` i `Accessibilitat (pa11y-ci)` en `success`.
- A staging: `/arquitectes/baas-arquitectura/` respon **200** amb la informació bona i `/arquitectes/baas/` respon **200** «Moguda».
- S'ha obert l'editor (Sveltia 0.224.0, staging) amb sessió de només lectura i s'ha carregat la fitxa de l'Arús, però **la inspecció del formulari va quedar a mitges** (la sessió es va tallar). La confirmació visual del punt 1 i del punt 2 queda pendent.

## 3. Mesura del problema (dades del web, 5/11/2026)

| Concepte | Valor |
|---|---|
| Fitxes d'element | 658 |
| Fitxes d'arquitecte | 277 |
| Noms d'arquitecte **sense fitxa** | **188 noms diferents** |
| Fitxes d'element afectades | **204** |

Repartiment per camp:

| Camp | Valors | Orfes | Noms orfes diferents |
|---|---|---|---|
| `arquitectes` | 505 | 38 | 26 |
| `intervencions[].autors` | 341 | 203 | 169 |

**12 fitxes tenen tots els noms orfes** al camp `arquitectes`: són les que es veuen completament buides a l'editor.

## 4. Classificació dels 188 noms (per triar el pla)

| Grup | Noms | Usos | Feina |
|---|---|---|---|
| Es resolen sols contra una fitxa existent (variant, typo, «A + B», any enganxat) | **96** | 126 | Renombrar. Cap decisió |
| Necessiten decisió (fitxa nova, un altre nom, o no és arquitecte) | **92** | 107 | Llista per validar |

## 5. Regressió detectada (efecte del punt 4)

La fusió de duplicats de `aa31e0a2` va esborrar dues fitxes (`josep-soteras-i-mauri` i `lorenzo-garcía-barbón`) i **deu referències dels edificis apunten encara a aquells títols**:

- `Josep Soteras i Mauri` → 9 referències a 7 fitxes (camp-nou, conjunt-del-congres-eucaristic, hispano-olivetti, palau-municipal-desports, poligon-montbau…).
- `Lorenzo García-Barbón` → 1 referència (camp-nou).

Des del desplegament, aquests arquitectes no enllacen a la fitxa. Cal canviar la referència al títol bo (`Josep Maria Soteras i Mauri`, `Llorenç García-Barbón Fernández de Henestrosa`): no crea ni esborra res.

## 6. Pla aprovat per Joan: opció A amb llista de verificació

L'opció B (que en Xavi netegi a mà) es descarta: la feina és **revisar una llista**, no tocar 204 fitxes.

- **Fase 0 — Desfer la regressió del punt 4.** Renombrar les 10 referències òrfenes al títol fusionat. Sense fitxes noves.
- **Fase 1 — Els 96 automàtics.** Renombrar als títols existents (variants i combinacions «A + B + C» que se separen en noms que ja tenen fitxa). Es registra al `REGISTRE-CANVIS-FITXES.md` com a correcció, sense altes.
- **Fase 2 — La llista per a en Xavi.** Pàgina al tauler (`/admin/revisio/`): una fila per nom amb *com surt al web · en quants edificis (amb enllaç per obrir-los) · proposta (crear fitxa / vol dir aquesta altra / no és arquitecte) · casella de validació*. **Ell no toca cap fitxa.**
- **Fase 3 — Aplicar el validat.** Crear només les fitxes que calguin (alta autoritzada per Joan, registrada a `REGISTRE-CANVIS-FITXES.md`).
- **Fase 4 — Xarxa de seguretat al CMS.** Que l'editor mostri sempre els noms sense fitxa (encara que no es puguin triar), perquè no torni a «desaparèixer» res ni es perdi en desar.

## 7. Pendents

- [ ] Confirmar a l'editor el comportament del camp `relation` amb noms orfes (punt 1) i de les intervencions (punt 2).
- [ ] OK de Joan per començar Fase 0 + Fase 1.
- [ ] Filtrar la llista de la Fase 2 abans de publicar-la al tauler.
- [ ] Punt 5 (filtre del mapa): espera la prova de Joan a staging i saber navegador i pàgina d'en Xavi.

## 8. Fitxers

- `pla-arquitectes-orfes-2026-11-05.json` — classificació completa (96 resolts amb el títol destí + 92 pendents amb els fragments que cal decidir).
