#!/usr/bin/env python3
# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-02-08
# References:
#   https://github.com/swar/nba_api
# --------------------------------------------------------------------------- #

# Using nba_api package

from nba_api.stats.endpoints.shotchartdetail import ShotChartDetail
from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats.static import teams
from nba_api.stats.endpoints import commonplayerinfo
import charts


# TODO D. Rodriguez 2020-02-22: Get player name from user input
player_name = 'Giannis Antetokounmpo'

player_dict = players.get_players()
player = [player for player in player_dict if player['full_name'] == player_name][0]
player_id = player['id']

# Use Player ID to get team full name and team ID
player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id)
team_name = player_info.data_sets[0].data['data'][0][17]
team_city = player_info.data_sets[0].data['data'][0][20]
team_full_name = team_city + ' ' + team_name
team_id = player_info.data_sets[0].data['data'][0][16]

player_gamelog = playergamelog.PlayerGameLog(player_id=player_id, season='2019')
game_id = player_gamelog.data_sets[0].data['data'][0][2]
game_date = player_gamelog.data_sets[0].data['data'][0][3]
game_teams = player_gamelog.data_sets[0].data['data'][0][4]

shot_chart_detail = ShotChartDetail(player_id=player_id, team_id=team_id,
                                    game_id_nullable=game_id,
                                    context_measure_simple='FGA')

headers = shot_chart_detail.data_sets[0].data['headers']
shots = shot_chart_detail.data_sets[0].data['data']

x_all = []
y_all = []

x_made = []
y_made = []

x_miss = []
y_miss = []

for shot in shots:
    x_all.append(shot[17])
    y_all.append(shot[18])

    if shot[20]:
        x_made.append(shot[17])
        y_made.append(shot[18])
    else:
        x_miss.append(shot[17])
        y_miss.append(shot[18])

chart_title = player_name + ' ' + game_date + ' ' + game_teams

chart = charts.shot_chart(x_made, y_made,
                          title=chart_title,
                          flip_court=True)

chart.scatter(x_miss, y_miss, color='r', marker='x')
