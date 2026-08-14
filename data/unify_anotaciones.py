"""Unifica los JSON parciales de anotación contenidos en
sicss-anotacion-20260814T182433Z-1-001.zip en un único archivo JSON.

Cada JSON parcial corresponde a las anotaciones de un anotador sobre el
mismo conjunto de tweets, por lo que el resultado es la concatenación de
todos los registros (no se eliminan filas por tratarse de anotaciones
distintas, aunque compartan tweet_id).
"""

import json
import zipfile
from pathlib import Path

DATA_DIR = Path(__file__).parent
ZIP_PATH = DATA_DIR / "sicss-anotacion-20260814T182433Z-1-001.zip"
OUTPUT_PATH = DATA_DIR / "sicss-anotacion-unificado.json"


def main() -> None:
    registros = []
    with zipfile.ZipFile(ZIP_PATH) as zf:
        json_names = sorted(n for n in zf.namelist() if n.endswith(".json"))
        for name in json_names:
            with zf.open(name) as f:
                registros.extend(json.load(f))

    OUTPUT_PATH.write_text(
        json.dumps(registros, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"Unificados {len(json_names)} archivos -> {len(registros)} registros")
    print(f"Guardado en: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
