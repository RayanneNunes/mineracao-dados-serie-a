import time

import pandas as pd

from config import (
    TEMPORADAS,
    BASE_URL,
    HEADERS,
    INTERVALO
)

from scraper import obter_html
from parser import extrair_jogadores
from database import salvar_csv
from database import salvar_sqlite


def main():

    print("\n" + "=" * 80)


    registros = []

    for temporada in TEMPORADAS:

        print(f"Coletando temporada {temporada}")

        url = BASE_URL.format(
            temporada=temporada
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

        print(
            f"{len(jogadores)} registros encontrados"
        )

        time.sleep(INTERVALO)

    if not registros:

        print("Nenhum registro coletado.")
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

    print("\nColeta finalizada com sucesso.")


if __name__ == "__main__":
    main()