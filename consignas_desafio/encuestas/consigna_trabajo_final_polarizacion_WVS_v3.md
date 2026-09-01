# Trabajo final — Taller de encuestas

## Polarización comparada: América Latina y el mundo (World Values Survey)

**Taller de Procesamiento de Lenguaje Natural y polarización**
Summer Institute in Computational Social Sciences - Buenos Aires 2026
Factor~Data

---

## El problema

"Polarización" nombra al menos cuatro propiedades distintas de una distribución de actitudes, que pueden moverse en direcciones independientes (DiMaggio, Evans y Bryson, 1996):

| Principio | Qué mide |
|---|---|
| **Dispersión** | Cuánto se alejan las opiniones del promedio y entre sí. Una población despolarizada concentra sus respuestas en un tramo angosto de la escala; una polarizada las reparte a lo ancho. Es la noción más intuitiva y la más pobre: no distingue una distribución uniforme —donde hay de todo— de una con dos campos enfrentados. |
| **Bimodalidad** | Si la distribución tiene dos picos y se vacía en el centro. Es lo que la discusión pública suele imaginar: no que haya diversidad, sino que las posiciones intermedias desaparezcan y queden dos bloques. Una distribución puede tener dispersión alta sin ser bimodal, y bimodalidad sin dispersión extrema. |
| **Restricción** (*constraint*) | Si las actitudes sobre temas distintos se responden de forma coherente entre sí. Que alguien esté a favor del aborto no dice nada, en principio, sobre su posición respecto de la redistribución; cuando sí lo dice, hay restricción. Significa que un solo eje organiza opiniones sobre asuntos independientes, y por lo tanto que el desacuerdo se acumula en vez de cruzarse. |
| **Consolidación** (alineamiento social) | Si las posiciones se alinean con la ideología declarada o con clivajes sociales —clase, educación, religión, edad—. Cuando la actitud es predecible a partir de la posición social de quien responde, el desacuerdo deja de ser entre individuos y pasa a ser entre grupos identificables. Define si existen bandos con base social, no solo opiniones distribuidas. |

En el taller aplicamos este esquema a Argentina con LAPOP. Acá lo extendemos a una comparación internacional.

Quisiéramos abordar la siguente pregunta: ¿Está América Latina más polarizada que el resto del mundo?


El archivo integrado de la Ola 7 (2017–2022) y el cuestionario maestro están descargados y disponibles en [`data/`](data), en este mismo repositorio. Los links de abajo bajan el archivo directamente:
- Datos WVS Ola 7, el mismo archivo integrado en dos formatos: [descargar CSV](https://github.com/gefero/factor_data_tuto_NLP_SICSS/raw/main/consignas_desafio/encuestas/data/F00011356-WVS_Cross-National_Wave_7_csv_v6_0.zip) (21 MB comprimido, 190 MB al descomprimir) · [descargar RDS](https://github.com/gefero/factor_data_tuto_NLP_SICSS/raw/main/consignas_desafio/encuestas/data/F00011421-WVS_Cross-National_Wave_7_rds_v6_0.zip) (19 MB, para leer desde R con `readRDS()`)
- [Descargar cuestionario maestro](https://github.com/gefero/factor_data_tuto_NLP_SICSS/raw/main/consignas_desafio/encuestas/data/F00010738-WVS-7_Master_Questionnaire_2017-2020_English%20%281%29.pdf) (PDF, versión en inglés)
- Libro de códigos: no está descargado. Se baja del [sitio de WVS](https://www.worldvaluessurvey.org/WVSDocumentationWV7.jsp), junto a los archivos anteriores.

Todo lo demás lo decide el grupo.

## Qué tienen que construir
Simple: una medida de polarización de actitudes comparable entre países a partir del World Values Survey, y usarla para responder la pregunta.

Algunas cuestiones a tener en cuenta:

1. **Qué se mide.** Qué dominio de actitudes, con qué ítems, y por qué esos ítems forman un dominio y no una lista arbitraria. Qué se descartó y con qué criterio.
2. **Qué países entran** en la comparación, y qué se gana y se pierde con ese recorte.
3. **Cómo se preparan los datos.** No respuestas, escalas de distinta amplitud, ítems que corren en sentido contrario, ponderadores.
4. **Cómo se operacionaliza cada uno de los cuatro principios.** Qué estadístico, calculado sobre qué, con qué supuestos. Hay más de una opción defendible para cada uno; la elección es el trabajo.
5. **Si los cuatro se combinan en un índice único o no.** Y sobre qué evidencia se toma esa decisión.
6. **Qué sostiene la medida construida y qué no.** Al menos tres límites, identificados por el grupo.

## Entregables
- Una presentación oral de unos 10 minutos, con slides, que reseñe decisiones metodológicas y principales resultados
- La notebook con el análisis acompaña como respaldo, pero lo que se discute es la presentación.

La idea es, en estas 6 horas, poder llegar a una primera iteración completa del proceso.
Por eso les conviene tener en cuenta lo siguiente:

- Muchas de estas preguntas, son teóricamente abiertas.
- Cerrar la selección de ítems dentro de la primera hora aunque no convenza del todo, y documentar la duda en el informe. Un dominio imperfecto analizado hasta el final vale más que uno perfecto sin resultados.
- Si a mitad de jornada faltan componentes, recortar la cantidad de países antes que la cantidad de principios medidos.
- Producir los gráficos directamente en calidad de proyección. Rehacer figuras al final es lo que hace pasarse de hora.
