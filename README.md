# Mineração de Dados - Campeonato Brasileiro Série A

Projeto desenvolvido para a disciplina de Mineração de Dados.

## Objetivo

Construir uma base de dados sobre jogadores do Campeonato Brasileiro Série A por meio de Web Scraping utilizando o Transfermarkt como fonte de dados.

Os dados coletados serão utilizados nas etapas de ETL, pré-processamento e mineração de dados da disciplina.

## Estrutura do Projeto

```text
mineracao_dados/
│
├── data/
│   ├── serie_a.db
│   └── serie_a.csv
│
├── src/
│   ├── config.py
│   ├── scraper.py
│   ├── parser.py
│   ├── database.py
│   └── main.py
│
└── requirements.txt
```

## Tecnologias Utilizadas

- Python 3.12+
- Requests
- BeautifulSoup4
- Pandas
- SQLite

## Instalação

Clone o repositório:

```bash
git clone <url-do-repositorio>
```

Entre na pasta do projeto:

```bash
cd mineracao_dados
```

Crie e ative uma máquina virtual:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Execução

Execute o script principal:

```bash
python src/main.py
```

## Dados Coletados

A base contempla informações como:

- Jogador
- Posição
- Clube
- Nacionalidade
- Idade
- Jogos
- Gols
- Assistências
- Participações em gols
- Temporada
- URL de origem
- Data da coleta

## Saídas

Ao final da execução são gerados:

- `data/serie_a.csv`
- `data/serie_a.db`

## Observações

- A coleta é realizada com intervalo entre requisições para reduzir o impacto sobre o servidor.
- Os dados são utilizados exclusivamente para fins acadêmicos.
- O projeto segue as etapas do processo KDD estudadas na disciplina.

## Autores

- Rayanne Nunes
- João Paulo Mussarelli Carossine