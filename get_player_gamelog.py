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


# TODO (D. Rodriguez 2020-04-24): Inputs are player ID, season year and type
def get_player_gamelog(player_id, season_year, season_type):
    parameters = {
        'DateFrom': '',
        'DateTo': '',
        'GameSegment': '',
        'LastNGames': '0',
        'LeagueID': '00',
        'Location': '',
        'MeasureType': 'Base',
        'Month': '0',
        'OpponentTeamID': '0',
        'Outcome': '',
        'PORound': '0',
        'PaceAdjust': 'N',
        'PerMode': 'Totals',
        'Period': '0',
        'PlayerID': player_id,
        'PlusMinus': 'N',
        'Rank': 'N',
        'Season': season_year,
        'SeasonSegment': '',
        'SeasonType': season_type,
        'ShotClockRange': '',
        'VsConference': '',
        'VsDivision': ''
        }

    endpoint = 'playergamelogs'
    request_url = f'https://stats.nba.com/stats/{endpoint}?'

    response = requests.get(request_url, headers=HEADERS, params=parameters)

    gamelog_headers = json.loads(response.content.decode())['resultSets'][0]['headers']
    gamelog_data = json.loads(response.content.decode())['resultSets'][0]['rowSet']

    gamelog = []

    for game in gamelog_data:
        gamelog.append(dict(zip(gamelog_headers, game)))

    gamelog_dict = {}
    gamelog_list = []

    for game in gamelog:
        gamelog_dict[game['GAME_DATE'][:10]] = game
        gamelog_list.append(game)

    return gamelog_dict, gamelog_list


# if __name__ == '__main__':
#     player_id = '893'
#     season_year = '1997-98'
#     season_type = 'Regular Season'
#
    # gamelog_dict = get_player_gamelog(player_id, season_year, season_type)



