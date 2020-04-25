# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-04-24
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


# TODO (D. Rodriguez 2020-04-24): Inputs are player ID and season
def get_player_gamelog():
    pass


if __name__ == '__main__':
    parameters = {
            "DateFrom": "",
            "DateTo": "",
            "GameSegment": "",
            "LastNGames": "0",
            "LeagueID": "00",
            "Location": "",
            "MeasureType": "Base",
            "Month": "0",
            "OpponentTeamID": "0",
            "Outcome": "",
            "PORound": "0",
            "PaceAdjust": "N",
            "PerMode": "Totals",
            "Period": "0",
            "PlayerID": "201935",
            "PlusMinus": "N",
            "Rank": "N",
            "Season": "2018-19",
            "SeasonSegment": "",
            "SeasonType": "Regular Season",
            "ShotClockRange": "",
            "VsConference": "",
            "VsDivision": ""
        }

    endpoint = 'playergamelogs'
    request_url = f'https://stats.nba.com/stats/{endpoint}?'

    response = requests.get(request_url, headers=HEADERS, params=parameters)

    # player_gamelog_dict = json.loads(response.content.decode())['resultSets'][0]

    player_gamelog_headers = json.loads(response.content.decode())['resultSets'][0]['headers']
    player_gamelog_data = json.loads(response.content.decode())['resultSets'][0]['rowSet']

    season_id = player_gamelog_data[0][0]
    game_id = player_gamelog_data[0][6]
    game_teams = player_gamelog_data[0][8]
