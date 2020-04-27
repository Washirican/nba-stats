# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-04-25
# --------------------------------------------------------------------------- #

import get_player_data
import get_player_career_stats
import get_player_gamelog
import shotchart

if __name__ == '__main__':
    first_name = 'LeBron'
    last_name = 'James'

    player_info = get_player_data.get_player_data(last_name, first_name)
    player_id = player_info[0]
    player_name = player_info[1]

    all_seasons = get_player_career_stats.get_player_seasons(player_id)
    rookie_season_year = all_seasons[0]

    gamelog_dict, gamelog_list = get_player_gamelog.get_player_gamelog(player_id, rookie_season_year, 'Regular Season')
    game_id = gamelog_list[0]['GAME_ID']

    all_shots = shotchart.get_shotchart_data(player_id, rookie_season_year, game_id)

    shotchart.plot_short_chart(all_shots)
