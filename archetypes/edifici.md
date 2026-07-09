+++
title = '{{ replace .File.ContentBaseName "-" " " | title }}'
date = '{{ .Date }}'
draft = true

# Camps núcli — presents (Sí) a quasi totes les publicacions del CSV.
adreca = ""
any = ""
publicacions = []      # slugs a data/publicacions.yaml, ex: ["gatcpac", "poblenou"]
lat = ""
long = ""

# Camps opcionals — presència real varia per publicació d'origen,
# consultar data/publicacions.yaml > <slug> > camps abans d'assumir-los buits.
descripcio = ""
tipologia = ""
foto = ""
illustracio = ""
arquitectes = []
descripcio_arquitectes = ""
proteccio = ""
arquitecte_reforma = ""
any_reforma = ""
premis = ""
superficie = ""
nomenclator = ""
descripcio_nomenclator = ""
+++
