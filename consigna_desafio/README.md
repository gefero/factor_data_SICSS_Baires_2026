# Desafío: índice de polarización en comentarios de noticias

**[Español](#español) · [English](#english)**

---

## Español

Consigna integradora del taller. A diferencia de las notebooks de `cap0/`–`cap3/`,
que enseñan una técnica por vez, acá se usa lo visto para responder una pregunta
sustantiva: **¿qué noticias polarizan la conversación de sus lectores?**

### La notebook

[`SICSS_BAires_Desafio_Polarizacion_Noticias.ipynb`](SICSS_BAires_Desafio_Polarizacion_Noticias.ipynb)

Toma el dataset [`finiteautomata/news-argentina`](https://huggingface.co/datasets/finiteautomata/news-argentina)
(comentarios de lectores a noticias de medios argentinos), clasifica cada comentario
con [`pysentimiento`](https://github.com/pysentimiento/pysentimiento) —las tareas
`sentiment` y `emotion`, no `hate_speech` como en `cap2/`— y **agrega** esas
clasificaciones en un índice por noticia.

El punto pedagógico es el salto de unidad de análisis: en `cap2/` la unidad era el
texto y la pregunta era si el modelo acertaba; acá la clasificación es un insumo y
lo que se mide es una propiedad del colectivo. Un comentario no es polarizado; una
conversación sí.

### El índice

| Dimensión | Fórmula | Qué mide |
|---|---|---|
| **D1** — disenso de valencia | $1 - \|(n_{pos} - n_{neg}) / (n_{pos} + n_{neg})\|$ | Cuán dividida está la sección entre positivos y negativos |
| **D2** — violencia emocional | $n_{viol} / (n_{viol} + n_{noviol})$ | Qué proporción de la emoción marcada es hostil (`anger`, `disgust`) |
| **D3** — bimodalidad | $\mathrm{Var}(s) / (1 - \bar{s}^2)$ | Cuánto se concentra la opinión en los extremos en vez del centro |

con $s = P(\text{POS}) - P(\text{NEG})$ por comentario. El índice compuesto es el
promedio simple de las tres, y la notebook discute explícitamente que esa ponderación
es una decisión (la compara contra una derivada por componentes principales).

D3 es la que hace el trabajo conceptual: sin ella, una noticia donde todos putean al
mismo actor —negativa y unánime— quedaría marcada como polarizada. Sentimiento
negativo no es polarización.

Como control de robustez se calcula también el índice de **Esteban-Ray** (1994) sobre
las tres clases discretas, y se comparan los dos ordenamientos.

### Cómo correrla

Abrila en **Google Colab con GPU** (`Entorno de ejecución > Cambiar tipo de entorno de
ejecución > GPU`). Sin GPU la predicción sobre varios miles de comentarios pasa de un
par de minutos a bastante más de media hora.

El costo lo controla `N_NOTICIAS`, en la celda de parámetros al principio (200 por
defecto). Si vas a correrla en CPU, bajalo a 30 o 40.

- **Dependencias:** `pysentimiento`, `datasets`, `pandas`, `numpy`, `scikit-learn`,
  `matplotlib`, `seaborn`, `tqdm`. La notebook las instala sola en la primera celda.
- **Datos:** se bajan de HuggingFace, no hay nada en `data/`.

### Nota sobre el dataset

La notebook detecta los nombres de columna automáticamente (diccionario `COLS`), así
que tolera cambios de esquema y se puede apuntar a otro corpus de comentarios tocando
una sola celda. Si `finiteautomata/news-argentina` no tuviera la estructura
noticia → comentarios que el índice necesita, el reemplazo directo es
[`piuba-bigdata/contextualized_hate_speech`](https://huggingface.co/datasets/piuba-bigdata/contextualized_hate_speech),
del mismo autor.

---

## English

Capstone assignment for the workshop. Unlike the `cap0/`–`cap3/` notebooks, which
each teach one technique, this one uses them to answer a substantive question:
**which news stories polarize their readers' conversation?**

### The notebook

[`SICSS_BAires_Desafio_Polarizacion_Noticias.ipynb`](SICSS_BAires_Desafio_Polarizacion_Noticias.ipynb)

It takes the [`finiteautomata/news-argentina`](https://huggingface.co/datasets/finiteautomata/news-argentina)
dataset (reader comments on Argentine news outlets), classifies each comment with
[`pysentimiento`](https://github.com/pysentimiento/pysentimiento) — the `sentiment`
and `emotion` tasks, not `hate_speech` as in `cap2/` — and **aggregates** those
classifications into a per-article index.

The pedagogical point is the shift in unit of analysis: in `cap2/` the unit was the
text and the question was whether the model was right; here classification is an
input, and what gets measured is a property of the collective. A single comment is
not polarized; a conversation is.

### The index

| Dimension | Formula | What it measures |
|---|---|---|
| **D1** — valence dissent | $1 - \|(n_{pos} - n_{neg}) / (n_{pos} + n_{neg})\|$ | How split the comment section is between positive and negative |
| **D2** — emotional violence | $n_{viol} / (n_{viol} + n_{nonviol})$ | What share of marked emotion is hostile (`anger`, `disgust`) |
| **D3** — bimodality | $\mathrm{Var}(s) / (1 - \bar{s}^2)$ | How much opinion clusters at the extremes rather than the centre |

with $s = P(\text{POS}) - P(\text{NEG})$ per comment. The composite index is their
simple average, and the notebook makes explicit that this weighting is a decision
(comparing it against one derived from principal components).

D3 does the conceptual work: without it, an article where everyone piles on the same
target — negative and unanimous — would be flagged as polarized. Negative sentiment
is not polarization.

As a robustness check the **Esteban-Ray** (1994) index is also computed over the three
discrete classes, and the two rankings are compared.

### How to run it

Open it in **Google Colab with GPU** (`Runtime > Change runtime type > GPU`). Without
a GPU, predicting over several thousand comments goes from a couple of minutes to well
over half an hour.

Cost is controlled by `N_NOTICIAS` in the parameters cell at the top (200 by default).
Drop it to 30 or 40 if you are running on CPU.

- **Dependencies:** `pysentimiento`, `datasets`, `pandas`, `numpy`, `scikit-learn`,
  `matplotlib`, `seaborn`, `tqdm`. The notebook installs them in its first cell.
- **Data:** downloaded from HuggingFace; nothing is stored in `data/`.

### Note on the dataset

The notebook auto-detects column names (the `COLS` dictionary), so it tolerates schema
changes and can be pointed at another comment corpus by editing a single cell. Should
`finiteautomata/news-argentina` not have the article → comments structure the index
needs, the drop-in replacement is
[`piuba-bigdata/contextualized_hate_speech`](https://huggingface.co/datasets/piuba-bigdata/contextualized_hate_speech),
by the same author.
