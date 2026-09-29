import time

import pandas as pd

from config import (
    TEMPORADAS,
    BASE_URL,
    HEADERS,
    INTERVALO
)

from scraper import (
    obter_html,
    descobrir_paginas
)

from parser import extrair_jogadores

from database import (
    salvar_csv,
    salvar_sqlite
)


def main():

    registros = []

    print("\n" + "=" * 80)

    for temporada in TEMPORADAS:

        print(f"Coletando temporada {temporada}")

        url_base = BASE_URL.format(
            temporada=temporada
        )

        total_paginas = descobrir_paginas(
            url_base,
            HEADERS
        )

        print(
            f"Total de páginas: "
            f"{total_paginas}"
        )

        total_registros_temporada = 0

        for pagina in range(
            1,
            total_paginas + 1
        ):

            if pagina == 1:

                url = url_base

            else:

                url = (
                    f"{url_base}"
                    f"/page/{pagina}"
                )

            html = obter_html(
                url,
                HEADERS
            )

            jogadores = extrair_jogadores(
                html,
                temporada,
                url
            )

            registros.extend(jogadores)

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
            "Nenhum registro coletado."
        )

        return

    df = pd.DataFrame(registros)

    print("\nResumo:")

    print(df.info())

    print("\nPrimeiras linhas:")

    print(df.head())

    print("\nSalvando CSV...")

    salvar_csv(df)

    print("\nSalvando SQLite...")

    salvar_sqlite(df)

    print(
        "\nColeta finalizada com sucesso."
    )


if __name__ == "__main__":
    main()