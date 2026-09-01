---
title: Trabajo final
description: Desafío de polarización — dos consignas a elección
permalink: /desafio/
---

# Trabajo final

El taller cierra con un trabajo final que integra lo visto en los módulos anteriores
para responder una pregunta sustantiva sobre **polarización**, en vez de enseñar una
técnica más. Hay **dos consignas a elección**, una por camino metodológico; cada grupo
elige una. Se resuelve en unas 6 horas y se entrega como una presentación de unos 10
minutos que reseñe las decisiones metodológicas y los principales resultados, con la
notebook del análisis como respaldo.

| Opción | Pregunta | Camino |
|---|---|---|
| **A. Clasificación** | ¿Qué noticias polarizan la conversación de sus lectores? | Taller de NLP |
| **B. Encuestas** | ¿Está América Latina más polarizada que el resto del mundo? | Taller de encuestas |

## Opción A — Un índice de polarización en comentarios de noticias

Hay que construir un índice de polarización **a nivel noticia** a partir de los
comentarios que cada una recibió, clasificados con `pysentimiento`. El eje del ejercicio
es el salto de unidad de análisis —del texto individual a la conversación— y las
decisiones metodológicas que ese salto obliga a tomar: la consigna no dice cómo
operacionalizar la polarización, sino que plantea las preguntas que el trabajo tiene que
contestar.

- [Consigna]({{ site.repo }}/blob/main/consignas_desafio/clasificacion/CONSIGNA.md)
- [Esqueleto de notebook]({{ site.repo }}/blob/main/consignas_desafio/clasificacion/SICSS_BAires_TP_Final_Esqueleto.ipynb)
- [Solución de referencia]({{ site.repo }}/blob/main/consignas_desafio/clasificacion/SICSS_BAires_Desafio_Polarizacion_Noticias.ipynb) (spoiler: no abrirla antes de resolver)

## Opción B — Polarización comparada: América Latina y el mundo (World Values Survey)

La misma pregunta, en el terreno de las encuestas. Hay que construir una medida de
polarización de actitudes comparable entre países a partir del World Values Survey (ola
7, 2017-2022), aplicando los cuatro principios de DiMaggio, Evans y Bryson (1996) que en
el taller se usaron con Argentina y LAPOP.

- [Consigna]({{ site.repo }}/blob/main/consignas_desafio/encuestas/consigna_trabajo_final_polarizacion_WVS_v3.md)
- Datos, con descarga directa: [CSV]({{ site.repo_raw }}/consignas_desafio/encuestas/data/F00011356-WVS_Cross-National_Wave_7_csv_v6_0.zip) (21 MB) · [RDS]({{ site.repo_raw }}/consignas_desafio/encuestas/data/F00011421-WVS_Cross-National_Wave_7_rds_v6_0.zip) (19 MB) · [cuestionario maestro (PDF)]({{ site.repo_raw }}/consignas_desafio/encuestas/data/F00010738-WVS-7_Master_Questionnaire_2017-2020_English%20%281%29.pdf)

## Lo que produjeron los grupos

Cuatro presentaciones de trabajos finales de ediciones anteriores, como muestra de lo
que se puede construir con estas consignas:

| Presentación | Grupo |
|---|---|
| [El pulso de los comentarios — un índice de polarización a nivel noticia]({{ site.repo_raw }}/consignas_desafio/presentaciones_asistentes/01_presentacion_polarizacion.pdf) | — |
| [Polarización en la conversación digital — comentarios a noticias de medios oficiales en Twitter]({{ site.repo_raw }}/consignas_desafio/presentaciones_asistentes/02_propuesta_polarizacion.pdf) | De Villalobos · Estévez Leston · Gomez Vargas · Nielsen |
| [Un índice de polarización a nivel comentario]({{ site.repo_raw }}/consignas_desafio/presentaciones_asistentes/03_proyecto%20final%20sicss.pdf) | Amado · Cellone · Marcantonio · Gallo · Morales |
| [Índice de polarización a nivel noticia]({{ site.repo_raw }}/consignas_desafio/presentaciones_asistentes/04_presentacion_polarizacion.pdf) | Abarzúa · Franco · García Migliore · Guerrisi · Riganti |
