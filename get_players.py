# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-04-22
# --------------------------------------------------------------------------- #

import json
import requests


def get_player_info(first_name, last_name):
    """Ger player id from Player Name"""
    player_index_url = 'https://stats.nba.com/js/data/ptsd/stats_ptsd.js'
    player_list = requests.get(player_index_url)

    # Cleanup string
    dict_str = player_list.content.decode()[17:-1]

    # Turns string into dictionary
    data = json.loads(dict_str)
    players = data['data']['players']
    teams = data['data']['teams']
    data_date = data['generated']

    # print(data_date)

    # first_name = 'Kobe'
    # last_name = 'Bryant'

    for player in players:
        # print(player[1])
        if f'{last_name}, {first_name}' in player[1]:
            # print(player[:])
            player_info = player
            return player_info
        # else:
        # print(f'Player {first_name.title()} {last_name.title()} not found in database.')

    # TODO (D. Rodriguez 2020-04-24): Break if team name not found
    # for team in teams:
    #     if str(team_id) in team[0]:
    #         print(team[:5])

    #
    return 0


# if __name__ == '__main__':
#     first_name = 'LeBron'
#     last_name = 'James'
#
#     player_info = get_player_info(first_name, last_name)
#     print(player_info)
