# factor_data_tuto_NLP_SICSS

![Logos Factor~Data y SICSS](imgs/logos_final.png)

Material del taller de introducción al **Procesamiento de Lenguaje Natural (NLP)**
dictado en el **Summer Institute in Computational Social Sciences (SICSS) - Buenos
Aires** por **Factor~Data**. Incluye diapositivas, una notebook de ejemplo y datasets
de tweets para las prácticas hands-on.

🌐 **Sitio del curso:** <https://gefero.github.io/factor_data_tuto_NLP_SICSS/>

**[Español](#español) · [English](#english)**

---

## Español

### Estructura del repositorio

```
.
├── _config.yml   # Configuración del sitio de GitHub Pages (Jekyll)
├── index.md      # Front page del sitio publicado
├── cap0/   # Clase 0 (M0): Modelado de tópicos
├── cap1/   # Clase 1 (M1): Word embeddings
├── cap2/   # Clase 2 (M2): Transformers
├── cap3/   # Clase 3 (M3): LLMs y prompt engineering
├── data/   # Datasets de tweets para las prácticas
├── imgs/   # Logos e imágenes institucionales
├── LICENSE
└── README.md
```

### Contenidos por clase

Cada clase (`capN/`) se corresponde con el módulo `MN` del
[sitio del curso](https://gefero.github.io/factor_data_tuto_NLP_SICSS/), donde
están los links a las diapositivas de Google Slides y a las notebooks de
Colab/Drive usadas en cada práctica.

| Carpeta | Archivos locales | Tema | Slides (Google) | Notebook |
|---|---|---|---|---|
| [`cap0/`](cap0) | [`00 - SICSS-BAires - Topic Modeling.pdf`](<cap0/00 - SICSS-BAires - Topic Modeling.pdf>) | Introducción a NLP y modelado de tópicos (LDA) | [M0](https://docs.google.com/presentation/d/1ZoOBD8BvoVZkAu_58hRxQe2xowutgVfrsGJo3tR4QeY/edit?usp=sharing) | [M0](https://drive.google.com/file/d/1dpL7G5Cp5Zpi3Rkzp1MrTSYRG_VjCAN0/view?usp=drive_link) |
| [`cap1/`](cap1) | [`01 - SICSS-BAires - Embeddings.pdf`](<cap1/01 - SICSS-BAires - Embeddings.pdf>), [`01 - SICSS-BAires - Ilustracion Embeddings.ipynb`](<cap1/01 - SICSS-BAires - Ilustracion Embeddings.ipynb>) | Word embeddings estáticos (word2vec) | [M1](https://docs.google.com/presentation/d/1AQ9mwtzUg23ePFU37xi0usMqIVRizvyefeBVp8fatEY/edit?usp=sharing) | [M1](https://colab.research.google.com/drive/1UUr5TWTf1DR-U_QGNyFxaYhtA9Vj06WP?usp=sharing) |
| [`cap2/`](cap2) | [`02 -  SICSS - BAires - Transformers.pdf`](<cap2/02 -  SICSS - BAires - Transformers.pdf>) | Arquitectura Transformer y self-attention | [M2](https://docs.google.com/presentation/d/1WW7WRTLpKdnNJDQY3j9FnNpOSMYSC27IQILWU98lOoA/edit?usp=sharing) | [M2](https://colab.research.google.com/drive/1bTeXc6RHtIQaOcD0v1C5YTE2VKTQ-hlI?usp=sharing) |
| [`cap3/`](cap3) | [`03 - SICSS-Baires - LLMs.pdf`](<cap3/03 - SICSS-Baires - LLMs.pdf>) | Large Language Models y prompt engineering | [M3](https://docs.google.com/presentation/d/1mtF_NDhC8dnK7CAWxcgTcdErfrcu2EPxe5JPe-L2yuE/edit?usp=sharing) | — |

#### `cap0/` — Clase 0: Detectando tópicos en un corpus (68 slides)

Qué es NLP y el problema del dato no estructurado, un flujo de trabajo "típico" en
NLP (limpieza de texto, stopwords, tokenización, stemming vs. lematización),
representación matemática de un texto (Document-Term Matrix, Bag of Words) y
modelado de tópicos con **Latent Dirichlet Allocation (LDA)**. Incluye casos de
aplicación (letras de tango, comentarios sobre COVID-19) y las consignas para el
trabajo hands-on en grupos con un dataset de noticias.

- [Slides (Google Slides)](https://docs.google.com/presentation/d/1ZoOBD8BvoVZkAu_58hRxQe2xowutgVfrsGJo3tR4QeY/edit?usp=sharing)
- [Notebook (Google Drive)](https://drive.google.com/file/d/1dpL7G5Cp5Zpi3Rkzp1MrTSYRG_VjCAN0/view?usp=drive_link)

#### `cap1/` — Clase 1: Acercamiento a los word embeddings (109 slides + notebook)

Semántica léxica y semántica vectorial, matrices de co-ocurrencia palabra-contexto,
similitud coseno, la intuición de **word2vec** (skip-gram, negative sampling) y
aplicaciones en ciencias sociales (detección de estereotipos, trayectorias).

La notebook [`01 - SICSS-BAires - Ilustracion Embeddings.ipynb`](<cap1/01 - SICSS-BAires - Ilustracion Embeddings.ipynb>)
ilustra el uso de embeddings estáticos en español para detectar estereotipos
culturales (género, pobreza) frente a dimensiones dependientes (deportes,
ocupaciones, música, etc.), calculando la distancia coseno entre los vectores
promedio de cada dimensión.

- **Dependencias:** `numpy`, `pandas`, `gensim`, `scipy`, `plotnine`.
- **Datos externos:** descarga automáticamente los embeddings preentrenados
  [SBWCE](https://cs.famaf.unc.edu.ar/~ccardellino/SBWCE/) (`SBW-vectors-300-min5`,
  ~1,5 GB) desde la propia notebook — no están versionados en este repo.

- [Slides (Google Slides)](https://docs.google.com/presentation/d/1AQ9mwtzUg23ePFU37xi0usMqIVRizvyefeBVp8fatEY/edit?usp=sharing)
- [Notebook (Google Colab)](https://colab.research.google.com/drive/1UUr5TWTf1DR-U_QGNyFxaYhtA9Vj06WP?usp=sharing)

#### `cap2/` — Clase 2: Transformers (32 slides)

De los modelos secuenciales (RNN) a los Transformers: embeddings de
entrada/salida, self-attention (vectores Query/Key/Value), atención multicabezal
(multi-head attention) y positional encoding. Reseña de GPT y BERT. Incluye
consignas hands-on con `pysentimiento` sobre un dataset de comentarios.

- [Slides (Google Slides)](https://docs.google.com/presentation/d/1WW7WRTLpKdnNJDQY3j9FnNpOSMYSC27IQILWU98lOoA/edit?usp=sharing)
- [Notebook (Google Colab)](https://colab.research.google.com/drive/1bTeXc6RHtIQaOcD0v1C5YTE2VKTQ-hlI?usp=sharing)

#### `cap3/` — Clase 3: ¿Cómo interactuamos con un LLM? (52 slides)

Evolución de los LLMs, para qué (no) conviene usarlos, sus riesgos (alucinaciones,
sesgos de género/raciales/culturales/políticos/lingüísticos) y transfer
learning/fine-tuning. La segunda mitad es una guía práctica de **prompt
engineering**: roles (`system`/`user`), x-shot learning y Chain of Thought (CoT),
con 6 ejercicios guiados para practicar con un LLM conversacional.

- [Slides (Google Slides)](https://docs.google.com/presentation/d/1mtF_NDhC8dnK7CAWxcgTcdErfrcu2EPxe5JPe-L2yuE/edit?usp=sharing)

### Datos (`data/`)

Dos corpus de tweets de la campaña electoral argentina 2023, comprimidos en `.zip`
(descomprimir con `unzip data/tweets_candidatos.zip -d data/`, por ejemplo).

| Archivo | Registros | Cuentas | Rango de fechas |
|---|---|---|---|
| `tweets_candidatos.zip` → `tweets_candidatos.csv` | 54.604 tweets | 25 cuentas de candidatos/dirigentes políticos (p. ej. `mauriciomacri`, `horaciorlarreta`, `SergioMassa`, `CFKArgentina`, `PatoBullrich`, `JuanGrabois`) | 2010-10-30 a 2023-02-02 |
| `tweets_menciones.zip` → `tweets_menciones.csv` | 279.913 tweets | Menciones de terceros a esas cuentas | 2023-02-02 a 2023-02-10 |

Ambos archivos comparten esquema (25 columnas), entre ellas: `id_str`, `created`,
`user_name`, `user_location`, `user_followers`, `user_description`, `tweet`,
`text`, `tweet_proc` (texto preprocesado), `n_favorites`, `n_retweets`, `language`,
`place_country`. Son datos públicos de Twitter/X recolectados con fines
didácticos para las prácticas de los capítulos 0 a 2.

### Imágenes (`imgs/`)

Logos institucionales usados en las diapositivas, en este README y en el sitio
del curso: `LOGO-FactorData-Color.png`, `SICSS_ARG_Transparente.png`,
`logos_final.png`.

### Sitio del curso (`_config.yml`, `index.md`)

El repositorio publica un sitio con **GitHub Pages** (tema Jekyll
`jekyll-theme-cayman`) generado a partir de `index.md`, con la presentación del
curso y los links a las diapositivas y notebooks de cada módulo:
<https://gefero.github.io/factor_data_tuto_NLP_SICSS/>.

### Cómo usar el material

1. Recorrer las diapositivas en orden: `cap0`/M0 → `cap1`/M1 → `cap2`/M2 →
   `cap3`/M3, ya sea desde los PDFs locales o desde los links de Google Slides
   del [sitio del curso](https://gefero.github.io/factor_data_tuto_NLP_SICSS/).
2. Abrir las notebooks de cada módulo en Google Colab/Drive (o la notebook
   local de `cap1/` en Jupyter) para reproducir las prácticas.
3. Descomprimir los datasets de `data/` para las consignas hands-on de tópicos y
   transformers.

> Nota: las notebooks de práctica de M0–M2 se distribuyen vía Google
> Colab/Drive (ver tabla y links por capítulo arriba) y no están versionadas en
> este repositorio; solo la notebook de `cap1/` tiene una copia local.

### Licencia

Este repositorio se distribuye bajo licencia [MIT](LICENSE).

---

## English

### Repository structure

```
.
├── _config.yml   # GitHub Pages (Jekyll) site configuration
├── index.md      # Front page of the published site
├── cap0/   # Session 0 (M0): Topic modeling
├── cap1/   # Session 1 (M1): Word embeddings
├── cap2/   # Session 2 (M2): Transformers
├── cap3/   # Session 3 (M3): LLMs and prompt engineering
├── data/   # Tweet datasets for the hands-on exercises
├── imgs/   # Institutional logos and images
├── LICENSE
└── README.md
```

### Contents by session

Each session (`capN/`) corresponds to module `MN` on the
[course site](https://gefero.github.io/factor_data_tuto_NLP_SICSS/), which
links to the Google Slides deck and the Colab/Drive notebook used in each
practice.

| Folder | Local files | Topic | Slides (Google) | Notebook |
|---|---|---|---|---|
| [`cap0/`](cap0) | [`00 - SICSS-BAires - Topic Modeling.pdf`](<cap0/00 - SICSS-BAires - Topic Modeling.pdf>) | Intro to NLP and topic modeling (LDA) | [M0](https://docs.google.com/presentation/d/1ZoOBD8BvoVZkAu_58hRxQe2xowutgVfrsGJo3tR4QeY/edit?usp=sharing) | [M0](https://drive.google.com/file/d/1dpL7G5Cp5Zpi3Rkzp1MrTSYRG_VjCAN0/view?usp=drive_link) |
| [`cap1/`](cap1) | [`01 - SICSS-BAires - Embeddings.pdf`](<cap1/01 - SICSS-BAires - Embeddings.pdf>), [`01 - SICSS-BAires - Ilustracion Embeddings.ipynb`](<cap1/01 - SICSS-BAires - Ilustracion Embeddings.ipynb>) | Static word embeddings (word2vec) | [M1](https://docs.google.com/presentation/d/1AQ9mwtzUg23ePFU37xi0usMqIVRizvyefeBVp8fatEY/edit?usp=sharing) | [M1](https://colab.research.google.com/drive/1UUr5TWTf1DR-U_QGNyFxaYhtA9Vj06WP?usp=sharing) |
| [`cap2/`](cap2) | [`02 -  SICSS - BAires - Transformers.pdf`](<cap2/02 -  SICSS - BAires - Transformers.pdf>) | Transformer architecture and self-attention | [M2](https://docs.google.com/presentation/d/1WW7WRTLpKdnNJDQY3j9FnNpOSMYSC27IQILWU98lOoA/edit?usp=sharing) | [M2](https://colab.research.google.com/drive/1bTeXc6RHtIQaOcD0v1C5YTE2VKTQ-hlI?usp=sharing) |
| [`cap3/`](cap3) | [`03 - SICSS-Baires - LLMs.pdf`](<cap3/03 - SICSS-Baires - LLMs.pdf>) | Large Language Models and prompt engineering | [M3](https://docs.google.com/presentation/d/1mtF_NDhC8dnK7CAWxcgTcdErfrcu2EPxe5JPe-L2yuE/edit?usp=sharing) | — |

#### `cap0/` — Session 0: Detecting topics in a corpus (68 slides)

What NLP is and the problem of unstructured data, a "typical" NLP workflow (text
cleaning, stopword removal, tokenization, stemming vs. lemmatization),
mathematical representations of text (Document-Term Matrix, Bag of Words), and
topic modeling with **Latent Dirichlet Allocation (LDA)**. Includes applied case
studies (tango lyrics, COVID-19 news comments) and the instructions for the
group hands-on exercise with a news dataset.

- [Slides (Google Slides)](https://docs.google.com/presentation/d/1ZoOBD8BvoVZkAu_58hRxQe2xowutgVfrsGJo3tR4QeY/edit?usp=sharing)
- [Notebook (Google Drive)](https://drive.google.com/file/d/1dpL7G5Cp5Zpi3Rkzp1MrTSYRG_VjCAN0/view?usp=drive_link)

#### `cap1/` — Session 1: Introduction to word embeddings (109 slides + notebook)

Lexical vs. vector semantics, word-context co-occurrence matrices, cosine
similarity, the intuition behind **word2vec** (skip-gram, negative sampling), and
social-science applications (stereotype detection, trajectories).

The notebook [`01 - SICSS-BAires - Ilustracion Embeddings.ipynb`](<cap1/01 - SICSS-BAires - Ilustracion Embeddings.ipynb>)
shows how to use Spanish static word embeddings to detect cultural stereotypes
(gender, poverty) against dependent dimensions (sports, occupations, music,
etc.) by computing cosine distance between each dimension's average vector.

- **Dependencies:** `numpy`, `pandas`, `gensim`, `scipy`, `plotnine`.
- **External data:** the notebook automatically downloads the pretrained
  [SBWCE](https://cs.famaf.unc.edu.ar/~ccardellino/SBWCE/) embeddings
  (`SBW-vectors-300-min5`, ~1.5 GB) — they are not tracked in this repo.

- [Slides (Google Slides)](https://docs.google.com/presentation/d/1AQ9mwtzUg23ePFU37xi0usMqIVRizvyefeBVp8fatEY/edit?usp=sharing)
- [Notebook (Google Colab)](https://colab.research.google.com/drive/1UUr5TWTf1DR-U_QGNyFxaYhtA9Vj06WP?usp=sharing)

#### `cap2/` — Session 2: Transformers (32 slides)

From sequential models (RNNs) to Transformers: input/output embeddings,
self-attention (Query/Key/Value vectors), multi-head attention, and positional
encoding. Overview of GPT and BERT. Includes hands-on instructions using
`pysentimiento` on a comments dataset.

- [Slides (Google Slides)](https://docs.google.com/presentation/d/1WW7WRTLpKdnNJDQY3j9FnNpOSMYSC27IQILWU98lOoA/edit?usp=sharing)
- [Notebook (Google Colab)](https://colab.research.google.com/drive/1bTeXc6RHtIQaOcD0v1C5YTE2VKTQ-hlI?usp=sharing)

#### `cap3/` — Session 3: How do we interact with an LLM? (52 slides)

Evolution of LLMs, when (not) to use them, their risks (hallucinations,
gender/racial/cultural/political/linguistic biases), and transfer
learning/fine-tuning. The second half is a hands-on **prompt engineering**
guide: roles (`system`/`user`), x-shot learning, and Chain of Thought (CoT)
prompting, with 6 guided exercises to practice with a conversational LLM.

- [Slides (Google Slides)](https://docs.google.com/presentation/d/1mtF_NDhC8dnK7CAWxcgTcdErfrcu2EPxe5JPe-L2yuE/edit?usp=sharing)

### Data (`data/`)

Two tweet corpora from the 2023 Argentine electoral campaign, compressed as
`.zip` files (unzip with `unzip data/tweets_candidatos.zip -d data/`, for
example).

| File | Records | Accounts | Date range |
|---|---|---|---|
| `tweets_candidatos.zip` → `tweets_candidatos.csv` | 54,604 tweets | 25 accounts of political candidates/leaders (e.g. `mauriciomacri`, `horaciorlarreta`, `SergioMassa`, `CFKArgentina`, `PatoBullrich`, `JuanGrabois`) | 2010-10-30 to 2023-02-02 |
| `tweets_menciones.zip` → `tweets_menciones.csv` | 279,913 tweets | Third-party tweets mentioning those accounts | 2023-02-02 to 2023-02-10 |

Both files share the same schema (25 columns), including: `id_str`, `created`,
`user_name`, `user_location`, `user_followers`, `user_description`, `tweet`,
`text`, `tweet_proc` (preprocessed text), `n_favorites`, `n_retweets`,
`language`, `place_country`. This is public Twitter/X data collected for
teaching purposes, used in the hands-on exercises of chapters 0 through 2.

### Images (`imgs/`)

Institutional logos used across the slides, this README, and the course site:
`LOGO-FactorData-Color.png`, `SICSS_ARG_Transparente.png`, `logos_final.png`.

### Course site (`_config.yml`, `index.md`)

The repository publishes a **GitHub Pages** site (Jekyll theme
`jekyll-theme-cayman`) generated from `index.md`, with the course overview and
the links to each module's slides and notebooks:
<https://gefero.github.io/factor_data_tuto_NLP_SICSS/>.

### How to use this material

1. Go through the slides in order: `cap0`/M0 → `cap1`/M1 → `cap2`/M2 →
   `cap3`/M3, either from the local PDFs or from the Google Slides links on the
   [course site](https://gefero.github.io/factor_data_tuto_NLP_SICSS/).
2. Open each module's notebook in Google Colab/Drive (or the local `cap1/`
   notebook in Jupyter) to reproduce the practices.
3. Unzip the datasets in `data/` for the topic-modeling and transformers
   hands-on exercises.

> Note: the M0–M2 practice notebooks are distributed via Google Colab/Drive
> (see the table and per-session links above) and are not tracked in this
> repository; only the `cap1/` notebook has a local copy.

### License

This repository is distributed under the [MIT](LICENSE) license.
