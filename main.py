from pathlib import Path

import pandas as pd

from src.coletar_ofensivo import main as coletar_ofensivo

from src.coletar_disciplinar import (
    main as coletar_disciplinar,
)

from scripts.montar_dataset import (
    main as montar_dataset,
)

from src.database import (
    salvar_dataset_final,
)

from scripts.responder_perguntas import (
    main as responder_perguntas,
)


BASE_DIR = Path(__file__).resolve().parent

DATASET_FINAL_PATH = (
    BASE_DIR
    / "data"
    / "dataset_final.csv"
)


def main():

    print("=" * 80)
    print("MINERAÇÃO DE DADOS - SÉRIE A")
    print("=" * 80)

    # ======================
    # Coleta ofensiva
    # ======================

    print("\n[1/5] Coleta ofensiva")

    coletar_ofensivo()

    # ======================
    # Coleta disciplinar
    # ======================

    print("\n[2/5] Coleta disciplinar")

    coletar_disciplinar()

    # ======================
    # Montagem do dataset
    # ======================

    print("\n[3/5] Montagem do dataset")

    montar_dataset()

    # ======================
    # Atualização do banco
    # ======================

    print("\n[4/5] Atualização do banco")

    df = pd.read_csv(
        DATASET_FINAL_PATH
    )

    salvar_dataset_final(
        df
    )

    # ======================
    # Responder perguntas
    # ======================

    print("\n[5/5] Respondendo perguntas")

    responder_perguntas()

    print("\nProcesso concluído com sucesso.")


if __name__ == "__main__":
    main()