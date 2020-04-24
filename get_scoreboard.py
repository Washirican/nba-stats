# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-04-23
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


def get_scoreboard_data():
    """Gets score board data for game on a given date"""
    pass


if __name__ == '__main__':
    # score_board = get_scoreboard_data()

    parameters = {
        'DayOffset': '0',
        'LeagueID': '00',
        'gameDate': '03/11/2019'
        }

    endpoint = 'scoreboardV2'
    request_url = f'https://stats.nba.com/stats/{endpoint}?'

    response = requests.get(request_url, headers=HEADERS, params=parameters)
    scoreboard_data_dict = json.loads(response.content.decode())['resultSets']

    scoreboard_data_all_games_list = json.loads(response.content.decode())['resultSets'][0]['rowSet']

