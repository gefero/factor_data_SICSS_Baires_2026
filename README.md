# factor_data_tuto_NLP_SICSS

![Logos Factor~Data y SICSS](imgs/logos_final.png)

Material del taller de introducción al **Procesamiento de Lenguaje Natural (NLP)**
dictado en el **Summer Institute in Computational Social Sciences (SICSS) - Buenos
Aires** por **Factor~Data**. Incluye diapositivas, una notebook de ejemplo y datasets
de tweets para las prácticas hands-on.

**[Español](#español) · [English](#english)**

---

## Español

### Estructura del repositorio

```
.
├── cap0/   # Clase 0: Modelado de tópicos
├── cap1/   # Clase 1: Word embeddings
├── cap2/   # Clase 2: Transformers
├── cap3/   # Clase 3: LLMs y prompt engineering
├── data/   # Datasets de tweets para las prácticas
├── imgs/   # Logos e imágenes institucionales
├── LICENSE
└── README.md
```

### Contenidos por clase

| Carpeta | Archivos | Tema |
|---|---|---|
| [`cap0/`](cap0) | [`00 - SICSS-BAires - Topic Modeling.pdf`](<cap0/00 - SICSS-BAires - Topic Modeling.pdf>) | Introducción a NLP y modelado de tópicos (LDA) |
| [`cap1/`](cap1) | [`01 - SICSS-BAires - Embeddings.pdf`](<cap1/01 - SICSS-BAires - Embeddings.pdf>), [`01 - SICSS-BAires - Ilustracion Embeddings.ipynb`](<cap1/01 - SICSS-BAires - Ilustracion Embeddings.ipynb>) | Word embeddings estáticos (word2vec) |
| [`cap2/`](cap2) | [`02 -  SICSS - BAires - Transformers.pdf`](<cap2/02 -  SICSS - BAires - Transformers.pdf>) | Arquitectura Transformer y self-attention |
| [`cap3/`](cap3) | [`03 - SICSS-Baires - LLMs.pdf`](<cap3/03 - SICSS-Baires - LLMs.pdf>) | Large Language Models y prompt engineering |

#### `cap0/` — Clase 0: Detectando tópicos en un corpus (68 slides)

Qué es NLP y el problema del dato no estructurado, un flujo de trabajo "típico" en
NLP (limpieza de texto, stopwords, tokenización, stemming vs. lematización),
representación matemática de un texto (Document-Term Matrix, Bag of Words) y
modelado de tópicos con **Latent Dirichlet Allocation (LDA)**. Incluye casos de
aplicación (letras de tango, comentarios sobre COVID-19) y las consignas para el
trabajo hands-on en grupos con un dataset de noticias.

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

#### `cap2/` — Clase 2: Transformers (32 slides)

De los modelos secuenciales (RNN) a los Transformers: embeddings de
entrada/salida, self-attention (vectores Query/Key/Value), atención multicabezal
(multi-head attention) y positional encoding. Reseña de GPT y BERT. Incluye
consignas hands-on con `pysentimiento` sobre un dataset de comentarios.

#### `cap3/` — Clase 3: ¿Cómo interactuamos con un LLM? (52 slides)

Evolución de los LLMs, para qué (no) conviene usarlos, sus riesgos (alucinaciones,
sesgos de género/raciales/culturales/políticos/lingüísticos) y transfer
learning/fine-tuning. La segunda mitad es una guía práctica de **prompt
engineering**: roles (`system`/`user`), x-shot learning y Chain of Thought (CoT),
con 6 ejercicios guiados para practicar con un LLM conversacional.

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

Logos institucionales usados en las diapositivas y en este README:
`LOGO-FactorData-Color.png`, `SICSS_ARG_Transparente.png`, `logos_final.png`.

### Cómo usar el material

1. Recorrer las diapositivas en orden: `cap0` → `cap1` → `cap2` → `cap3`.
2. Abrir la notebook de `cap1/` en Jupyter o Google Colab para reproducir el
   ejemplo de embeddings (instalar las dependencias listadas arriba).
3. Descomprimir los datasets de `data/` para las consignas hands-on de tópicos y
   transformers.

> Nota: las diapositivas de `cap0` y `cap2` hacen referencia a notebooks de
> práctica ("Vamos al notebook...") que todavía no están versionadas en este
> repositorio.

### Licencia

Este repositorio se distribuye bajo licencia [MIT](LICENSE).

---

## English

### Repository structure

```
.
├── cap0/   # Session 0: Topic modeling
├── cap1/   # Session 1: Word embeddings
├── cap2/   # Session 2: Transformers
├── cap3/   # Session 3: LLMs and prompt engineering
├── data/   # Tweet datasets for the hands-on exercises
├── imgs/   # Institutional logos and images
├── LICENSE
└── README.md
```

### Contents by session

| Folder | Files | Topic |
|---|---|---|
| [`cap0/`](cap0) | [`00 - SICSS-BAires - Topic Modeling.pdf`](<cap0/00 - SICSS-BAires - Topic Modeling.pdf>) | Intro to NLP and topic modeling (LDA) |
| [`cap1/`](cap1) | [`01 - SICSS-BAires - Embeddings.pdf`](<cap1/01 - SICSS-BAires - Embeddings.pdf>), [`01 - SICSS-BAires - Ilustracion Embeddings.ipynb`](<cap1/01 - SICSS-BAires - Ilustracion Embeddings.ipynb>) | Static word embeddings (word2vec) |
| [`cap2/`](cap2) | [`02 -  SICSS - BAires - Transformers.pdf`](<cap2/02 -  SICSS - BAires - Transformers.pdf>) | Transformer architecture and self-attention |
| [`cap3/`](cap3) | [`03 - SICSS-Baires - LLMs.pdf`](<cap3/03 - SICSS-Baires - LLMs.pdf>) | Large Language Models and prompt engineering |

#### `cap0/` — Session 0: Detecting topics in a corpus (68 slides)

What NLP is and the problem of unstructured data, a "typical" NLP workflow (text
cleaning, stopword removal, tokenization, stemming vs. lemmatization),
mathematical representations of text (Document-Term Matrix, Bag of Words), and
topic modeling with **Latent Dirichlet Allocation (LDA)**. Includes applied case
studies (tango lyrics, COVID-19 news comments) and the instructions for the
group hands-on exercise with a news dataset.

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

#### `cap2/` — Session 2: Transformers (32 slides)

From sequential models (RNNs) to Transformers: input/output embeddings,
self-attention (Query/Key/Value vectors), multi-head attention, and positional
encoding. Overview of GPT and BERT. Includes hands-on instructions using
`pysentimiento` on a comments dataset.

#### `cap3/` — Session 3: How do we interact with an LLM? (52 slides)

Evolution of LLMs, when (not) to use them, their risks (hallucinations,
gender/racial/cultural/political/linguistic biases), and transfer
learning/fine-tuning. The second half is a hands-on **prompt engineering**
guide: roles (`system`/`user`), x-shot learning, and Chain of Thought (CoT)
prompting, with 6 guided exercises to practice with a conversational LLM.

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

Institutional logos used across the slides and this README:
`LOGO-FactorData-Color.png`, `SICSS_ARG_Transparente.png`, `logos_final.png`.

### How to use this material

1. Go through the slides in order: `cap0` → `cap1` → `cap2` → `cap3`.
2. Open the `cap1/` notebook in Jupyter or Google Colab to reproduce the
   embeddings example (install the dependencies listed above).
3. Unzip the datasets in `data/` for the topic-modeling and transformers
   hands-on exercises.

> Note: the `cap0` and `cap2` slides reference practice notebooks ("Vamos al
> notebook...") that are not yet tracked in this repository.

### License

This repository is distributed under the [MIT](LICENSE) license.
