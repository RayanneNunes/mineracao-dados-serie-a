import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

DB_PATH = DATA_DIR / "serie_a.db"


def salvar_dataset_final(df):

    DATA_DIR.mkdir(exist_ok=True)

    with sqlite3.connect(DB_PATH) as conexao:

        df.to_sql(
            "dataset_final",
            conexao,
            if_exists="replace",
            index=False
        )

    print(
        f"Banco atualizado: {DB_PATH}"
    )