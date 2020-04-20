# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-04-17
# --------------------------------------------------------------------------- #

# TODO D. Rodriguez 2020-04-17: Get box score data for a given game

import requests


def get_box_score():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) '
                      'Gecko/20100101 Firefox/75.0',
        'Host': 'stats.nba.com',
        'Connection': 'keep-alive',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': 'application/json, text/plain, */*'
        }

    game_id = '0021800944'

    request_url = f'https://stats.nba.com/stats/boxscoresummaryv2?' \
                  f'GameID={game_id}'
    result = requests.get(request_url, headers=headers)
    return result


if __name__ == '__main__':
    print('NBA Box Score')
    box_score_data = get_box_score()
    print(f'Box Score data: {box_score_data}')
