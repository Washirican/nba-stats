# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-01-18
# References:
#   https://github.com/seemethere/nba_py/wiki/stats.nba.com-Endpoint-Documentation
#   https://www.youtube.com/watch?v=NCyPY-jfb3I
#   https://github.com/swar/nba_api
# --------------------------------------------------------------------------- #
import pandas as pd
from nba_api.stats.static import players

player_dict = players.get_players()

bron = [player for player in player_dict if player['full_name'] == 'LeBron James'][0]
bron_id = bron['id']

from nba_api.stats.static import teams
team_dict = teams.get_teams()
GSW = [team for team in team_dict if team['full_name'] == 'Golden State Warriors'][0]
GSW_id = GSW['id']

from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll

gamelog_bron = playergamelog.PlayerGameLog(player_id=bron_id, season='2017')
gamelog_bron_df = gamelog_bron.get_data_frames()[0]


gamelog_bron_all = playergamelog.PlayerGameLog(player_id=bron_id, season=SeasonAll.all)
gamelog_bron_df_all = gamelog_bron_all.get_data_frames()[0]

from nba_api.stats.endpoints import leaguegamefinder
GSW_games = leaguegamefinder.LeagueGameFinder(team_id_nullable=GSW_id).get_data_frames()[0]
