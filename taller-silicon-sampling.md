---
title: Taller de Silicon Sampling
description: LLMs para simular respuestas de encuesta
permalink: /taller-silicon-sampling/
---

# Taller de Silicon Sampling

20/08 (jueves), 9:00 a 18:00, a cargo de Elina Gómez y Germán Rosati.

## Qué es silicon sampling

El **silicon sampling** (muestreo de silicio) consiste en usar grandes modelos de
lenguaje (LLMs) para simular las respuestas que darían participantes humanos en
encuestas, experimentos o entrevistas. Al condicionar al modelo con perfiles
sociodemográficos (edad, género, educación, ideología, país, etc.), se generan
"muestras de silicio": encuestados sintéticos cuyas respuestas buscan aproximar las de
subpoblaciones humanas específicas. Se lo propone como un complemento rápido y de bajo
costo a la recolección de datos tradicional (para pilotear instrumentos, explorar
hipótesis o aproximar grupos difíciles de alcanzar), aunque su fiabilidad sigue en
debate: los modelos pueden reproducir sesgos sociales, aplanar la variabilidad interna
de los grupos y alinearse de manera desigual entre culturas e idiomas.

## Contenidos

El taller incluye dos análisis reproducibles de **sesgo de punto medio** en muestras de
silicio, con notebooks en Python/Colab (backends OpenAI y Ollama: `gpt-4o`,
`gpt-oss-20B`, `gpt-oss-120B`):

1. **Q130 de la World Values Survey** (ola 7): una escala ordinal de 4 puntos sin punto
   medio neutral. El sesgo se mide como concentración excesiva en las categorías
   interiores frente a las distribuciones empíricas de la WVS en Argentina, Uruguay y
   Estados Unidos, comparando dos versiones de prompt.
2. **Expresiones verbales de probabilidad**: réplica de la Etapa 1 del experimento
   "Quizás, quizás, quizás" (El Gato y La Caja / Decision-making Lab, University of
   Rochester), con una escala continua de 0 a 100 que sí tiene punto medio, comparando
   a los modelos contra una línea de base humana relevada por los propios participantes
   del taller.

## Material completo

Todo el material (notebooks, datos, diapositivas y bibliografía) vive en su propio
micrositio:

**[Ir al sitio del taller de Silicon Sampling](https://gefero.github.io/factor_data_silicon_tutorial/)**
