# Trabajo final

## Un índice de polarización a nivel noticia

**Taller de Procesamiento de Lenguaje Natural y polarización**
Summer Institute in Computational Social Sciences - Buenos Aires 2026
Factor~Data

---

## El problema

Todos tenemos una intuición de qué significa que una noticia "prenda fuego los
comentarios". El trabajo consiste en convertir esa intuición en un **número**: un índice
que, dada una noticia y el conjunto de comentarios que recibió, diga cuán polarizada
quedó esa conversación.

Es un problema distinto al que veníamos resolviendo. Hasta ahora la unidad de análisis
era el texto: entraba un tuit, salía una etiqueta, y la pregunta era si el modelo
acertaba. Acá **la clasificación no es el resultado sino el insumo**. La unidad de
análisis pasa a ser la noticia, y lo que hay que medir es una propiedad que ningún
comentario individual tiene por sí solo. Un comentario no es polarizado. Una conversación
sí puede serlo.

Eso quiere decir que el trabajo que importa no es correr el modelo —eso ya lo saben
hacer— sino **decidir qué hacer con lo que el modelo devuelve**.

## Los datos

[`finiteautomata/news-argentina`](https://huggingface.co/datasets/finiteautomata/news-argentina),
comentarios de lectores a noticias de medios argentinos.

```python
from datasets import load_dataset
ds = load_dataset("finiteautomata/news-argentina")
```

No les vamos a describir el esquema. Ábranlo, mírenlo, y decidan ustedes qué columnas les
sirven y cuáles no. Parte del trabajo es esa.

## Qué tienen que construir

Un índice de polarización **a nivel noticia**. Es decir: una función que toma todos los
comentarios de una noticia y devuelve un número.

Tres requisitos, y ninguno les dice cómo:

1. **Tiene que ser comparable entre noticias.** Si la noticia X da 0,8 y la noticia Y da
   0,3, esa diferencia tiene que significar algo, y tienen que poder explicar qué.

2. **Tiene que combinar más de una señal del texto.** Una sola medida no alcanza para
   capturar algo tan cargado como "polarización". Cuántas señales usan y cuáles, lo
   deciden ustedes.

3. **Tiene que estar definido solo para las noticias que superen un mínimo de
   comentarios**, y ese mínimo lo fijan ustedes con algún criterio que puedan defender.
   "Nos pareció razonable" no es un criterio.

## Los casos de prueba

Acá está el corazón del trabajo. Imaginen cuatro noticias, cada una con cien comentarios:

| | Cómo son sus comentarios |
|---|---|
| **A** | Mitad elogios encendidos, mitad insultos |
| **B** | Todos tibios. Nadie se juega por nada |
| **C** | Casi todos critican, y critican lo mismo |
| **D** | Mitad a favor y mitad en contra, pero todos moderados |

**Su índice tiene que asignarle valores distintos a A, B, C y D**, y ustedes tienen que
mostrar que lo hace. No alcanza con afirmarlo: constrúyanse los casos —pueden ser
sintéticos, no hace falta que salgan del dataset— y pasen su índice por ellos.

Presten atención especial a dos comparaciones:

- **A contra C.** Las dos secciones tienen mucha carga negativa. ¿Su índice las
  distingue? ¿Debería?
- **A contra D.** Las dos están partidas al medio en la misma proporción. ¿Su índice las
  distingue? ¿Debería?

Si alguno de esos pares les resulta difícil de separar, **eso es un hallazgo, no un
fracaso**. Es probablemente lo más interesante que les va a pasar en las seis horas.
Cuéntenlo en la presentación.

## Lo que la presentación tiene que contestar

No hay una lista de pasos a seguir. Hay preguntas que su trabajo tiene que poder
responder:

1. **¿Qué decidieron que es polarización, y qué quedó afuera de esa definición?** Toda
   definición recorta. Digan qué recortaron.

2. **¿Qué señales del texto usaron, y por qué esas y no otras?** ¿Qué descartaron en el
   camino, y por qué?

3. **¿Cuántos comentarios hacen falta para que el número sea creíble?** ¿Cómo lo
   establecieron?

4. **¿Cómo sabemos que su índice mide lo que ustedes dicen que mide?** Esta es la
   pregunta difícil. Piensen qué evidencia los convencería a ustedes si se la presentara
   otro grupo.

5. **¿Cuál es la decisión más frágil que tomaron?** Es decir: si la hubieran tomado
   distinto, ¿cuánto cambiaría el resultado? Muéstrenlo, no lo supongan.

6. **¿Qué noticias polarizan más, y qué tienen en común?** El hallazgo sustantivo. Es
   para lo que construyeron todo lo anterior.

## Dos cosas que conviene no saltearse

**Antes de mostrar un ranking, lean los comentarios.** Los de la noticia que les quedó
primera y los de la que les quedó última. Si al leerlos no ven lo que su índice dice que
hay ahí, tienen un problema — y encontrarlo ustedes es mucho mejor que encontrarlo
durante la presentación.

**No traten igual el índice de una noticia con 15 comentarios que el de una con 900.**
Piensen qué significa eso para las comparaciones que quieran hacer.

## La presentación

- **Grupos de 3 o 4 personas.**
- **8 a 10 minutos**, con slides. Breve: no es una clase, es una defensa.
- La notebook con el análisis acompaña como respaldo, pero lo que se discute es la
  presentación.

Tiene que estar sí o sí:

- Su definición de polarización, en una frase.
- Cómo quedó armado el índice.
- La evidencia de los casos de prueba.
- El hallazgo sustantivo.
- La decisión más frágil.

No hace falta que el índice sea "el correcto" — no existe. Hace falta que puedan
defenderlo, y que sepan dónde flaquea.

## Cronograma sugerido

Seis horas alcanzan si no se quedan trabados en la parte que ya saben hacer.

| Tramo | Trabajo |
|---|---|
| 0:00 – 0:30 | Explorar los datos y acordar en grupo qué van a llamar polarización |
| 0:30 – 1:15 | Clasificar los comentarios. Dejen corriendo la inferencia mientras siguen discutiendo lo anterior |
| 1:15 – 3:00 | Construir el índice e iterar contra los casos de prueba |
| 3:00 – 4:00 | Validar: leer comentarios, ver qué tan estable es el número |
| 4:00 – 5:00 | El análisis sustantivo |
| 5:00 – 6:00 | Armar la presentación |

Clasificar los comentarios es lo que ya hicieron en `cap2/` con `pysentimiento`; no
gasten ahí más tiempo del necesario. Usen una muestra de noticias, no el corpus entero:
con GPU y unas doscientas noticias les alcanza de sobra, y les deja tiempo para lo que
importa.

Tienen un esqueleto de notebook en
[`SICSS_BAires_TP_Final_Esqueleto.ipynb`](SICSS_BAires_TP_Final_Esqueleto.ipynb) con las
secciones vacías, por si les sirve para ordenarse.

---

## Sobre la solución de referencia

En esta misma carpeta hay una notebook resuelta,
`SICSS_BAires_Desafio_Polarizacion_Noticias.ipynb`, que construye un índice posible.
Sabemos que está ahí y ustedes también.

**No la abran hasta tener su propio índice andando.** No es una cuestión de honestidad
sino de que se pierden el trabajo: la parte que se aprende es equivocarse contra los
casos de prueba, y eso no se puede leer, hay que hacerlo.

Después de terminar, ábranla. Comparen. Si su índice difiere del de referencia, la
pregunta interesante no es cuál está bien —ninguno de los dos es "el correcto"— sino en
qué se diferencian las decisiones que tomaron y qué consecuencias tuvo cada una. Si
llegan a eso, la presentación se vuelve bastante más interesante.
