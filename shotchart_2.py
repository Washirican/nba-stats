# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-02-08
# --------------------------------------------------------------------------- #

# Using nba_api package

from nba_api.stats.endpoints.shotchartdetail import ShotChartDetail
from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats.static import teams

# team_dict = teams.get_teams()
# team_data = [team for team in team_dict if team['full_name'] == 'Houston Rockets'][0]
# team_id = team_data['id']
#
# player_dict = players.get_players()
# harden = [player for player in player_dict if player['full_name'] == 'James Harden'][0]
# player_id = harden['id']
#
# gamelog_harden = playergamelog.PlayerGameLog(player_id=player_id, season='2019')
# gamelog_harden_df = gamelog_harden.get_data_frames()[0]
#
# parameters = {'LeagueID': '00',
#               'Season': '2019-20',
#               'SeasonType': 'Regular Season',
#               'TeamID': team_id,
#               'PlayerID': player_id,
#               'GameID': '0021900282',
#               'Outcome': '',
#               'Location': '',
#               'Month': 0,
#               'SeasonSegment': '',
#               'DateFrom': '',
#               'DateTo': '',
#               'OpponentTeamID': 0,
#               'VsConference': '',
#               'VsDivision': '',
#               'Position': '',
#               'RookieYear': '',
#               'GameSegment': '',
#               'Period': 0,
#               'LastNGames': 0,
#               'ClutchTime': '',
#               'AheadBehind': '',
#               'PointDiff': '',
#               'RangeType': 0,
#               'StartPeriod': 1,
#               'EndPeriod': 10,
#               'StartRange': 0,
#               'EndRange': 28800,
#               'ContextFilter': '',
#               'ContextMeasure': 'FGA'}

player_id = '201935'
team_id = '1610612745'
game_id = '0021900768'

shot_chart_detail = ShotChartDetail(player_id=player_id, team_id=team_id,
                                    game_id_nullable=game_id,
                                    context_measure_simple='FGA')

headers = shot_chart_detail.data_sets[0].data['headers']
shots = shot_chart_detail.data_sets[0].data['data']

# TODO D. Rodriguez 2020-02-08: Plot shots with matplotlib or similar
print(headers[7:19])
for shot in shots:
    print(shot[7:19])

