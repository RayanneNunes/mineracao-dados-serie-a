from bs4 import BeautifulSoup


def extrair_jogadores(html, temporada, url):

    soup = BeautifulSoup(html, "html.parser")

    tabela = soup.find("table", class_="items")

    if tabela is None:
        return []

    registros = []

    linhas = tabela.find_all("tr")

    for linha in linhas:

        colunas = linha.find_all("td")

        if len(colunas) < 14:
            continue

        try:

            dados = [
                td.get_text(" ", strip=True)
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
                "jogos": dados[7],
                "idade": dados[8],
                "substituicoes_entrada": dados[9],
                "substituicoes_saida": dados[10],
                "gols": dados[11],
                "assistencias": dados[12],
                "participacao_gols": dados[13],
                "temporada": temporada,
                "url_origem": url
            }

            registros.append(registro)

        except Exception as erro:

            print(
                f"Erro ao processar registro: {erro}"
            )

    return registros