# SICSS - Buenos Aires 2026

![Logos Factor~Data y SICSS](imgs/logos_final.png)

Material completo del **Summer Institute in Computational Social Sciences (SICSS) -
Buenos Aires 2026**, organizado por **[Factor~Data](https://factor-data.netlify.app/)**
junto a la EIDAES-UNSAM: charlas, talleres (Procesamiento de Lenguaje Natural y
Encuestas) y el trabajo final del instituto.

🌐 **Sitio del instituto:** <https://gefero.github.io/factor_data_SICSS_Baires_2026/> — ahí
está la descripción de cada charla, cada módulo y cada consigna, con los links a
diapositivas de Google Slides y notebooks de Colab/Drive. Este README es solo un mapa
del repositorio.

## Estructura del repositorio

```
.
├── _config.yml, _data/, _includes/, _layouts/   # sitio de GitHub Pages (Jekyll)
├── index.md, charlas.md, taller-nlp.md,
│   taller-encuestas.md, desafio.md              # páginas del sitio
├── charlas/            # PDFs de las 13 charlas y paneles del instituto
├── taller_nlp/         # taller de NLP: cap0 (vectorización) … cap3 (LLMs)
├── taller_encuestas/   # taller de encuestas: material comprimido (~102 MB)
├── consignas_desafio/  # trabajo final: dos consignas a elección
│   ├── clasificacion/            # opción A: índice de polarización en noticias
│   ├── encuestas/                # opción B: polarización comparada (WVS)
│   └── presentaciones_asistentes/  # trabajos finales de ediciones anteriores
├── data/                # datasets de tweets, HatEval y anotaciones para el taller de NLP
├── imgs/                # logos institucionales
├── LICENSE
└── README.md
```

## Git LFS

Los archivos pesados (`.zip`, `.rds`, y algunos `.csv`/`.pdf` según cuándo se subieron)
están en [Git LFS](https://git-lfs.com/). Para clonar el repo con el contenido real y no
con los punteros:

```
git lfs install
git clone https://github.com/gefero/factor_data_SICSS_Baires_2026
```

Si ya clonaste sin `git-lfs` instalado, `git lfs pull` dentro del repo baja el contenido.

**Ojo con Colab:** las celdas `!git clone ...` de las notebooks de `taller_nlp/` clonan
sin `git-lfs`, así que algunos datasets (`hateval_test_df.csv`, `hateval_train_df.csv`,
`rtas_hateval_llm.csv`, los `.zip`) quedan como punteros de texto de ~130 bytes en vez del
archivo real — y `pandas` no tira error al leerlos, así que el fallo es silencioso, no un
`FileNotFoundError`. Por eso esas celdas ahora instalan `git-lfs` antes de clonar
(`!apt-get -qq install -y git-lfs && git lfs install --skip-repo`); si adaptás o agregás
una notebook nueva que lea de `data/`, conviene mantener esa línea.

## Licencia

Este repositorio se distribuye bajo licencia [MIT](LICENSE).
