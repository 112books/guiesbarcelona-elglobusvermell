# Full de ruta — Guies Barcelona (migració WordPress → Hugo)

**Creat:** 2026-07-28
**Propòsit:** document viu de seguiment del projecte. Llista totes les tasques pendents, una a una, amb casella per marcar-les i un registre del temps dedicat. Pensat perquè qualsevol persona o IA (Claude o una altra) pugui agafar el projecte des d'aquí sense necessitar context previ.

---

## Protocol per a cada tasca

Cada tasca de desenvolupament (no les purament de decisió/espera) segueix aquests 5 passos abans de donar-se per tancada:

1. **Pensar** — entendre el problema, mirar alternatives si n'hi ha.
2. **Desenvolupar** — implementar-ho.
3. **Verificar** — comprovar que funciona de veritat (no assumir-ho).
4. **Vist-i-plau del client** — ensenyar-ho a Xavi/Jorge i esperar confirmació explícita.
5. **Marcar com a feta** — només un cop passat el pas 4.

Una tasca sense el vist-i-plau del client (pas 4) es queda com **"fet tècnicament, pendent de validació"**, no com a tancada.

### Llegenda de caselles
- `[ ]` pendent de començar
- `[~]` en curs / fet tècnicament, pendent de vist-i-plau
- `[x]` fet i validat pel client

---

## Historial (fins al 28 jul 2026)

Registre real basat en els commits de git (dates i hores exactes; el "temps dedicat" és una estimació a partir del primer i l'últim commit de cada sessió, no temps de feina pur).

| Data | Franja horària | Temps aprox. | Què es va fer |
|---|---|---|---|
| 2026-07-22 | 16:23–16:44 | ~20 min | Auditoria de reconciliació de recomptes d'edificis (564/671/656): anàlisi del dump SQL de febrer, taxonomia, coordenades. Document `AUDITORIA-RECONCILIACIO-EDIFICIS.md`. |
| 2026-07-23 | 13:09–17:30 | ~4h30 | Accés SSH al servidor (Hetzner/YunoHost), dump fresc de producció, confirmació del recompte 671, primer script de descàrrega d'imatges (bloquejat per WP Cerber a mitja tarda). |
| 2026-07-23 | 20:46 | ~15 min | Ajustos manuals (Joan): fix de categories, mode local anti-Cerber, 166 fotos noves. |
| 2026-07-24 | 11:05 | — | Actualització manual de la pàgina "Crèdits" (no relacionat amb sessions de Claude). |
| 2026-07-27 | 13:20–14:59 | ~1h40 | Nou mètode de descàrrega d'imatges via dump SQL (esquiva Cerber del tot), verificació exhaustiva del recompte de fotos (443 confirmades sense imatge), documents de dubtes pendents i mail de presentació a Xavi. |
| 2026-07-28 | 11:47–17:32 | ~5h45 (amb pauses) | CMS: títol/logo personalitzats, targeta i guia de "Gestió d'usuaris", colors del CMS escalfats cap al vermell de marca, camp "Fotografia" afegit al formulari d'edificis (no existia — per això no es veia a l'editor). |

**Temps total aproximat invertit fins ara: ~12h30.**

---

## Setmana actual — 28 jul al 3 ago 2026

