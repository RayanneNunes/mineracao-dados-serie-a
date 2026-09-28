# Temporadas que serão coletadas

TEMPORADAS = [2022, 2023, 2024, 2025]

# URL da página de estatísticas

BASE_URL = (
    "https://www.transfermarkt.com/"
    "campeonato-brasileiro-serie-a/scorerliste/"
    "wettbewerb/BRA1/saison_id/{temporada}/"
    "altersklasse/alle/plus/1"
)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/128.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9"
}

INTERVALO = 5