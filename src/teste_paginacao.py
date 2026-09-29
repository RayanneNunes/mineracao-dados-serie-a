import requests
from bs4 import BeautifulSoup

url = (
    "https://www.transfermarkt.com/"
    "campeonato-brasileiro-serie-a/assistliste/"
    "wettbewerb/BRA1/saison_id/2025"
)

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/128.0.0.0 Safari/537.36"
    )
}

html = requests.get(
    url,
    headers=headers
).text

soup = BeautifulSoup(html, "html.parser")

for a in soup.find_all("a", href=True):

    texto = a.get_text(strip=True)

    if texto in [
        "1", "2", "3", "4", "5",
        "6", "7", "8", "9", "10",
        ">", ">>"
    ]:

        print(
            f"Texto: {texto}"
        )

        print(
            f"Href: {a['href']}"
        )

        print("-" * 50)
