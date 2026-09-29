import time
from pathlib import Path

import pandas as pd

from src.config import (
    TEMPORADAS,
    BASE_URL,
    HEADERS,
    INTERVALO,
)

from src.scraper import (
    obter_html,
    descobrir_paginas,
)

from src.parser_ofensivo import (
    extrair_jogadores,
)


BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

CSV_PATH = DATA_DIR / "ofensivo.csv"


def main():

    registros = []

    print("\n" + "=" * 80)
    print("COLETA OFENSIVA")
    print("=" * 80)

    for temporada in TEMPORADAS:

        print(
            f"\nColetando temporada {temporada}"
        )

        url_base = BASE_URL.format(
            temporada=temporada
        )

        total_paginas = descobrir_paginas(
            url_base,
            HEADERS,
        )

        print(
            f"Total de páginas: {total_paginas}"
        )

        total_registros_temporada = 0

        for pagina in range(
            1,
            total_paginas + 1,
        ):

            if pagina == 1:

                url = url_base

            else:

                url = (
                    f"{url_base}/page/{pagina}"
                )

            html = obter_html(
                url,
                HEADERS,
            )

            jogadores = extrair_jogadores(
                html,
                temporada,
                url,
            )

            registros.extend(
                jogadores
            )

            total_registros_temporada += len(
                jogadores
            )

            print(
                f"Página {pagina}: "
                f"{len(jogadores)} registros"
            )

            time.sleep(INTERVALO)

        print(
            f"Temporada {temporada}: "
            f"{total_registros_temporada} registros"
        )

        print("-" * 50)

    if not registros:

        print(
            "\nNenhum registro coletado."
        )

        return

    df = pd.DataFrame(
        registros
    )

    print("\nResumo:")

    df.info()

    print("\nPrimeiras linhas:")

    print(
        df.head()
    )

    DATA_DIR.mkdir(
        exist_ok=True
    )

    print("\nSalvando CSV...")

    df.to_csv(
        CSV_PATH,
        index=False,
        encoding="utf-8-sig",
    )

    print(
        f"\nArquivo salvo em: {CSV_PATH}"
    )

    print(
        "\nColeta ofensiva finalizada com sucesso."
    )


if __name__ == "__main__":
    main()