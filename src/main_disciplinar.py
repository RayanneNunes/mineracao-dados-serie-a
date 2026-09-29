import time

import pandas as pd

from config import (
    TEMPORADAS,
    DISCIPLINARY_URL,
    HEADERS,
    INTERVALO
)

from scraper import (
    obter_html,
    descobrir_paginas
)

from parser_disciplinar import (
    extrair_cartoes
)


def main():

    registros = []

    print("\n" + "=" * 80)

    for temporada in TEMPORADAS:

        print(
            f"Coletando temporada {temporada}"
        )

        url_base = DISCIPLINARY_URL.format(
            temporada=temporada
        )

        total_paginas = descobrir_paginas(
            url_base,
            HEADERS
        )

        print(
            f"Total de páginas: {total_paginas}"
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
                    f"{url_base}/page/{pagina}"
                )

            html = obter_html(
                url,
                HEADERS
            )

            registros_pagina = extrair_cartoes(
                html,
                temporada,
                url
            )

            registros.extend(
                registros_pagina
            )

            total_registros_temporada += len(
                registros_pagina
            )

            print(
                f"Página {pagina}: "
                f"{len(registros_pagina)} registros"
            )

            time.sleep(
                INTERVALO
            )

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

    df = pd.DataFrame(
        registros
    )

    print("\nResumo:")

    print(df.info())

    print("\nPrimeiras linhas:")

    print(df.head())

    arquivo = (
        "../data/cartoes_debug.csv"
    )

    df.to_csv(
        arquivo,
        index=False,
        encoding="utf-8-sig"
    )

    print(
        f"\nArquivo salvo: {arquivo}"
    )

    print(
        "\nColeta disciplinar finalizada."
    )


if __name__ == "__main__":
    main()