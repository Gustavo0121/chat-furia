"""Get info."""

import os
from dotenv import load_dotenv
import requests

load_dotenv()

PANDA_API = os.getenv('PANDA_API')
IDFURIA = 124530
HEADERS = {
    "accept": "application/json",
    "authorization": f"Bearer {PANDA_API}",
}
BASE_URL = "https://api.pandascore.co"


def get_recent_achievements() -> str:
    """Obter os torneios recentes onde a Fúria ganhou."""
    response = requests.get(
        f"{BASE_URL}/teams/{IDFURIA}/tournaments", 
        headers=HEADERS,
        proxies={"http": None, "https": None},
    )

    tournaments = response.json()
    tournaments_win = ''
    for tournament in tournaments:
        if tournament['serie']['winner_id'] == 124530:
            tournaments_win += f"- {tournament['league']['name']} {tournament['name']} {tournament['serie']['year']}\n"

    return tournaments_win

def get_current_roster() -> str:
    """Elenco atual dos jogadores."""
    response = requests.get(
        f"{BASE_URL}/teams/{IDFURIA}",
        headers=HEADERS,
        proxies={"http": None, "https": None},
    )

    players = response.json()
    roster = ''
    for player in players['players']:
        roster += f"- {player['name']} ({player['first_name']} {player['last_name']})\n"
    return roster

def get_upcoming_matches_and_tournaments() -> str:
    """Próximas partidas e torneios."""
    response_matches = requests.get(
        f"{BASE_URL}/csgo/matches/upcoming",
        headers=HEADERS,
        proxies={"http": None, "https": None},
    )
    response_tournaments = requests.get(
        f"{BASE_URL}/csgo/tournaments/upcoming",
        headers=HEADERS,
        proxies={"http": None, "https": None},
    )

    matches = response_matches.json()
    tournaments = response_tournaments.json()
    upcoming_matches = ''
    upcoming_tournaments = ''

    for partida in matches:
        if 'FURIA' in partida['name']:
            upcoming_matches += f"- {partida['name']} {partida['serie']['full_name']}\n"

    for tournament in tournaments:
        for team in tournament['teams']:
            if team['name'] == 'FURIA':
                upcoming_tournaments += f"- {tournament['serie']['full_name']}\n"


    return f"Próximas partidas:\n{upcoming_matches}\nPróximos Torneios:\n{upcoming_tournaments}"

if __name__ == '__main__':
    get_recent_achievements()
    get_current_roster()
    get_upcoming_matches_and_tournaments()