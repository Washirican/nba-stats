# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-04-25
# --------------------------------------------------------------------------- #

import requests
import json


HEADERS = {
        'Host': 'stats.nba.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) '
                      'Gecko/20100101 Firefox/72.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'x-nba-stats-origin': 'stats',
        'x-nba-stats-token': 'true',
        'Connection': 'keep-alive',
        'Referer': 'https://stats.nba.com/',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        }


def get_player_seasons(player_id):
    """Get player career stats per player ID"""
    parameters = {
        'LeagueID': '00',
        'PerMode': 'PerGame',
        'PlayerID': player_id
        }

    endpoint = 'playerprofilev2'
    request_url = f'https://stats.nba.com/stats/{endpoint}?'

    response = requests.get(request_url, headers=HEADERS, params=parameters)
    player_career_stats_dict = \
    json.loads(response.content.decode())['resultSets'][0]['rowSet']

    player_career_seasons = []

    for season in player_career_stats_dict:
        player_career_seasons.append(season[1])

    return player_career_seasons


# if __name__ == '__main__':
#     player_id = '2544'
#     all_seasons = get_player_seasons(player_id)
#     print(all_seasons)
