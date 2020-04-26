# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-04-25
# --------------------------------------------------------------------------- #

import get_players
import get_player_career_stats
import get_player_gamelog
import shotchart

if __name__ == '__main__':
    player_id = get_players.get_player_id('Kobe', 'Bryant')
    season = get_player_career_stats.get_player_seasons(player_id)[12]
    gamelog_dict, gamelog_list = get_player_gamelog.get_player_gamelog(player_id, season, 'Regular Season')
    game_id = gamelog_list[2]['GAME_ID']

    all_shots = shotchart.get_shotchart_data(player_id, season, game_id)

    shotchart.plot_short_chart(all_shots)
