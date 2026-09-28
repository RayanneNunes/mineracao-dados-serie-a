import pandas as pd

from config import *
from scraper import obter_html
from parser import extrair_jogadores
from database import salvar_csv
from database import salvar_sqlite

def main():

    registros = []

    for temporada in TEMPORADAS:

        html = obter_html(...)

        registros.extend(
            extrair_jogadores(
                html,
                temporada
            )
        )

    df = pd.DataFrame(registros)

    salvar_csv(
        df,
        "data/serie_a_estatisticas.csv"
    )

    salvar_sqlite(
        df,
        "data/serie_a.db"
    )

if __name__ == "__main__":
    main()