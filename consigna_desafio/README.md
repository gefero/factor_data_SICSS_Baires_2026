# Trabajo final: índice de polarización en comentarios de noticias

**[Español](#español) · [English](#english)**

---

## Español

Consigna integradora del taller. A diferencia de las notebooks de `cap0/`–`cap3/`, que
enseñan una técnica por vez, acá se usa lo visto para responder una pregunta sustantiva:
**¿qué noticias polarizan la conversación de sus lectores?**

### Empezar por acá

| Archivo | Qué es |
|---|---|
| [`CONSIGNA.md`](CONSIGNA.md) | **El enunciado del trabajo final.** Empezá por acá |
| [`SICSS_BAires_TP_Final_Esqueleto.ipynb`](SICSS_BAires_TP_Final_Esqueleto.ipynb) | Esqueleto de notebook con las secciones vacías, para ordenarse |

El trabajo pide construir un índice de polarización **a nivel noticia** a partir de los
comentarios que cada noticia recibió, clasificados con
[`pysentimiento`](https://github.com/pysentimiento/pysentimiento). Se resuelve en unas
6 horas, en grupos de 3 o 4, y se entrega como una presentación breve.

La consigna deliberadamente **no dice cómo operacionalizar la polarización**: da
requisitos y casos de prueba que el índice tiene que saber distinguir, y la estrategia
metodológica la deciden los grupos.

El punto pedagógico es el salto de unidad de análisis: en `cap2/` la unidad era el texto
y la pregunta era si el modelo acertaba; acá la clasificación es un insumo y lo que se
mide es una propiedad del colectivo. Un comentario no es polarizado; una conversación sí.

### Datos

[`finiteautomata/news-argentina`](https://huggingface.co/datasets/finiteautomata/news-argentina),
comentarios de lectores a noticias de medios argentinos. Se descarga desde la notebook;
no hay nada en `data/`.

- **Dependencias:** `pysentimiento`, `datasets`, `pandas`, `numpy`, `scikit-learn`,
  `matplotlib`, `seaborn`, `tqdm`.
- **Requiere GPU** (Colab). Sin GPU, la inferencia sobre varios miles de comentarios pasa
  de un par de minutos a bastante más de media hora.

---

### Solución de referencia

> **Spoiler.** [`SICSS_BAires_Desafio_Polarizacion_Noticias.ipynb`](SICSS_BAires_Desafio_Polarizacion_Noticias.ipynb)
> es **una solución posible** del trabajo, comentada en detalle. Si vas a resolver la
> consigna, no la abras hasta tener tu propio índice andando: la parte que se aprende es
> equivocarse contra los casos de prueba, y eso no se puede leer.

Construye un índice de tres dimensiones —disenso de valencia, violencia emocional y
bimodalidad del sentimiento—, incluye el índice de Esteban-Ray (1994) como control de
robustez, un bootstrap que justifica el mínimo de comentarios por noticia, y una
ponderación alternativa por componentes principales. Detecta los nombres de columna del
dataset automáticamente, así que tolera cambios de esquema y se puede apuntar a otro
corpus de comentarios tocando una sola celda.

No es "la" respuesta: es una entre varias defendibles. La comparación entre el índice
propio y este es un buen cierre del trabajo.

---

## English

Capstone assignment for the workshop. Unlike the `cap0/`–`cap3/` notebooks, which each
teach one technique, this one uses them to answer a substantive question: **which news
stories polarize their readers' conversation?**

### Start here

| File | What it is |
|---|---|
| [`CONSIGNA.md`](CONSIGNA.md) | **The assignment brief** (in Spanish). Start here |
| [`SICSS_BAires_TP_Final_Esqueleto.ipynb`](SICSS_BAires_TP_Final_Esqueleto.ipynb) | Skeleton notebook with empty sections, to get organized |

The assignment asks for a polarization index **at the article level**, built from the
comments each article received, classified with
[`pysentimiento`](https://github.com/pysentimiento/pysentimiento). It takes about
6 hours, in groups of 3 or 4, and is handed in as a short presentation.

The brief deliberately **does not say how to operationalize polarization**: it gives
requirements and test cases the index must tell apart, and each group decides the
methodological strategy.

The pedagogical point is the shift in unit of analysis: in `cap2/` the unit was the text
and the question was whether the model was right; here classification is an input, and
what gets measured is a property of the collective. A single comment is not polarized;
a conversation is.

### Data

[`finiteautomata/news-argentina`](https://huggingface.co/datasets/finiteautomata/news-argentina),
reader comments on Argentine news outlets. Downloaded from the notebook; nothing is
stored in `data/`.

- **Dependencies:** `pysentimiento`, `datasets`, `pandas`, `numpy`, `scikit-learn`,
  `matplotlib`, `seaborn`, `tqdm`.
- **Requires a GPU** (Colab). Without one, predicting over several thousand comments goes
  from a couple of minutes to well over half an hour.

---

### Reference solution

> **Spoiler.** [`SICSS_BAires_Desafio_Polarizacion_Noticias.ipynb`](SICSS_BAires_Desafio_Polarizacion_Noticias.ipynb)
> is **one possible solution**, commented in detail. If you are going to work through the
> assignment, do not open it until your own index runs: the part you learn from is
> getting the test cases wrong, and that cannot be read.

It builds a three-dimensional index — valence dissent, emotional violence and sentiment
bimodality — includes the Esteban-Ray (1994) index as a robustness check, a bootstrap
justifying the minimum comments per article, and an alternative weighting from principal
components. It auto-detects the dataset's column names, so it tolerates schema changes
and can be pointed at another comment corpus by editing a single cell.

It is not "the" answer: it is one among several defensible ones. Comparing your own index
against it makes for a good closing section.
