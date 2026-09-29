from pathlib import Path

import pandas as pd


# =====================================
# Caminhos
# =====================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

DATASET_PATH = DATA_DIR / "dataset_final.csv"


# =====================================
# Utilidades
# =====================================

def classificar_nacionalidade(valor):

    if str(valor).strip().lower() == "brazil":
        return "Brasileiro"

    return "Estrangeiro"


# =====================================
# Q1
# =====================================

def responder_q1(df):

    print("\n" + "=" * 80)
    print("Q1")
    print("=" * 80)

    print(
        "\nQuais posições apresentam maior contribuição ofensiva,"
        "\nmedida por gols e assistências, ao longo das temporadas?"
    )

    resultado = (
        df.groupby("posicao")
        [
            [
                "gols",
                "assistencias",
                "participacao_gols",
            ]
        ]
        .mean()
        .sort_values(
            "participacao_gols",
            ascending=False,
        )
        .round(2)
    )

    print(resultado)


# =====================================
# Q2
# =====================================

def responder_q2(df):

    print("\n" + "=" * 80)
    print("Q2")
    print("=" * 80)

    print(
        "\nComo o perfil disciplinar,"
        "\nmedido em cartões por partida,"
        "\nvaria entre as posições?"
    )

    resultado = (
        df.groupby("posicao")
        [
            [
                "cartoes_amarelos",
                "cartoes_vermelhos",
                "pontos_disciplinares",
                "cartoes_por_partida",
            ]
        ]
        .mean()
        .sort_values(
            "cartoes_por_partida",
            ascending=False,
        )
        .round(2)
    )

    print(resultado)


# =====================================
# Q3
# =====================================

def responder_q3(df):

    print("\n" + "=" * 80)
    print("Q3")
    print("=" * 80)

    print(
        "\nJogadores estrangeiros disputam mais partidas"
        "\ne apresentam maior produção ofensiva"
        "\ndo que os brasileiros?"
    )

    df["grupo_nacionalidade"] = (
        df["nacionalidade"]
        .apply(classificar_nacionalidade)
    )

    resultado = (
        df.groupby("grupo_nacionalidade")
        [
            [
                "partidas",
                "gols",
                "assistencias",
                "participacao_gols",
            ]
        ]
        .mean()
        .round(2)
    )

    print(resultado)


# =====================================
# Q4
# =====================================

def responder_q4(df):

    print("\n" + "=" * 80)
    print("Q4")
    print("=" * 80)

    print(
        "\nA presença de jogadores estrangeiros"
        "\nmudou ao longo das temporadas?"
    )

    df["grupo_nacionalidade"] = (
        df["nacionalidade"]
        .apply(classificar_nacionalidade)
    )

    total = (
        df.groupby("temporada")["jogador"]
        .nunique()
    )

    estrangeiros = (
        df[
            df["grupo_nacionalidade"]
            == "Estrangeiro"
        ]
        .groupby("temporada")["jogador"]
        .nunique()
    )

    resultado = pd.DataFrame(
        {
            "total_jogadores": total,
            "estrangeiros": estrangeiros,
        }
    ).fillna(0)

    resultado["percentual_estrangeiros"] = (
        resultado["estrangeiros"]
        / resultado["total_jogadores"]
        * 100
    ).round(2)

    print(resultado)


# =====================================
# Main
# =====================================

def main():

    print("=" * 80)
    print("ANÁLISE DAS PERGUNTAS")
    print("=" * 80)

    df = pd.read_csv(
        DATASET_PATH
    )

    colunas_numericas = [
        "partidas",
        "gols",
        "assistencias",
        "participacao_gols",
        "suspensoes_amarelo",
        "cartoes_amarelos",
        "segundo_amarelo",
        "cartoes_vermelhos",
        "expulsoes",
        "pontos_disciplinares",
        "cartoes_por_partida",
    ]

    for coluna in colunas_numericas:

        if coluna in df.columns:

            df[coluna] = pd.to_numeric(
                df[coluna],
                errors="coerce",
            )

    responder_q1(df)

    responder_q2(df)

    responder_q3(df)

    responder_q4(df)

    print("\nAnálise concluída.")


if __name__ == "__main__":
    main()