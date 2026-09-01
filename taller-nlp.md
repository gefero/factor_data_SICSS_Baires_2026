---
title: Taller de Procesamiento de Lenguaje Natural
description: NLP para investigación en ciencias sociales
permalink: /taller-nlp/
---

![Logos Factor~Data y SICSS]({{ site.repo_raw }}/imgs/logo_final_conjunto.png)

# Taller de Procesamiento de Lenguaje Natural

## Docentes
- [Germán Rosati](https://gefero.github.io/)
- [Juan Manuel Pérez](https://www.linkedin.com/in/perezjuanma/)
- [Tomás Maguire](https://www.linkedin.com/in/tomasebm/)

## Ayudante
- Román Fernández Arias

## Presentación
Este taller es una introducción práctica al **Procesamiento de Lenguaje Natural (NLP)**
para la investigación en ciencias sociales, dictado en el **Summer Institute in
Computational Social Sciences (SICSS) - Buenos Aires** por
**[Factor~Data](https://factor-data.netlify.app/)**.

Se propone que las y los asistentes:
- comprendan conceptos metodológicos fundamentales para el preprocesamiento de datos
  textuales (tokenización, lematización, stemming, etc.) y la representación vectorial
  clásica de textos (Document-Term Matrix, Bag of Words, etc.);
- se introduzcan a técnicas modernas de representación vectorial de textos (word
  embeddings, word2vec);
- incorporen nociones básicas de la arquitectura Transformer (mecanismo de atención,
  positional encoding, etc.);
- se familiaricen con conceptos centrales de prompting (roles, instrucciones) y con los
  riesgos y usos de los Large Language Models (LLMs).

Todo el material local de este taller (diapositivas, notebooks y traducciones a R) está
en [`taller_nlp/`]({{ site.repo }}/tree/main/taller_nlp) en el repositorio.

## Contenidos y materiales

### M0. Vectorizando un corpus
Qué es NLP y el problema del dato no estructurado, un flujo de trabajo "típico" en NLP
(limpieza de texto, stopwords, tokenización, stemming vs. lematización), representación
matemática de un texto (Document-Term Matrix, Bag of Words) y modelado de tópicos con
Latent Dirichlet Allocation (LDA).

- [Diapositivas (Google Slides)](https://docs.google.com/presentation/d/1ZoOBD8BvoVZkAu_58hRxQe2xowutgVfrsGJo3tR4QeY/edit?usp=sharing) · [PDF]({{ site.repo_raw }}/taller_nlp/cap0/00%20-%20SICSS-BAires%20-%20Vectorizaci%C3%B3n.pdf)
- [Notebook - Práctica guiada (Google Drive)](https://drive.google.com/file/d/1CjMq7aKPH_P_mFDEtRlNgLUFpanNnzNQ/view?usp=sharing) · [notebook]({{ site.repo_raw }}/taller_nlp/cap0/00_SICSS_BAires_Vectorizaci%C3%B3n.ipynb) · [versión en R]({{ site.repo_raw }}/taller_nlp/cap0/00_SICSS_BAires_Vectorizaci%C3%B3n_R.Rmd)
- [Notebook - Ejemplo de clasificación]({{ site.repo_raw }}/taller_nlp/cap0/ejemplo_clasificacion.ipynb)

### M1. Acercamiento a los word embeddings
Semántica léxica y semántica vectorial, matrices de co-ocurrencia palabra-contexto,
similitud coseno, la intuición de word2vec (skip-gram, negative sampling) y aplicaciones
en ciencias sociales (detección de estereotipos, trayectorias).

- [Diapositivas (Google Slides)](https://docs.google.com/presentation/d/1AQ9mwtzUg23ePFU37xi0usMqIVRizvyefeBVp8fatEY/edit?usp=sharing) · [PDF]({{ site.repo_raw }}/taller_nlp/cap1/01%20-%20SICSS-BAires%20-%20Embeddings.pdf)
- [Notebook - Práctica guiada (Colab)](https://colab.research.google.com/drive/1UUr5TWTf1DR-U_QGNyFxaYhtA9Vj06WP?usp=sharing) · [notebook]({{ site.repo_raw }}/taller_nlp/cap1/01_SICSS_BAires_Ilustracion_Embeddings.ipynb)

### M2. Transformers
De los modelos secuenciales (RNN) a los Transformers: embeddings de entrada/salida,
self-attention (Query/Key/Value), atención multicabezal y positional encoding. Reseña de
GPT y BERT.

- [Diapositivas (Google Slides)](https://docs.google.com/presentation/d/1WW7WRTLpKdnNJDQY3j9FnNpOSMYSC27IQILWU98lOoA/edit?usp=sharing) · [PDF]({{ site.repo_raw }}/taller_nlp/cap2/02%20-%20%20SICSS%20-%20BAires%20-%20Transformers.pdf)
- [Notebook - Práctica guiada transformers (Colab)](https://colab.research.google.com/drive/1bTeXc6RHtIQaOcD0v1C5YTE2VKTQ-hlI?usp=sharing) · [notebook]({{ site.repo_raw }}/taller_nlp/cap2/02_SICSS_BAires_Transformers.ipynb) · [versión en R]({{ site.repo_raw }}/taller_nlp/cap2/02_SICSS_BAires_Transformers_R.Rmd)
- [Notebook - Práctica guiada pysentimiento (Google Drive)](https://drive.google.com/file/d/1ZY0OXzECcuvfYPBC6bFxyPByO9osRa6O/view?usp=sharing) · [notebook]({{ site.repo_raw }}/taller_nlp/cap2/02_SICSS_BAires_Hate_Speech_con_pysentimiento.ipynb)

### M3. ¿Cómo interactuamos con un LLM?
Evolución de los LLMs, para qué (no) conviene usarlos, sus riesgos (alucinaciones,
sesgos) y transfer learning/fine-tuning. Guía práctica de prompt engineering: roles
(`system`/`user`), x-shot learning y Chain of Thought (CoT). Usos posibles de los LLMs:
clasificación, anotación. Sesgos y estereotipos en LLMs.

- [Diapositivas - Intro LLMs (Google Slides)](https://docs.google.com/presentation/d/1mtF_NDhC8dnK7CAWxcgTcdErfrcu2EPxe5JPe-L2yuE/edit?usp=sharing) · [PDF]({{ site.repo_raw }}/taller_nlp/cap3/03%20-%20SICSS-Baires%20-%20LLMs.pdf)
- [Notebook - Práctica guiada Intro LLMs (Google Drive)](https://drive.google.com/file/d/1cFBVP9pZveZORl1cqn6-t54jz2VJry0D/view?usp=sharing) · [notebook]({{ site.repo_raw }}/taller_nlp/cap3/03_SICSS_Baires_LLMs.ipynb) · [versión en R]({{ site.repo_raw }}/taller_nlp/cap3/03_SICSS_Baires_LLMs_R.Rmd)
- [Diapositivas - LLMs y anotación (Google Slides)](https://docs.google.com/presentation/d/1sDPwu6nCDt8CGr5jmqxcMTUcNvjjdfaMqDAj19RLjck/edit?usp=sharing) · [PDF]({{ site.repo_raw }}/taller_nlp/cap3/03%20-%20SICSS-Baires%20-%20LLMs%20y%20Anotaci%C3%B3n.pdf)
- [Notebook - Práctica guiada LLMs y anotación (Colab)](https://colab.research.google.com/drive/1RdQxYVqEIFTEHohsq1zVbmB9tML05iUz?usp=sharing) · [notebook]({{ site.repo_raw }}/taller_nlp/cap3/03_SICSS_Baires_LLMs_y_Anotaci%C3%B3n.ipynb)
- [Notebook - Acuerdo entre anotadores]({{ site.repo_raw }}/taller_nlp/cap3/03_SICSS_Baires_Acuerdo_entre_Anotadores.ipynb) — métricas de acuerdo inter-anotador (kappa de Cohen, kappa de Fleiss, alfa de Krippendorff) sobre las anotaciones humanas de discurso de odio, como techo realista contra el que evaluar a un LLM anotador
- [Diapositivas - LLMs y sesgos (Google Slides)](https://docs.google.com/presentation/d/1tkrYcqOefaGM8_ZAYeVC4hf7tlV92TYa8uEpgysgCvU/edit?usp=sharing) · [PDF]({{ site.repo_raw }}/taller_nlp/cap3/03%20-%20SICSS-Baires%20-%20LLMs%20y%20sesgos.pdf)
- [Notebook - Práctica guiada LLMs y sesgos (Colab)](https://colab.research.google.com/drive/15v5kDWl8dQJY9pL1kMZk4zHxz1yK2C2n?usp=sharing) · [notebook]({{ site.repo_raw }}/taller_nlp/cap3/03_SICSS_Baires_LLMS_Sesgos.ipynb)

## Datos

Los datasets de tweets y de anotación usados en las prácticas están en
[`data/`]({{ site.repo }}/tree/main/data): dos corpus de tweets de la campaña electoral
argentina 2023 (`tweets_candidatos.zip`, `tweets_menciones.zip`), los splits de HatEval
en español y las anotaciones unificadas de discurso de odio. Al clonar el repo, las
notebooks los leen automáticamente desde ahí.

## Trabajo final

El taller cierra con un trabajo final sobre polarización, con dos consignas a elección —
ver la [página del desafío]({{ '/desafio/' | relative_url }}).
