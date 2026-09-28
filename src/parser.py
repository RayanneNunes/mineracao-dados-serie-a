from bs4 import BeautifulSoup


def extrair_jogadores(html, temporada, url):

    soup = BeautifulSoup(html, "html.parser")

    tabela = soup.find("table", class_="items")

    print(f"Tabela encontrada: {tabela is not None}")

    if tabela is None:
        return []

    registros = []

    linhas = tabela.find_all("tr")

    print(f"Total de linhas encontradas: {len(linhas)}")

    for linha in linhas:

        colunas = linha.find_all("td")

        # Ignora cabeçalho ou linhas vazias
        if len(colunas) < 10:
            continue

        try:

            dados = [
                td.get_text(" ", strip=True)
                for td in colunas
            ]

            # DEBUG
            print(f"Qtd colunas: {len(dados)}")

            if len(dados) >= 14:

                registro = {
                    "jogador": dados[3] if len(dados) > 3 else "",
                    "posicao": dados[4] if len(dados) > 4 else "",
                    "idade": dados[8] if len(dados) > 8 else "",
                    "jogos": dados[9] if len(dados) > 9 else "",
                    "substituicoes_entrada": dados[10] if len(dados) > 10 else "",
                    "substituicoes_saida": dados[11] if len(dados) > 11 else "",
                    "gols": dados[12] if len(dados) > 12 else "",
                    "assistencias": dados[13] if len(dados) > 13 else "",
                    "temporada": temporada,
                    "url_origem": url
                }

                registros.append(registro)

        except Exception as erro:
            print(f"Erro: {erro}")

    print(f"Registros extraídos: {len(registros)}")

    return registros