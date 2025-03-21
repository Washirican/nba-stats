# --------------------------------------------------------------------------- #
# D. Rodriguez, 2025-03-18
# --------------------------------------------------------------------------- #

import requests
# from urllib3 import urlencode
import urllib.parse


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



def get_play_by_play_data(game_id):
    game_id = '0022400985'
    parameters = {'GameID': game_id,
                  'StartPeriod': 1,
                  'EndPeriod' : 4,
                  }
    endpoint = 'playbyplayv3'
    request_url = f'https://stats.nba.com/stats/{endpoint}?'

    response = requests.get(request_url, headers=HEADERS, params=urllib.parse.urlencode(parameters))
    raw_data = response.json()

    print(f"Found {len(raw_data['game']['actions'])} game events")


    return result