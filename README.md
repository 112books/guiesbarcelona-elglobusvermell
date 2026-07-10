# guiesbarcelona.elglobusvermell.org

Webapp de guies de Barcelona per El Globus Vermell. Hugo + OpenStreetMap/Leaflet + OpenRouteService, sense dependències de Google. Detalls tècnics a la proposta v1.3 (repo `docs`).

## Desenvolupament

```bash
hugo server -D
```

## Publicar canvis

Editar els `.md` i executar `./publica-canvis` (Mac/Linux) o fer doble clic a `publica-canvis.bat` (Windows, requereix Git for Windows / Git Bash).

## Branques

- `main` → únic entorn: revisió/staging i producció alhora (GitHub Pages, protegit amb contrasenya fins al llançament final). Un cop validat, es publica al servidor definitiu de LinuxBCN.

## Repos relacionats

- `../docs` — propostes, pressupost, decisions ([112books/elglobusvermell-docs](https://github.com/112books/elglobusvermell-docs))
- `../sync-elglobusvermell` — scripts de sincronització i deploy (ús intern LinuxBCN)
