# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-04-22
# --------------------------------------------------------------------------- #

import json
import requests

# TODO D. Rodriguez 2020-04-22: Scrape NBA Stats Team Index for player
#  names and IDs

player_index_url = 'https://stats.nba.com/js/data/ptsd/stats_ptsd.js'
player_list = requests.get(player_index_url)

# Cleanup string
dict_str = player_list.content.decode()[17:-1]

# Turns string into dictionary
data = json.loads(dict_str)
players = data['data']['players']
teams = data['data']['teams']
data_date = data['generated']

first_name = 'Michael'
last_name = 'Jordan'

for player in players:
    # print(player[1])
    if f'{last_name.title()}, {first_name.title()}' in player[1]:
        print(player[:])
        team_id = player[5]
        # break
    # else:
    # print(f'Player {first_name.title()} {last_name.title()} not found in database.')

# TODO (D. Rodriguez 2020-04-24): Break if team name not found
# for team in teams:
#     if str(team_id) in team[0]:
#         print(team[:5])

# TODO (D. Rodriguez, 2020-04-22): Save player and team info to database
#  (sqlite3/MongoDB)

