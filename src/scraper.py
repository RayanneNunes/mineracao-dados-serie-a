import requests
from bs4 import BeautifulSoup


def obter_html(url, headers):

    response = requests.get(
        url,
        headers=headers,
        timeout=30
    )

    response.raise_for_status()

    return response.text


def descobrir_paginas(url, headers):

    html = obter_html(url, headers)

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    paginas = set()

    for a in soup.find_all("a", href=True):

        href = a["href"]

        if "/page/" in href:

            try:

                numero = int(
                    href.split("/page/")[1]
                )

                paginas.add(numero)

            except ValueError:
                pass

    total_paginas = max(paginas) if paginas else 1

    return total_paginas