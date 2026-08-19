# Trabajo final

## Un índice de polarización a nivel noticia

**Taller de Procesamiento de Lenguaje Natural y polarización**
Summer Institute in Computational Social Sciences - Buenos Aires 2026
Factor~Data

---

## El problema
Todos tenemos una intuición de qué significa que una noticia "prenda fuego los
comentarios". El trabajo consiste en convertir esa intuición en un índice
que, dada una noticia y el conjunto de comentarios que recibió, diga cuán polarizada
quedó esa conversación.

Es un problema distinto al que veníamos resolviendo. Hasta ahora la unidad de análisis
era el texto: entraba un tuit, salía una etiqueta, y la pregunta era si el modelo
acertaba. Ahora, la clasificación no es el resultado sino el insumo. La unidad de
análisis pasa a ser la noticia.

Eso quiere decir que el trabajo que importa no es correr el modelo (es lo más fácil) sino decidir qué hacer con lo que el modelo devuelve.

## Los datos
[`finiteautomata/news-argentina`](https://huggingface.co/datasets/finiteautomata/news-argentina),
comentarios de lectores a noticias de medios argentinos.

```python
from datasets import load_dataset
ds = load_dataset("finiteautomata/news-argentina")
```

## Qué tienen que construir
Un índice de polarización a nivel noticia: una función que toma todos los
comentarios de una noticia y devuelve un número.

Algunas preguntas para pensar el desafío:

1. ¿Qué podría significar que una noticia sea "polarizante"?
2. ¿Cómo operacionalizar esa idea?
3. ¿Cómo hacer para que el índice sea comparable entre noticias?
4. ¿Cómo procesar el texto para extraer las señales de polarización
5. ¿Sobre qué cantidad de comentarios en cada noticia es posible construir un índice válido?
6. ¿Cómo validar el índice construído? (Van a tener que leer noticias a mano... piensen un criterio para seleccionarlas)
7. ¿Qué noticias (o grupo de noticias polarizan más)? 

## Entregable
- Una presentación oral de unos 10 minutos, con slides, que reseñe decisiones metodológicas y principales resultados
- La notebook con el análisis acompaña como respaldo, pero lo que se discute es la presentación.

Tengan en cuenta que clasificar los comentarios es lo que ya hicieron en `cap2/` con `pysentimiento`; no
gasten ahí más tiempo del necesario. Usen una muestra de noticias, no el corpus entero:
con GPU y unas doscientas noticias les alcanza de sobra, y les deja tiempo para lo que
importa.

Tienen un esqueleto de notebook en
[`SICSS_BAires_TP_Final_Esqueleto.ipynb`](SICSS_BAires_TP_Final_Esqueleto.ipynb) con las
secciones vacías, por si les sirve para ordenarse.


## Sobre la solución de referencia
En esta misma carpeta hay una notebook resuelta,
`SICSS_BAires_Desafio_Polarizacion_Noticias.ipynb`, que construye un índice posible (no necesariamente el mejor).
Sabemos que está ahí y ustedes también.

**No la abran hasta tener su propio índice andando.** No es una cuestión de honestidad
sino de que se pierden el trabajo: la parte que se aprende es equivocarse contra los
casos de prueba, y eso no se puede leer, hay que hacerlo.

Después de terminar, ábranla y comparen. 