# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-04-25
# --------------------------------------------------------------------------- #

import get_player_data
import get_player_career_stats
import get_player_gamelog
import get_shotchart_data
import plot_shotchart


if __name__ == '__main__':
    first_name = 'LeBron'
    last_name = 'James'

    player_info = get_player_data.get_player_data(last_name, first_name)
    player_id = player_info[0]
    player_name = player_info[1]

    all_seasons = get_player_career_stats.get_player_seasons(player_id)
    # Selects Rookie Season
    season = len(all_seasons) - 1
    season_year = all_seasons[season]

    gamelog_dict, gamelog_list = get_player_gamelog.get_player_gamelog(player_id, season_year, 'Regular Season')
    # Select first game of the season
    game = 0
    game_id = gamelog_list[game]['GAME_ID']
    matchup = gamelog_list[game]['MATCHUP']
    game_date = gamelog_list[game]['GAME_DATE'][:10]
    player_name = gamelog_list[game]['PLAYER_NAME']
    team_name = gamelog_list[game]['TEAM_ABBREVIATION']

    all_shots = get_shotchart_data.get_shotchart_data(player_id, season_year, game_id)

    plot_shotchart.plot_shortchart(all_shots, player_name, team_name, matchup, game_date)
