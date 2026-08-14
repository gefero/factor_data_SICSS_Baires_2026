"""Unifica los JSON parciales de anotación contenidos en
sicss-anotacion-20260814T182433Z-1-001.zip en un único archivo JSON.

Cada JSON parcial corresponde a las anotaciones de un anotador sobre el
mismo conjunto de tweets, por lo que el resultado es la concatenación de
todos los registros (no se eliminan filas por tratarse de anotaciones
distintas, aunque compartan tweet_id).

Caveat sobre `annotator`: tres de los diez archivos parciales tienen el
mismo valor "anonymous" en ese campo, pero corresponden a tres personas
distintas (son tres archivos separados dentro del zip). Si se concatenara
sin más, esas tres identidades quedarían mezcladas bajo un mismo nombre,
lo que arruina cualquier análisis por codificador (agreement, sesgos,
etc.). Por eso se agrega un campo `coder_id`, derivado del archivo de
origen, que sí identifica a cada uno de los 10 codificadores de forma
unívoca: si el `annotator` es único se reutiliza tal cual, y si se repite
se sufija con un índice (anonymous_1, anonymous_2, anonymous_3).
"""

import json
import zipfile
from collections import Counter
from pathlib import Path

DATA_DIR = Path(__file__).parent
ZIP_PATH = DATA_DIR / "sicss-anotacion-20260814T182433Z-1-001.zip"
OUTPUT_PATH = DATA_DIR / "sicss-anotacion-unificado.json"


def main() -> None:
    with zipfile.ZipFile(ZIP_PATH) as zf:
        json_names = sorted(n for n in zf.namelist() if n.endswith(".json"))
        archivos = [(name, json.load(zf.open(name))) for name in json_names]

    # Cuenta cuántos archivos comparten el mismo `annotator` para poder
    # desambiguar (ver caveat en el docstring del módulo).
    total_por_annotator = Counter(recs[0]["annotator"] for _, recs in archivos)
    contador_visto = Counter()

    registros = []
    for name, recs in archivos:
        annotator = recs[0]["annotator"]
        if total_por_annotator[annotator] > 1:
            contador_visto[annotator] += 1
            coder_id = f"{annotator}_{contador_visto[annotator]}"
        else:
            coder_id = annotator
        for r in recs:
            r["coder_id"] = coder_id
        registros.extend(recs)

    OUTPUT_PATH.write_text(
        json.dumps(registros, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    n_coders = len({r["coder_id"] for r in registros})
    print(f"Unificados {len(json_names)} archivos -> {len(registros)} registros")
    print(f"Codificadores (coder_id) identificados: {n_coders}")
    print(f"Guardado en: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
