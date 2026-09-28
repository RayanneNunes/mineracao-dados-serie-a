import sqlite3

def salvar_sqlite(df, arquivo):
    conexao = sqlite3.connect(arquivo)

    df.to_sql(
        "jogadores",
        conexao,
        if_exists="replace",
        index=False
    )

    conexao.close()

def salvar_csv(df, arquivo):
    df.to_csv(
        arquivo,
        index=False,
        encoding="utf-8-sig"
    )