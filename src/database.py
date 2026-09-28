import sqlite3
from pathlib import Path

DB_PATH = "data/serie_a.db"
CSV_PATH = "data/serie_a_estatisticas.csv"

def salvar_sqlite(df):
    Path("data").mkdir(exist_ok=True)

    with sqlite3.connect(DB_PATH) as conexao:
        df.to_sql(
            "jogadores",
            conexao,
            if_exists="replace",
            index=False
        )

def salvar_csv(df):
    Path("data").mkdir(exist_ok=True)

    df.to_csv(
        CSV_PATH,
        index=False,
        encoding="utf-8-sig"
    )