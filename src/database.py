import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

DB_PATH = DATA_DIR / "serie_a.db"

CSV_PATH = DATA_DIR / "serie_a_estatisticas.csv"


def salvar_sqlite(df):

    DATA_DIR.mkdir(exist_ok=True)

    with sqlite3.connect(DB_PATH) as conexao:

        df.to_sql(
            "jogadores",
            conexao,
            if_exists="replace",
            index=False
        )

    print(f"Banco atualizado: {DB_PATH}")


def salvar_csv(df):

    DATA_DIR.mkdir(exist_ok=True)

    df.to_csv(
        CSV_PATH,
        index=False,
        encoding="utf-8-sig"
    )

    print(f"CSV atualizado: {CSV_PATH}")