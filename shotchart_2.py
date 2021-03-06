# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-02-08
# References:
#   #   https://github.com/swar/nba_api
# --------------------------------------------------------------------------- #

# Using nba_api package

from nba_api.stats.endpoints.shotchartdetail import ShotChartDetail
from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats.static import teams
import charts

player_name = 'LeBron James'
team_name = 'Los Angeles Lakers'

player_dict = players.get_players()
player = [player for player in player_dict if player['full_name'] == player_name][0]
player_id = player['id']

# TODO D. Rodriguez 2020-02-20: How to get Team ID from Player Name
team_dict = teams.get_teams()
team = [team for team in team_dict if team['full_name'] == team_name][0]
team_id = team['id']

player_gamelog = playergamelog.PlayerGameLog(player_id=player_id, season='2019')

# TODO D. Rodriguez 2020-02-12: Make search function
# player_id = '2544'  # LeBron
# team_id = '1610612747'

# player_id = '201935'  # Harden
# team_id = '1610612745'
game_id = '0021900817'

shot_chart_detail = ShotChartDetail(player_id=player_id, team_id=team_id,
                                    game_id_nullable=game_id,
                                    context_measure_simple='FGA')

headers = shot_chart_detail.data_sets[0].data['headers']
shots = shot_chart_detail.data_sets[0].data['data']

x = []
y = []

# TODO D. Rodriguez 2020-02-12: Separate shots into made/missed
# print(headers[7:19])
for shot in shots:
    # print(shot)
    # print(shot[7:19])
    x.append(shot[17])
    y.append(shot[18])

chart = charts.shot_chart(x, y)
