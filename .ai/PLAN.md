# PLAN.md — Pla de treball actiu

Última actualització: 28 juliol 2026

---

## Estat actual (28 jul 2026)

### ✅ Completat avui

- Fitxes sense foto: eliminat placeholder "Imatge pendent", ara no es mostra cap imatge.
- Mapa: punts compartits entre publicacions dibuixats amb dos o més cercles de colors.
- Filtre de publicacions: tots els punts atenuats al iniciar, ressaltats al marcar una publicació.
- Enllaços des de la fitxa: corregit bug d'URL (absURL vs relURL) per al subpath de GitHub Pages.
- Taxonomia d'arquitectes activa: pàgina de llistat, pàgina individual per arquitecte amb mapa i edificis.
- Enllaços a arquitectes i publicacions des de la fitxa d'edifici.
- Llistat de punts desubicats generat amb proposta de geocodificació (`.ai/PUNTS-DESUBICATS.md`).
- Llistat d'arquitectes combinats a separar generat (`.ai/ARQUITECTES-A-SEPARAR.md`).
- Diccionari de normalització d'arquitectes duplicats per variants d'ortografia (`.ai/ARQUITECTES-NORMALITZACIO.yaml`).
- Pàgina de cada guia: secció de descàrregues PDF per idioma preparada.
- Mail de resposta definitiu a Xavi redactat (`docs/2026-07-28-mail-resposta-definitiu-xavi.md`).
- Deploy a staging (GitHub Pages) iniciat per Joan.

### ✅ Completat anteriorment (16 jul 2026)

- Estructura `.ai/` creada (PROJECT.md, ARCHITECTURE.md, PLAN.md, QUESTIONS-CLIENT.md)
- Clau SSH LinuxBCN generada (`~/.ssh/linuxbcn`) i pujada a GitHub
- 66 edificis importats del dump SQL a Hugo (gatcpac, interiors-illa, poblenou, mercats, biblioteques, 76-08, 09-25)
- Mapa Leaflet + OpenStreetMap amb marcadors de colors per publicació
- Filtres de mapa per publicació (llista plana, activables independentment)
- Logo de guiesbarcelona al header
- Pàgines estàtiques migrades del WordPress: Presentació, En paper (13 publicacions), Crèdits
- Navegació: Presentació / Mapa / En paper / Crèdits
- Fix subpath GitHub Pages (relURL/absURL)
- Deploy automàtic actiu a https://112books.github.io/guiesbarcelona-elglobusvermell/

---

## Blocants actius

### 🔴 Jorge — accés al servidor actual
Pendent que Jorge passi: host, usuari, ruta, clau SSH.
Desbloqueja: migració WordPress, contingut real (564 entrades), imatges, correu.

### 🔴 Google Maps API Key — URGENT (termini: setembre 2026)
La clau actual pertany a un compte d'alumnes que s'esborrarà al setembre.
Acció: Xavi ha de crear projecte Google Cloud i generar nova clau.

### 🟡 Disseny
Xavi debat internament: colors per publicació vs nou disseny de elglobusvermell.org.
No bloqueja el desenvolupament actual.

### 🟡 "Filtrar per publicacions" al mapa de l'app
Pendent de clarificació exacta del comportament esperat.

### 🟡 Separació d'arquitectes combinats
73 casos detectats (vegeu `.ai/ARQUITECTES-A-SEPARAR.md`). Pendent que Xavi ho revisi o ens demani fer-ho.

### 🟡 PDFs descarregables a "En paper"
Pendent de rebre els fitxers PDF de cada guia.

---

## Pròxims passos (per ordre)

### 1. Quan arribin dades de Jorge
- Fer còpia del WordPress (wp-content + BD)
- Importar les 564 entrades reals (edificis + coordenades)
- Descarregar les imatges
- Decidir correu: IMAP al nou servidor vs Etik

### 2. Revisió dels canvis publicats a staging
- Xavi revisa el nou comportament del mapa, enllaços de fitxes i pàgines d'arquitecte.
- Confirmar esquema de "En paper" (portada + botó PDF).

### 3. Disseny del web de guies
- Esperar decisió interna de Xavi sobre paleta
- Alternativa: avançar amb disseny neutre i adaptar colors després

### 3. App Flutter — Fase 1 (inici previst ~18 jul 2026)
- Eliminar Firebase del codi Flutter
- Configurar nova Google Maps API Key
- Compilar app buida per iOS i Android

### 4. App Flutter — Fase 2
- Decidir arquitectura BD (PostgreSQL vs alternativa)
- Decidir futur del backoffice Node.js
- Migrar compte admin Xavi

### 5. App Flutter — Fase 3 (scope confirmat, 3.900€)
- Llistat d'edificis amb filtres per publicació
- Fitxa d'edifici amb mapa
- Mapa general amb punts
- Filtre "per publicacions" (pendent clarificació)

---

## Calendari

| Qui | No disponible |
|-----|--------------|
| Joan | 2 setmanes agost (dates per confirmar) |
| Xavi | 1-9 ago, 22-30 ago, 1-16 set |

**Dipòsit:** 50% previ a l'inici del desenvolupament Flutter (flexible amb Xavi).
**Confirmació pressupost:** Xavi confirma 3.900€ — Joan pendent de validar.

---

## Decisions obertes

| Decisió | Opcions | Estat |
|---------|---------|-------|
| Correu electrònic | IMAP propi / Etik / seguir amb Gmail | Espera Jorge |
| Backoffice app | Mantenir Node.js / Reescriure / Headless CMS | Pendent |
| Base de dades app | PostgreSQL / SQLite / altra | Pendent |
| Disseny web guies | Colors publicació / Nou rebrand | Xavi decideix |
| Migració servidor complet | Fase 1 o Fase 2 | Pendent pressupost |
| Esquema "En paper" | Portada → plànol + botó PDF / només portada | Espera Xavi |
| Llicència peu de pàgina | © / Creative Commons | Espera Xavi |
| Separació d'arquitectes combinats | Manual per Xavi / automàtica per LinuxBCN | Espera Xavi |
| Normalització d'arquitectes duplicats | Aprovar `.ai/ARQUITECTES-NORMALITZACIO.yaml` | Espera Xavi |
| Correcció de punts desubicats | Aprovar propostes de geocodificació | Espera Xavi |