### En curs / fet tècnicament, pendent de vist-i-plau
- [x] Mail de primera presentació enviat a Xavi (2026-07-27) — **esperant resposta** sobre: direcció estètica, navegació del mapa (icona "i"), New Babylon/Tàpies, capçalera/peu.
- [~] CMS personalitzat (logo, títol, colors, gestió d'usuaris, camp de fotografia) — fet i verificat tècnicament, **pendent que Joan el faci servir uns dies i confirmi que tot rutlla**.

### Pendents d'aquesta setmana
- [ ] **1.** Revisar `admin-editor/` i `static/admin/config.yml` (arrel) — semblen configuracions de CMS antigues i òrfenes (no enllaçades enlloc). Decidir si s'eliminen.
      *Protocol: pensar (confirmar que no s'usen) → esborrar → verificar que el hub segueix funcionant → no cal vist-i-plau de client (és neteja interna) → marcar fet.*
- [ ] **2.** Confirmar què és `/var/www/my_webapp` al servidor (Jorge no ho tenia clar).
      *Protocol: preguntar a Jorge → si és brossa, proposar eliminar-lo → vist-i-plau de Jorge abans de tocar-hi → marcar fet.*
- [ ] **3.** Rèplica de l'accés SSH des de l'ordinador de casa de Joan (ara només funciona des d'un Mac).
      *Protocol: Joan afegeix la clau pública de l'altre ordinador → Jorge (o Joan amb accés root) l'afegeix a `authorized_keys` → verificar connexió → marcar fet.*

---

## Setmanes següents — condicionades a la resposta de Xavi

Les tasques d'aquí depenen de les 4 confirmacions demanades al mail de presentació. Mentre no arribi resposta, es pot avançar en paral·lel amb feina que no depèn d'aquestes decisions (marcada "no bloquejada").

### 4 ago – 10 ago 2026 (o quan Xavi respongui, el que sigui més tard)

- [ ] **4.** Implementar l'accés a la pàgina de cada submapa des del mapa general (icona "i" o l'alternativa que Globus prefereixi). *Bloquejada — depèn de la resposta.*
- [ ] **5.** Resoldre New Babylon i Tàpies: si han de tenir capa pròpia al mapa, caldrà geolocalitzar-ne els punts (avui no en tenen cap). *Bloquejada.*
- [ ] **6.** Revisar contingut de "Presentació" i "Crèdits" segons el que digui Globus. *Bloquejada.*
- [ ] **7.** Footer: decidir CC vs © i mailto vs formulari de contacte, i aplicar-ho. *Bloquejada.*
- [ ] **8.** Confirmar signatura "LinuxBCN" al footer (Globus no hi hauria de tenir objecció, però cal el sí explícit). *Bloquejada.*

**No bloquejades (es poden fer en paral·lel):**
- [ ] **9.** Completar fotografies pendents (443 edificis sense imatge a WordPress). Requereix que algú de Globus pengi fotos noves a WordPress; un cop pujades, tornar a córrer `scripts/images-from-dump.py` amb un dump fresc.
      *Protocol: Globus puja fotos → Joan/Claude fa dump fresc + executa script → verificar quantes noves s'han enllaçat → informar Globus → marcar fet quan arribi a ~100%.*
- [ ] **10.** Resoldre els 4 edificis sense aparellar amb cap post de WP: `casa-unifamiliar`, `edifici-dhabitatges-carrer-navas`, `jardins-dagusti-centelles`, `placa-dolors-piera-isabel-vila`.
      *Protocol: cercar-los manualment al WordPress (potser slug canviat) → si es troben, aparellar-los i comprovar foto → si no existeixen, preguntar a Globus si cal crear-los o eliminar-los del Hugo → marcar fet.*

### 11 ago – 17 ago 2026 (estimat)

- [ ] **11.** Sincronitzar el Hugo estàtic amb la producció de WordPress: hi ha 4 edificis publicats a WP que encara no existeixen com a fitxa al Hugo.
      *Protocol: identificar quins 4 (comparar dump vs `content/ca/elements/`) → crear-ne les fitxes amb `scripts/importa-edificis-wp.py` → verificar que apareixen al mapa amb coordenades correctes → vist-i-plau de Joan → marcar fet.*
- [ ] **12.** Decidir gestió del DNS (Joan el migra a Dinahosting, o el porta Jorge des de joker.com) i executar-ho.
      *Protocol: decisió → si el porta Joan, crear compte Dinahosting i moure zona DNS → verificar propagació i que el web segueix accessible → marcar fet.*

---

## Aparcat (baixa prioritat, sense data)

- [ ] Traduir la interfície del CMS (Sveltia) al català ("New", "Group", "Filter", "Sort"...). Investigat: el català **no existeix** com a idioma nadiu del CMS; caldria un pedaç JS fràgil que es podria trencar amb cada actualització del CMS. Es deixa aparcat fins que hi hagi més interès o Sveltia l'afegeixi de sèrie.
- [ ] Preparar tasques mecàniques (descàrrega d'imatges, etc.) perquè les faci OpenCode en lloc de Claude, per estalviar tokens. Ja hi ha un precedent (`scripts/download-images-elements.py` es va deixar preparat per OpenCode, encara que finalment es va haver de substituir per l'enfocament de dump per l'Cerber).

---

## Com continuar aquest document

- Quan es comenci una tasca nova que no hi sigui, afegir-la amb el mateix format (número, casella, protocol).
- Quan es tanqui una tasca del tot (pas 5, vist-i-plau inclòs), moure-la de la secció de pendents a l'Historial, amb data i temps dedicat.
- Revisar setmanalment si cal reprojectar les setmanes següents (Les dates són estimacions, no compromisos ferms).
