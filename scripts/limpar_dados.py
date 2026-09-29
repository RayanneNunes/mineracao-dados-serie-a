from pathlib import Path

import pandas as pd


# =====================================
# Caminhos
# =====================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

DATASET_PATH = DATA_DIR / "dataset_final.csv"

DATASET_LIMPO_PATH = DATA_DIR / "dataset_final_limpo.csv"


# =====================================
# Main
# =====================================

def main():

    print("=" * 80)
    print("LIMPEZA E ANÁLISE DESCRITIVA")
    print("=" * 80)

    # =====================================
    # Carregar base
    # =====================================

    df = pd.read_csv(
        DATASET_PATH
    )

    registros_antes = len(df)

    print(
        f"\nRegistros carregados: "
        f"{registros_antes}"
    )

    # =====================================
    # Conversão de tipos
    # =====================================

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
                errors="coerce"
            )

    # =====================================
    # Preencher NaN disciplinares com 0
    # =====================================

    colunas_disciplinares = [
        "suspensoes_amarelo",
        "cartoes_amarelos",
        "segundo_amarelo",
        "cartoes_vermelhos",
        "expulsoes",
        "pontos_disciplinares",
        "cartoes_por_partida",
    ]

    for coluna in colunas_disciplinares:

        if coluna in df.columns:

            df[coluna] = (
                df[coluna]
                .fillna(0)
            )

    # =====================================
    # Valores nulos
    # =====================================

    print("\n" + "=" * 80)
    print("VALORES NULOS")
    print("=" * 80)

    print(
        df.isnull()
        .sum()
        .sort_values(
            ascending=False
        )
    )

    # =====================================
    # Duplicados
    # =====================================

    duplicados = (
        df.duplicated()
        .sum()
    )

    print("\n" + "=" * 80)
    print("DUPLICADOS")
    print("=" * 80)

    print(
        f"Duplicados encontrados: "
        f"{duplicados}"
    )

    # =====================================
    # Remoção de duplicados
    # =====================================

    df = (
        df
        .drop_duplicates()
        .reset_index(drop=True)
    )

    registros_depois = len(df)

    # =====================================
    # Salvar base limpa
    # =====================================

    df.to_csv(
        DATASET_LIMPO_PATH,
        index=False,
        encoding="utf-8-sig"
    )

    print(
        f"\nBase limpa salva em:\n"
        f"{DATASET_LIMPO_PATH}"
    )

    # =====================================
    # Comparativo
    # =====================================

    print("\n" + "=" * 80)
    print("ANTES E DEPOIS DA LIMPEZA")
    print("=" * 80)

    print(
        f"Registros antes: "
        f"{registros_antes}"
    )

    print(
        f"Registros depois: "
        f"{registros_depois}"
    )

    print(
        f"Registros removidos: "
        f"{registros_antes - registros_depois}"
    )

    # =====================================
    # Tipos das variáveis
    # =====================================

    print("\n" + "=" * 80)
    print("TIPOS DAS VARIÁVEIS")
    print("=" * 80)

    print(df.dtypes)

    # =====================================
    # Valores únicos
    # =====================================

    print("\n" + "=" * 80)
    print("VALORES ÚNICOS")
    print("=" * 80)

    print(df.nunique())

    # =====================================
    # Estatísticas descritivas
    # =====================================

    print("\n" + "=" * 80)
    print("ESTATÍSTICAS DESCRITIVAS")
    print("=" * 80)

    print(
        df[colunas_numericas]
        .describe()
        .round(2)
    )

    # =====================================
    # Medianas
    # =====================================

    print("\n" + "=" * 80)
    print("MEDIANAS")
    print("=" * 80)

    print(
        df[colunas_numericas]
        .median()
        .round(2)
    )

    # =====================================
    # Nacionalidades
    # =====================================

    print("\n" + "=" * 80)
    print("TOP 10 NACIONALIDADES")
    print("=" * 80)

    print(
        df["nacionalidade"]
        .value_counts()
        .head(10)
    )

    # =====================================
    # Posições
    # =====================================

    print("\n" + "=" * 80)
    print("DISTRIBUIÇÃO DE POSIÇÕES")
    print("=" * 80)

    print(
        df["posicao"]
        .value_counts()
    )

    # =====================================
    # Clubes
    # =====================================

    print("\n" + "=" * 80)
    print("TOP 10 CLUBES")
    print("=" * 80)

    print(
        df["clube"]
        .value_counts()
        .head(10)
    )

    # =====================================
    # Valores máximos
    # =====================================

    print("\n" + "=" * 80)
    print("VALORES MÁXIMOS")
    print("=" * 80)

    print(
        f"Maior número de gols: "
        f"{df['gols'].max()}"
    )

    print(
        f"Maior número de assistências: "
        f"{df['assistencias'].max()}"
    )

    print(
        f"Maior número de cartões amarelos: "
        f"{df['cartoes_amarelos'].max()}"
    )

    print(
        f"Maior número de cartões vermelhos: "
        f"{df['cartoes_vermelhos'].max()}"
    )

    print(
        f"Maior média de cartões por partida: "
        f"{df['cartoes_por_partida'].max()}"
    )

    # =====================================
    # Amostra da base
    # =====================================

    print("\n" + "=" * 80)
    print("AMOSTRA DA BASE")
    print("=" * 80)

    print(
        df.head(10)
    )

    print("\nLimpeza e análise concluídas.")


if __name__ == "__main__":
    main()