from pathlib import Path

import pandas as pd


# =====================================
# Caminhos
# =====================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

OFENSIVO_PATH = DATA_DIR / "ofensivo.csv"

DISCIPLINAR_PATH = DATA_DIR / "disciplinar.csv"

DATASET_FINAL_PATH = DATA_DIR / "dataset_final.csv"


# =====================================
# Temporadas utilizadas
# =====================================

TEMPORADAS = [2023, 2024, 2025]


def main():

    print("=" * 80)
    print("MONTAGEM DO DATASET FINAL")
    print("=" * 80)

    print("\nCarregando bases...")

    ofensivo = pd.read_csv(
        OFENSIVO_PATH
    )

    disciplinar = pd.read_csv(
        DISCIPLINAR_PATH
    )

    # =====================================
    # Filtrar temporadas
    # =====================================

    ofensivo = ofensivo[
        ofensivo["temporada"].isin(
            TEMPORADAS
        )
    ]

    disciplinar = disciplinar[
        disciplinar["temporada"].isin(
            TEMPORADAS
        )
    ]

    # =====================================
    # Normalizar chaves
    # =====================================

    for coluna in ["jogador", "clube"]:

        ofensivo[coluna] = (
            ofensivo[coluna]
            .astype(str)
            .str.strip()
        )

        disciplinar[coluna] = (
            disciplinar[coluna]
            .astype(str)
            .str.strip()
        )

    # =====================================
    # Colunas ofensivas
    # =====================================

    ofensivo = ofensivo[
        [
            "jogador",
            "posicao",
            "clube",
            "nacionalidade",
            "temporada",
            "partidas",
            "gols",
            "assistencias",
            "participacao_gols",
        ]
    ]

    # =====================================
    # Colunas disciplinares
    # =====================================

    disciplinar = disciplinar[
        [
            "jogador",
            "clube",
            "temporada",
            "suspensoes_amarelo",
            "cartoes_amarelos",
            "segundo_amarelo",
            "cartoes_vermelhos",
            "expulsoes",
            "pontos_disciplinares",
            "cartoes_por_partida",
        ]
    ]

    print(
        f"\nRegistros ofensivos: {len(ofensivo)}"
    )

    print(
        f"Registros disciplinares: {len(disciplinar)}"
    )

    # =====================================
    # Merge
    # =====================================

    print("\nRealizando merge...")

    dataset_final = pd.merge(
        ofensivo,
        disciplinar,
        on=[
            "jogador",
            "clube",
            "temporada",
        ],
        how="inner",
    )

    # =====================================
    # Remover duplicados
    # =====================================

    dataset_final = (
        dataset_final
        .drop_duplicates()
        .reset_index(drop=True)
    )

    # =====================================
    # Ordenação
    # =====================================

    dataset_final = (
        dataset_final
        .sort_values(
            [
                "temporada",
                "clube",
                "jogador",
            ]
        )
        .reset_index(drop=True)
    )

    # =====================================
    # Salvar CSV
    # =====================================

    DATA_DIR.mkdir(
        exist_ok=True
    )

    dataset_final.to_csv(
        DATASET_FINAL_PATH,
        index=False,
        encoding="utf-8-sig",
    )

    # =====================================
    # Resumo
    # =====================================

    print("\nResumo")

    print(
        f"Registros finais: "
        f"{len(dataset_final)}"
    )

    print(
        f"Colunas finais: "
        f"{len(dataset_final.columns)}"
    )

    print(
        f"Arquivo salvo: "
        f"{DATASET_FINAL_PATH}"
    )

    print(
        "\nDataset final criado com sucesso."
    )


if __name__ == "__main__":
    main()