# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-04-17
# --------------------------------------------------------------------------- #

# TODO D. Rodriguez 2020-04-17: Get box score data for a given game
# TODO D. Rodriguez 2020-04-20: Get player basic data
# TODO D. Rodriguez 2020-04-20: Get game IDs
# TODO D. Rodriguez 2020-04-20: Get team data
# TODO D. Rodriguez 2020-04-20: Create basic UI

import requests
import matplotlib.pyplot as plt

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


def clean_data(response):
    raw_data = response.json()
    results = raw_data['resultSets']

    data = {}

    for result in results:
        name = result['name']
        headers = result['headers']
        row_set = result['rowSet']

        rows = []
        for raw_row in row_set:
            row = {}
            for i in range(len(headers)):
                row[headers[i]] = raw_row[i]
            rows.append(row)
        data[name] = rows

    return data


def get_boxscore_data(game_id):
    parameters = {'GameID': game_id}
    endpoint = 'boxscoresummaryv2'
    request_url = f'https://stats.nba.com/stats/{endpoint}?'

    response = requests.get(request_url, headers=HEADERS, params=parameters)
    result = clean_data(response)

    return result


if __name__ == '__main__':
    game_id = '0021900652'
    boxscore_data = get_boxscore_data(game_id)
    print('Box Score data keys: ')
    print(boxscore_data['InactivePlayers'])

    bron_id = 2544
    LAL_id = 1610612747
