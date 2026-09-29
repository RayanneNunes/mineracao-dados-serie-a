from bs4 import BeautifulSoup


def extrair_cartoes(
    html,
    temporada,
    url,
):
    soup = BeautifulSoup(
        html,
        "html.parser",
    )

    tabela = soup.find(
        "table",
        class_="items",
    )

    if tabela is None:
        return []

    registros = []

    linhas = tabela.find_all("tr")

    for linha in linhas:

        colunas = linha.find_all("td")

        if len(colunas) < 15:
            continue

        try:

            dados = [
                td.get_text(
                    " ",
                    strip=True,
                )
                for td in colunas
            ]

            # Clube

            clube = ""

            clube_img = colunas[5].find("img")

            if clube_img:
                clube = (
                    clube_img.get("title")
                    or clube_img.get("alt")
                    or ""
                )

            # Nacionalidade

            nacionalidade = ""

            nacao_img = colunas[6].find("img")

            if nacao_img:
                nacionalidade = (
                    nacao_img.get("title")
                    or nacao_img.get("alt")
                    or ""
                )

            registro = {
                "jogador": dados[3],
                "posicao": dados[4],
                "clube": clube,
                "nacionalidade": nacionalidade,

                "partidas": dados[7],
                "suspensoes_amarelo": dados[8],
                "cartoes_amarelos": dados[9],
                "segundo_amarelo": dados[10],
                "cartoes_vermelhos": dados[11],
                "expulsoes": dados[12],
                "pontos_disciplinares": dados[13],
                "cartoes_por_partida": (
                    dados[14]
                    if len(dados) > 14
                    else ""
                ),

                "temporada": temporada,
                "url_origem": url,
            }

            registros.append(
                registro
            )

        except Exception as erro:

            print(
                f"Erro: {erro}"
            )

    return registros