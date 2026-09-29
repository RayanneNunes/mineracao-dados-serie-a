# Mineração de Dados - Campeonato Brasileiro Série A

Projeto desenvolvido para a disciplina de Mineração de Dados.

## Objetivo

Construir uma base de dados sobre jogadores do Campeonato Brasileiro Série A por meio de Web Scraping utilizando o Transfermarkt como fonte de dados.

Os dados coletados serão utilizados nas etapas de ETL, preparação dos dados e análise exploratória, seguindo o processo de KDD (Knowledge Discovery in Databases).

---

## Perguntas de Pesquisa

**Q1)** Quais posições apresentam maior contribuição ofensiva, medida por gols e assistências, ao longo das temporadas?

**Q2)** Como o perfil disciplinar, medido em cartões por partida, varia entre as posições?

**Q3)** Jogadores estrangeiros disputam mais partidas e apresentam maior produção ofensiva do que os brasileiros?

**Q4)** A presença de jogadores estrangeiros mudou ao longo das temporadas?

---

## Fonte dos Dados

- Site: Transfermarkt
- Competição: Campeonato Brasileiro Série A
- Temporadas analisadas:
  - 2023
  - 2024
  - 2025

---

## Estrutura do Projeto

```text
mineracao-dados-serie-a/
│
├── data/
│   ├── ofensivo.csv
│   ├── disciplinar.csv
│   ├── dataset_final.csv
│   ├── dataset_final_limpo.csv
│   └── serie_a.db
│
├── doc/
│   └── diagrama_pipeline.png
│
├── scripts/
│   ├── montar_dataset.py
│   ├── limpar_dados.py
│   └── responder_perguntas.py
│
├── src/
│   ├── coletar_disciplinar.py
│   ├── coletar_ofensivo.py
│   ├── config.py
│   ├── database.py
│   ├── parser_disciplinar.py
│   ├── parser_ofensivo.py
│   └── scraper.py
│
├── main.py
│
├── requirements.txt
│
└── README.md
```

---

## Tecnologias Utilizadas

- Python 3.13+
- Requests
- BeautifulSoup4
- Pandas
- SQLite

---

## Instalação

### 1. Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
```

### 2. Entrar na pasta do projeto

```bash
cd mineracao-dados-serie-a
```

### 3. Criar o ambiente virtual

```bash
python -m venv venv
```

### 4. Ativar o ambiente virtual

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / MacOS

```bash
source venv/bin/activate
```

### 5. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## Execução

Para executar todo o pipeline do projeto:

```bash
python main.py
```

O processo executará automaticamente:

1. Coleta dos dados ofensivos
2. Coleta dos dados disciplinares
3. Integração das bases
4. Limpeza dos dados
5. Atualização do banco SQLite
6. Resposta das perguntas de pesquisa

---

## Pipeline do Projeto

```text
                  TRANSFERMARKT
                         │
        ┌────────────────┴────────────────┐
        │                                 │
        ▼                                 ▼
  Coleta Ofensiva                 Coleta Disciplinar
(coletar_ofensivo.py)         (coletar_disciplinar.py)
        │                                 │
        ▼                                 ▼
    ofensivo.csv                  disciplinar.csv
        │                                 │
        └────────────────┬────────────────┘
                         │
                         ▼
               montar_dataset.py
                         │
                         ▼
                 dataset_final.csv
                         │
                         ▼
                  limpar_dados.py
                         │
                         ▼
             dataset_final_limpo.csv
                         │
                         ▼
                    database.py
                         │
                         ▼
                     serie_a.db
                         │
                         ▼
              responder_perguntas.py
                         │
                         ▼
                  Q1 • Q2 • Q3 • Q4
```

---

## Bases Geradas

### Base Ofensiva (`ofensivo.csv`)

Contém:

- Jogador
- Posição
- Clube
- Nacionalidade
- Partidas
- Gols
- Assistências
- Participação em gols
- Temporada
- URL de origem

---

### Base Disciplinar (`disciplinar.csv`)

Contém:

- Jogador
- Posição
- Clube
- Nacionalidade
- Partidas
- Suspensões por amarelo
- Cartões amarelos
- Segundo amarelo
- Cartões vermelhos
- Expulsões
- Pontos disciplinares
- Cartões por partida
- Temporada
- URL de origem

---

### Base Integrada (`dataset_final.csv`)

Resultado da integração das bases ofensiva e disciplinar.

---

### Base Final Limpa (`dataset_final_limpo.csv`)

Resultado do processo de limpeza e preparação dos dados.

Contém os atributos:

```text
jogador
posicao
clube
nacionalidade
temporada

partidas

gols
assistencias
participacao_gols

suspensoes_amarelo
cartoes_amarelos
segundo_amarelo
cartoes_vermelhos
expulsoes
pontos_disciplinares
cartoes_por_partida
```

---

## Banco de Dados

O projeto também gera:

```text
data/serie_a.db
```

Tabela:

```text
dataset_final_limpo
```

---

## Limpeza dos Dados

As seguintes etapas são aplicadas:

- Conversão de atributos numéricos
- Tratamento de valores ausentes disciplinares
- Remoção de registros duplicados
- Identificação de valores nulos
- Estatísticas descritivas
- Identificação de valores extremos

Jogadores que atuaram por mais de um clube na mesma temporada recebem a categoria:

```text
MULTIPLOS_CLUBES
```

preservando os registros sem perda de informação.

---

## Resultados da Preparação

Base final:

- 1032 registros
- 16 atributos
- 595 jogadores únicos
- 27 clubes
- 27 nacionalidades
- 3 temporadas (2023–2025)

---

## Próximas Etapas

- Análise das perguntas de pesquisa
- Aplicação de técnicas de mineração de dados
- Construção do dashboard final da disciplina

---

## Autores

### Rayanne Nunes

GitHub:

```text
[https://github.com/RayanneNunes](https://github.com/RayanneNunes)
```

### João Paulo Mussarelli Carossine

GitHub:

```text
[https://github.com/joaopcarossine](https://github.com/joaopcarossine)
```