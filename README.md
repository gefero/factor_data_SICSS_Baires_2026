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
├── consigna_desafio/   # Trabajo final: dos consignas a elección
│   ├── clasificacion/   # Opción A: índice de polarización en comentarios de noticias
│   └── encuestas/   # Opción B: polarización comparada con el World Values Survey
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
| [`cap0/`](cap0) | [`00 - SICSS-BAires - Topic Modeling.pdf`](<cap0/00 - SICSS-BAires - Topic Modeling.pdf>), [`00_SICSS_BAires_Vectorización.ipynb`](<cap0/00_SICSS_BAires_Vectorización.ipynb>), [`00_SICSS_BAires_Vectorización_R.Rmd`](<cap0/00_SICSS_BAires_Vectorización_R.Rmd>), [`ejemplo_clasificacion.ipynb`](cap0/ejemplo_clasificacion.ipynb) | Introducción a NLP y modelado de tópicos (LDA) | [M0](https://docs.google.com/presentation/d/1ZoOBD8BvoVZkAu_58hRxQe2xowutgVfrsGJo3tR4QeY/edit?usp=sharing) | [M0](https://drive.google.com/file/d/1dpL7G5Cp5Zpi3Rkzp1MrTSYRG_VjCAN0/view?usp=drive_link) |
| [`cap1/`](cap1) | [`01 - SICSS-BAires - Embeddings.pdf`](<cap1/01 - SICSS-BAires - Embeddings.pdf>), [`01_SICSS_BAires_Ilustracion_Embeddings.ipynb`](cap1/01_SICSS_BAires_Ilustracion_Embeddings.ipynb) | Word embeddings estáticos (word2vec) | [M1](https://docs.google.com/presentation/d/1AQ9mwtzUg23ePFU37xi0usMqIVRizvyefeBVp8fatEY/edit?usp=sharing) | [M1](https://colab.research.google.com/drive/1UUr5TWTf1DR-U_QGNyFxaYhtA9Vj06WP?usp=sharing) |
| [`cap2/`](cap2) | [`02 -  SICSS - BAires - Transformers.pdf`](<cap2/02 -  SICSS - BAires - Transformers.pdf>), [`02_SICSS_BAires_Hate_Speech_con_pysentimiento.ipynb`](cap2/02_SICSS_BAires_Hate_Speech_con_pysentimiento.ipynb), [`02_SICSS_BAires_Transformers.ipynb`](cap2/02_SICSS_BAires_Transformers.ipynb), [`02_SICSS_BAires_Transformers_R.Rmd`](cap2/02_SICSS_BAires_Transformers_R.Rmd) | Arquitectura Transformer y self-attention | [M2](https://docs.google.com/presentation/d/1WW7WRTLpKdnNJDQY3j9FnNpOSMYSC27IQILWU98lOoA/edit?usp=sharing) | [M2](https://colab.research.google.com/drive/1bTeXc6RHtIQaOcD0v1C5YTE2VKTQ-hlI?usp=sharing) |
| [`cap3/`](cap3) | [`03 - SICSS-Baires - LLMs.pdf`](<cap3/03 - SICSS-Baires - LLMs.pdf>), [`03_SICSS_Baires_LLMs.ipynb`](cap3/03_SICSS_Baires_LLMs.ipynb), [`03_SICSS_Baires_LLMs_R.Rmd`](cap3/03_SICSS_Baires_LLMs_R.Rmd), [`03_SICSS_Baires_LLMs_y_Anotación.ipynb`](<cap3/03_SICSS_Baires_LLMs_y_Anotación.ipynb>), [`03_SICSS_Baires_LLMS_Sesgos.ipynb`](cap3/03_SICSS_Baires_LLMS_Sesgos.ipynb), [`03_SICSS_Baires_Acuerdo_entre_Anotadores.ipynb`](cap3/03_SICSS_Baires_Acuerdo_entre_Anotadores.ipynb) | Large Language Models y prompt engineering | [M3](https://docs.google.com/presentation/d/1mtF_NDhC8dnK7CAWxcgTcdErfrcu2EPxe5JPe-L2yuE/edit?usp=sharing) | [Acuerdo entre anotadores](cap3/03_SICSS_Baires_Acuerdo_entre_Anotadores.ipynb) |
| [`consigna_desafio/clasificacion/`](consigna_desafio/clasificacion) | [`CONSIGNA.md`](consigna_desafio/clasificacion/CONSIGNA.md), [`SICSS_BAires_TP_Final_Esqueleto.ipynb`](consigna_desafio/clasificacion/SICSS_BAires_TP_Final_Esqueleto.ipynb), [`SICSS_BAires_Desafio_Polarizacion_Noticias.ipynb`](consigna_desafio/clasificacion/SICSS_BAires_Desafio_Polarizacion_Noticias.ipynb) | **Trabajo final, opción A:** índice de polarización en comentarios de noticias | — | [Consigna](consigna_desafio/clasificacion/CONSIGNA.md) · [Esqueleto](consigna_desafio/clasificacion/SICSS_BAires_TP_Final_Esqueleto.ipynb) · [Solución](consigna_desafio/clasificacion/SICSS_BAires_Desafio_Polarizacion_Noticias.ipynb) |
| [`consigna_desafio/encuestas/`](consigna_desafio/encuestas) | [`consigna_trabajo_final_polarizacion_WVS_v3.md`](consigna_desafio/encuestas/consigna_trabajo_final_polarizacion_WVS_v3.md), [`data/`](consigna_desafio/encuestas/data) (WVS ola 7 + cuestionario) | **Trabajo final, opción B:** polarización comparada con el World Values Survey | — | [Consigna](consigna_desafio/encuestas/consigna_trabajo_final_polarizacion_WVS_v3.md) |

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

La notebook [`01_SICSS_BAires_Ilustracion_Embeddings.ipynb`](cap1/01_SICSS_BAires_Ilustracion_Embeddings.ipynb)
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

#### `cap2/` — Clase 2: Transformers (32 slides + notebook)

De los modelos secuenciales (RNN) a los Transformers: embeddings de
entrada/salida, self-attention (vectores Query/Key/Value), atención multicabezal
(multi-head attention) y positional encoding. Reseña de GPT y BERT. Incluye
consignas hands-on con `pysentimiento` sobre un dataset de comentarios.

La notebook [`02_SICSS_BAires_Hate_Speech_con_pysentimiento.ipynb`](cap2/02_SICSS_BAires_Hate_Speech_con_pysentimiento.ipynb)
usa el modelo de discurso de odio en español de `pysentimiento` (RoBERTuito
fine-tuneado) para predecir `HS` sobre el split de test de HatEval
(`data/hateval_test_df.csv`), y compara el resultado contra las
representaciones clásicas (TF, TF-IDF, embeddings) de `cap0/`.

- **Dependencias:** `pysentimiento`, `transformers`, `torch`, `pandas`,
  `scikit-learn`, `matplotlib`, `seaborn`.
- **Datos:** `data/hateval_test_df.csv` (ya versionado en el repo).

- [Slides (Google Slides)](https://docs.google.com/presentation/d/1WW7WRTLpKdnNJDQY3j9FnNpOSMYSC27IQILWU98lOoA/edit?usp=sharing)
- [Notebook (Google Colab)](https://colab.research.google.com/drive/1bTeXc6RHtIQaOcD0v1C5YTE2VKTQ-hlI?usp=sharing)

#### `cap3/` — Clase 3: ¿Cómo interactuamos con un LLM? (52 slides)

Evolución de los LLMs, para qué (no) conviene usarlos, sus riesgos (alucinaciones,
sesgos de género/raciales/culturales/políticos/lingüísticos) y transfer
learning/fine-tuning. La segunda mitad es una guía práctica de **prompt
engineering**: roles (`system`/`user`), x-shot learning y Chain of Thought (CoT),
con 6 ejercicios guiados para practicar con un LLM conversacional.

- [Slides (Google Slides)](https://docs.google.com/presentation/d/1mtF_NDhC8dnK7CAWxcgTcdErfrcu2EPxe5JPe-L2yuE/edit?usp=sharing)

La notebook [`03_SICSS_Baires_Acuerdo_entre_Anotadores.ipynb`](cap3/03_SICSS_Baires_Acuerdo_entre_Anotadores.ipynb)
calcula métricas de acuerdo inter-anotador (acuerdo observado, kappa de Cohen,
kappa de Fleiss, alfa de Krippendorff, PABAK) sobre `data/sicss-anotacion-unificado.json`,
donde 10 codificadores anotaron el mismo conjunto de 74 tweets con el esquema
de discurso de odio usado en `03_SICSS_Baires_LLMs_y_Anotación.ipynb`. Sirve
como techo realista contra el que evaluar a un LLM anotador.

- **Dependencias:** `pandas`, `numpy`, `scikit-learn`, `statsmodels`,
  `matplotlib`, `seaborn`.
- **Datos:** `data/sicss-anotacion-unificado.json`.

#### `consigna_desafio/` — Trabajo final: polarización

El taller cierra con un trabajo final que usa lo visto para responder una pregunta
sustantiva en vez de enseñar una técnica. Hay **dos consignas a elección**, una por
camino metodológico; cada grupo elige una. El entregable es el mismo en las dos: una
presentación de unos 10 minutos que reseñe las decisiones metodológicas y los
principales resultados, con la notebook del análisis como respaldo.

| Opción | Consigna | Pregunta |
|---|---|---|
| **A. Clasificación** | [`clasificacion/CONSIGNA.md`](consigna_desafio/clasificacion/CONSIGNA.md) | ¿Qué noticias polarizan la conversación de sus lectores? |
| **B. Encuestas** | [`encuestas/consigna_trabajo_final_polarizacion_WVS_v3.md`](consigna_desafio/encuestas/consigna_trabajo_final_polarizacion_WVS_v3.md) | ¿Está América Latina más polarizada que el resto del mundo? |

##### Opción A — `clasificacion/`: índice de polarización a nivel noticia

La [consigna](consigna_desafio/clasificacion/CONSIGNA.md) pide construir un índice de
polarización **a nivel noticia**: una función que toma todos los comentarios que recibió
una noticia y devuelve un número. Deliberadamente **no dice cómo operacionalizar la
polarización**: plantea siete preguntas abiertas —qué significa que una noticia sea
polarizante, cómo hacer el índice comparable entre noticias, sobre cuántos comentarios es
válido calcularlo, cómo validarlo— y la estrategia metodológica la deciden los grupos. Hay
un [esqueleto de notebook](consigna_desafio/clasificacion/SICSS_BAires_TP_Final_Esqueleto.ipynb)
con las secciones vacías para ordenarse.

La notebook [`SICSS_BAires_Desafio_Polarizacion_Noticias.ipynb`](consigna_desafio/clasificacion/SICSS_BAires_Desafio_Polarizacion_Noticias.ipynb)
es **una solución posible** (spoiler: no abrirla antes de resolver la consigna).
Clasifica comentarios de lectores del dataset
[`finiteautomata/news-argentina`](https://huggingface.co/datasets/finiteautomata/news-argentina)
con `pysentimiento` —las tareas `sentiment` y `emotion`, no `hate_speech` como en
`cap2/`— y **agrega** esas clasificaciones en un índice de polarización por noticia
de tres dimensiones: disenso de valencia (ratio positivos/negativos), violencia
emocional (ratio `anger`+`disgust` sobre el resto) y bimodalidad (dispersión
normalizada del score de sentimiento). Incluye Esteban-Ray (1994) como control de
robustez, bootstrap para justificar el mínimo de comentarios por noticia, y una
ponderación alternativa por componentes principales.

El punto pedagógico es el salto de unidad de análisis: en `cap2/` la unidad era el
texto y la pregunta era si el modelo acertaba; acá la clasificación es un insumo y lo
que se mide es una propiedad del colectivo.

- **Dependencias:** `pysentimiento`, `datasets`, `pandas`, `numpy`, `scikit-learn`,
  `matplotlib`, `seaborn`, `tqdm`.
- **Datos:** se descargan de HuggingFace; nada en `data/`.
- **Requiere GPU** (Colab). El costo se controla con `N_NOTICIAS`.

##### Opción B — `encuestas/`: polarización comparada con el World Values Survey

La [consigna](consigna_desafio/encuestas/consigna_trabajo_final_polarizacion_WVS_v3.md)
lleva la misma pregunta al terreno de las encuestas: **¿está América Latina más polarizada
que el resto del mundo?** Hay que construir una medida de polarización de actitudes
**comparable entre países** a partir del World Values Survey (ola 7, 2017-2022) y usarla
para responder.

El marco es el de DiMaggio, Evans y Bryson (1996), que descompone la polarización en
cuatro principios que pueden moverse en direcciones independientes:

| Principio | Qué mide |
|---|---|
| **Dispersión** | Cuánto se alejan las opiniones del promedio y entre sí |
| **Bimodalidad** | Si la distribución tiene dos picos y se vacía en el centro |
| **Restricción** | Si las actitudes sobre temas distintos se responden de forma coherente entre sí |
| **Consolidación** | Si las posiciones se alinean con la ideología declarada o con clivajes sociales |

En el taller ese esquema se aplica a Argentina con LAPOP; la consigna lo extiende a una
comparación internacional. Las decisiones abiertas son qué dominio de actitudes se mide y
con qué ítems, qué países entran, cómo se preparan los datos (no respuestas, escalas de
distinta amplitud, ítems invertidos, ponderadores), cómo se operacionaliza cada principio
y si los cuatro se combinan o no en un índice único.

- **Datos:** el archivo integrado de la ola 7 está versionado en
  [`consigna_desafio/encuestas/data/`](consigna_desafio/encuestas/data), en CSV y en RDS
  (~20 MB comprimido cada uno; el CSV pesa 190 MB al descomprimir), junto al
  [cuestionario maestro](<consigna_desafio/encuestas/data/F00010738-WVS-7_Master_Questionnaire_2017-2020_English (1).pdf>)
  en PDF. El libro de códigos todavía no está: se baja del
  [sitio de WVS](https://www.worldvaluessurvey.org/WVSDocumentationWV7.jsp).

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

`data/sicss-anotacion-unificado.json` contiene las anotaciones humanas del
ejercicio de discurso de odio de `cap3/`: 740 registros = 10 codificadores
(`coder_id`) × 74 tweets, con el esquema `HATEFUL`/`OFFENSIVE`/`CALLS` + 8
categorías temáticas. Se genera con `data/unify_anotaciones.py` a partir de
`data/sicss-anotacion-20260814T182433Z-1-001.zip` (10 JSON parciales, uno por
codificador); el script desambigua los archivos con `annotator == "anonymous"`
asignándoles un `coder_id` propio, ya que corresponden a personas distintas.

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
2. Abrir las notebooks de cada módulo en Google Colab/Drive, o las copias
   locales de `cap0/`–`cap3/` en Jupyter, para reproducir las prácticas.
3. Descomprimir los datasets de `data/` para las consignas hands-on de tópicos y
   transformers.
4. Elegir una de las dos consignas de `consigna_desafio/` para el trabajo final.

> Nota: las notebooks también circulan por Google Colab/Drive durante la cursada
> (ver tabla y links por capítulo arriba), y esas versiones pueden estar más
> actualizadas que las copias versionadas acá. Las traducciones a R están como
> `.Rmd` junto a la notebook de Python correspondiente.

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
├── consigna_desafio/   # Final assignment: two briefs to choose from
│   ├── clasificacion/   # Option A: polarization index over news comments
│   └── encuestas/   # Option B: comparative polarization with the World Values Survey
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
| [`cap0/`](cap0) | [`00 - SICSS-BAires - Topic Modeling.pdf`](<cap0/00 - SICSS-BAires - Topic Modeling.pdf>), [`00_SICSS_BAires_Vectorización.ipynb`](<cap0/00_SICSS_BAires_Vectorización.ipynb>), [`00_SICSS_BAires_Vectorización_R.Rmd`](<cap0/00_SICSS_BAires_Vectorización_R.Rmd>), [`ejemplo_clasificacion.ipynb`](cap0/ejemplo_clasificacion.ipynb) | Intro to NLP and topic modeling (LDA) | [M0](https://docs.google.com/presentation/d/1ZoOBD8BvoVZkAu_58hRxQe2xowutgVfrsGJo3tR4QeY/edit?usp=sharing) | [M0](https://drive.google.com/file/d/1dpL7G5Cp5Zpi3Rkzp1MrTSYRG_VjCAN0/view?usp=drive_link) |
| [`cap1/`](cap1) | [`01 - SICSS-BAires - Embeddings.pdf`](<cap1/01 - SICSS-BAires - Embeddings.pdf>), [`01_SICSS_BAires_Ilustracion_Embeddings.ipynb`](cap1/01_SICSS_BAires_Ilustracion_Embeddings.ipynb) | Static word embeddings (word2vec) | [M1](https://docs.google.com/presentation/d/1AQ9mwtzUg23ePFU37xi0usMqIVRizvyefeBVp8fatEY/edit?usp=sharing) | [M1](https://colab.research.google.com/drive/1UUr5TWTf1DR-U_QGNyFxaYhtA9Vj06WP?usp=sharing) |
| [`cap2/`](cap2) | [`02 -  SICSS - BAires - Transformers.pdf`](<cap2/02 -  SICSS - BAires - Transformers.pdf>), [`02_SICSS_BAires_Hate_Speech_con_pysentimiento.ipynb`](cap2/02_SICSS_BAires_Hate_Speech_con_pysentimiento.ipynb), [`02_SICSS_BAires_Transformers.ipynb`](cap2/02_SICSS_BAires_Transformers.ipynb), [`02_SICSS_BAires_Transformers_R.Rmd`](cap2/02_SICSS_BAires_Transformers_R.Rmd) | Transformer architecture and self-attention | [M2](https://docs.google.com/presentation/d/1WW7WRTLpKdnNJDQY3j9FnNpOSMYSC27IQILWU98lOoA/edit?usp=sharing) | [M2](https://colab.research.google.com/drive/1bTeXc6RHtIQaOcD0v1C5YTE2VKTQ-hlI?usp=sharing) |
| [`cap3/`](cap3) | [`03 - SICSS-Baires - LLMs.pdf`](<cap3/03 - SICSS-Baires - LLMs.pdf>), [`03_SICSS_Baires_LLMs.ipynb`](cap3/03_SICSS_Baires_LLMs.ipynb), [`03_SICSS_Baires_LLMs_R.Rmd`](cap3/03_SICSS_Baires_LLMs_R.Rmd), [`03_SICSS_Baires_LLMs_y_Anotación.ipynb`](<cap3/03_SICSS_Baires_LLMs_y_Anotación.ipynb>), [`03_SICSS_Baires_LLMS_Sesgos.ipynb`](cap3/03_SICSS_Baires_LLMS_Sesgos.ipynb), [`03_SICSS_Baires_Acuerdo_entre_Anotadores.ipynb`](cap3/03_SICSS_Baires_Acuerdo_entre_Anotadores.ipynb) | Large Language Models and prompt engineering | [M3](https://docs.google.com/presentation/d/1mtF_NDhC8dnK7CAWxcgTcdErfrcu2EPxe5JPe-L2yuE/edit?usp=sharing) | [Annotator agreement](cap3/03_SICSS_Baires_Acuerdo_entre_Anotadores.ipynb) |
| [`consigna_desafio/clasificacion/`](consigna_desafio/clasificacion) | [`CONSIGNA.md`](consigna_desafio/clasificacion/CONSIGNA.md), [`SICSS_BAires_TP_Final_Esqueleto.ipynb`](consigna_desafio/clasificacion/SICSS_BAires_TP_Final_Esqueleto.ipynb), [`SICSS_BAires_Desafio_Polarizacion_Noticias.ipynb`](consigna_desafio/clasificacion/SICSS_BAires_Desafio_Polarizacion_Noticias.ipynb) | **Final assignment, option A:** a polarization index over news comments | — | [Brief](consigna_desafio/clasificacion/CONSIGNA.md) · [Skeleton](consigna_desafio/clasificacion/SICSS_BAires_TP_Final_Esqueleto.ipynb) · [Solution](consigna_desafio/clasificacion/SICSS_BAires_Desafio_Polarizacion_Noticias.ipynb) |
| [`consigna_desafio/encuestas/`](consigna_desafio/encuestas) | [`consigna_trabajo_final_polarizacion_WVS_v3.md`](consigna_desafio/encuestas/consigna_trabajo_final_polarizacion_WVS_v3.md), [`data/`](consigna_desafio/encuestas/data) (WVS wave 7 + questionnaire) | **Final assignment, option B:** comparative polarization with the World Values Survey | — | [Brief](consigna_desafio/encuestas/consigna_trabajo_final_polarizacion_WVS_v3.md) |

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

The notebook [`01_SICSS_BAires_Ilustracion_Embeddings.ipynb`](cap1/01_SICSS_BAires_Ilustracion_Embeddings.ipynb)
shows how to use Spanish static word embeddings to detect cultural stereotypes
(gender, poverty) against dependent dimensions (sports, occupations, music,
etc.) by computing cosine distance between each dimension's average vector.

- **Dependencies:** `numpy`, `pandas`, `gensim`, `scipy`, `plotnine`.
- **External data:** the notebook automatically downloads the pretrained
  [SBWCE](https://cs.famaf.unc.edu.ar/~ccardellino/SBWCE/) embeddings
  (`SBW-vectors-300-min5`, ~1.5 GB) — they are not tracked in this repo.

- [Slides (Google Slides)](https://docs.google.com/presentation/d/1AQ9mwtzUg23ePFU37xi0usMqIVRizvyefeBVp8fatEY/edit?usp=sharing)
- [Notebook (Google Colab)](https://colab.research.google.com/drive/1UUr5TWTf1DR-U_QGNyFxaYhtA9Vj06WP?usp=sharing)

#### `cap2/` — Session 2: Transformers (32 slides + notebook)

From sequential models (RNNs) to Transformers: input/output embeddings,
self-attention (Query/Key/Value vectors), multi-head attention, and positional
encoding. Overview of GPT and BERT. Includes hands-on instructions using
`pysentimiento` on a comments dataset.

The notebook [`02_SICSS_BAires_Hate_Speech_con_pysentimiento.ipynb`](cap2/02_SICSS_BAires_Hate_Speech_con_pysentimiento.ipynb)
uses `pysentimiento`'s Spanish hate-speech model (a fine-tuned RoBERTuito) to
predict `HS` on the HatEval test split (`data/hateval_test_df.csv`), and
compares the result against the classical representations (TF, TF-IDF,
embeddings) from `cap0/`.

- **Dependencies:** `pysentimiento`, `transformers`, `torch`, `pandas`,
  `scikit-learn`, `matplotlib`, `seaborn`.
- **Data:** `data/hateval_test_df.csv` (already tracked in this repo).

- [Slides (Google Slides)](https://docs.google.com/presentation/d/1WW7WRTLpKdnNJDQY3j9FnNpOSMYSC27IQILWU98lOoA/edit?usp=sharing)
- [Notebook (Google Colab)](https://colab.research.google.com/drive/1bTeXc6RHtIQaOcD0v1C5YTE2VKTQ-hlI?usp=sharing)

#### `cap3/` — Session 3: How do we interact with an LLM? (52 slides)

Evolution of LLMs, when (not) to use them, their risks (hallucinations,
gender/racial/cultural/political/linguistic biases), and transfer
learning/fine-tuning. The second half is a hands-on **prompt engineering**
guide: roles (`system`/`user`), x-shot learning, and Chain of Thought (CoT)
prompting, with 6 guided exercises to practice with a conversational LLM.

- [Slides (Google Slides)](https://docs.google.com/presentation/d/1mtF_NDhC8dnK7CAWxcgTcdErfrcu2EPxe5JPe-L2yuE/edit?usp=sharing)

The notebook [`03_SICSS_Baires_Acuerdo_entre_Anotadores.ipynb`](cap3/03_SICSS_Baires_Acuerdo_entre_Anotadores.ipynb)
computes inter-annotator agreement metrics (observed agreement, Cohen's kappa,
Fleiss' kappa, Krippendorff's alpha, PABAK) on
`data/sicss-anotacion-unificado.json`, where 10 coders annotated the same set
of 74 tweets with the hate-speech schema used in
`03_SICSS_Baires_LLMs_y_Anotación.ipynb`. It serves as a realistic ceiling to
evaluate an LLM annotator against.

- **Dependencies:** `pandas`, `numpy`, `scikit-learn`, `statsmodels`,
  `matplotlib`, `seaborn`.
- **Data:** `data/sicss-anotacion-unificado.json`.

#### `consigna_desafio/` — Final assignment: polarization

The workshop closes with a final assignment that uses what was covered to answer a
substantive question rather than to teach a technique. There are **two briefs to choose
from**, one per methodological route; each group picks one. The deliverable is the same in
both: a roughly 10-minute presentation reviewing the methodological decisions and the main
results, with the analysis notebook as backup.

| Option | Brief | Question |
|---|---|---|
| **A. Classification** | [`clasificacion/CONSIGNA.md`](consigna_desafio/clasificacion/CONSIGNA.md) | Which news stories polarize their readers' conversation? |
| **B. Surveys** | [`encuestas/consigna_trabajo_final_polarizacion_WVS_v3.md`](consigna_desafio/encuestas/consigna_trabajo_final_polarizacion_WVS_v3.md) | Is Latin America more polarized than the rest of the world? |

##### Option A — `clasificacion/`: an article-level polarization index

The [brief](consigna_desafio/clasificacion/CONSIGNA.md) (in Spanish) asks for a
polarization index **at the article level**: a function that takes every comment an
article received and returns a number. It deliberately **does not say how to
operationalize polarization**: it poses seven open questions — what it might mean for an
article to be polarizing, how to make the index comparable across articles, how many
comments are enough for it to be valid, how to validate it — and each group decides the
methodological strategy. A
[skeleton notebook](consigna_desafio/clasificacion/SICSS_BAires_TP_Final_Esqueleto.ipynb)
with empty sections is provided to get organized.

The notebook [`SICSS_BAires_Desafio_Polarizacion_Noticias.ipynb`](consigna_desafio/clasificacion/SICSS_BAires_Desafio_Polarizacion_Noticias.ipynb)
is **one possible solution** (spoiler: do not open it before working through the brief).
It classifies reader comments from the
[`finiteautomata/news-argentina`](https://huggingface.co/datasets/finiteautomata/news-argentina)
dataset with `pysentimiento` — the `sentiment` and `emotion` tasks, not `hate_speech`
as in `cap2/` — and **aggregates** those classifications into a three-dimensional
per-article polarization index: valence dissent (positive/negative ratio), emotional
violence (`anger`+`disgust` over the rest) and bimodality (normalized dispersion of
the sentiment score). It includes Esteban-Ray (1994) as a robustness check, a
bootstrap justifying the minimum comments per article, and an alternative weighting
from principal components.

The pedagogical point is the shift in unit of analysis: in `cap2/` the unit was the
text and the question was whether the model was right; here classification is an input
and what gets measured is a property of the collective.

- **Dependencies:** `pysentimiento`, `datasets`, `pandas`, `numpy`, `scikit-learn`,
  `matplotlib`, `seaborn`, `tqdm`.
- **Data:** downloaded from HuggingFace; nothing in `data/`.
- **Requires a GPU** (Colab). Cost is controlled by `N_NOTICIAS`.

##### Option B — `encuestas/`: comparative polarization with the World Values Survey

The [brief](consigna_desafio/encuestas/consigna_trabajo_final_polarizacion_WVS_v3.md) (in
Spanish) takes the same question to survey data: **is Latin America more polarized than the
rest of the world?** It asks for a measure of attitude polarization that is **comparable
across countries**, built from the World Values Survey (wave 7, 2017-2022), and for using
it to answer.

The framework is DiMaggio, Evans and Bryson (1996), which breaks polarization into four
principles that can move in independent directions:

| Principle | What it measures |
|---|---|
| **Dispersion** | How far opinions sit from the mean and from each other |
| **Bimodality** | Whether the distribution has two peaks and empties out in the middle |
| **Constraint** | Whether attitudes on unrelated issues are answered coherently with one another |
| **Consolidation** | Whether positions align with declared ideology or with social cleavages |

The workshop applies that scheme to Argentina using LAPOP; this brief extends it to an
international comparison. The open decisions are which attitude domain gets measured and
with which items, which countries are included, how the data are prepared (missing answers,
scales of differing width, reverse-coded items, weights), how each principle is
operationalized, and whether the four are combined into a single index or not.

- **Data:** the wave 7 integrated file is tracked in
  [`consigna_desafio/encuestas/data/`](consigna_desafio/encuestas/data), as CSV and as RDS
  (~20 MB compressed each; the CSV is 190 MB once unzipped), alongside the
  [master questionnaire](<consigna_desafio/encuestas/data/F00010738-WVS-7_Master_Questionnaire_2017-2020_English (1).pdf>)
  in PDF. The codebook is not there yet: it is downloaded from the
  [WVS site](https://www.worldvaluessurvey.org/WVSDocumentationWV7.jsp).

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

`data/sicss-anotacion-unificado.json` holds the human annotations for the
`cap3/` hate-speech exercise: 740 records = 10 coders (`coder_id`) × 74
tweets, with the `HATEFUL`/`OFFENSIVE`/`CALLS` schema plus 8 topical
categories. It is generated by `data/unify_anotaciones.py` from
`data/sicss-anotacion-20260814T182433Z-1-001.zip` (10 partial JSON files, one
per coder); the script disambiguates the files with `annotator == "anonymous"`
by assigning each one its own `coder_id`, since they correspond to different
people.

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
2. Open each module's notebook in Google Colab/Drive, or the local copies in
   `cap0/`–`cap3/` in Jupyter, to reproduce the practices.
3. Unzip the datasets in `data/` for the topic-modeling and transformers
   hands-on exercises.
4. Pick one of the two briefs in `consigna_desafio/` for the final assignment.

> Note: the notebooks also circulate via Google Colab/Drive during the workshop
> (see the table and per-session links above), and those versions may be more
> up to date than the copies tracked here. R translations sit next to the
> corresponding Python notebook as `.Rmd` files.

### License

This repository is distributed under the [MIT](LICENSE) license.
