import requests
from bs4 import BeautifulSoup


def obter_html(url: str, headers: dict) -> str:
    response = requests.get(
        url,
        headers=headers,
        timeout=30,
    )

    response.raise_for_status()

    return response.text


def descobrir_paginas(
    url: str,
    headers: dict,
) -> int:

    html = obter_html(
        url,
        headers,
    )

    soup = BeautifulSoup(
        html,
        "html.parser",
    )

    paginas = set()

    for a in soup.find_all(
        "a",
        href=True,
    ):
        href = a["href"]

        if "/page/" not in href:
            continue

        try:
            numero = int(
                href.split("/page/")[1]
                .split("?")[0]
                .split("/")[0]
            )

            paginas.add(numero)

        except ValueError:
            continue

    return max(paginas) if paginas else 1