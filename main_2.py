# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-14
# --------------------------------------------------------------------------- #
# Rewrite code to use Players and Teams classes

import json
import requests
import matplotlib.pyplot as plt

from players import Players
from teams import Teams


HEADERS = {
        'Host': 'stats.nba.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) '
                      'Gecko/20100101 Firefox/72.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'x-nba-stats-origin': 'stats',
        'x-nba-stats-token': 'true',
        'Connection': 'keep-alive',
        'Referer': 'https://stats.nba.com/',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        }


def get_player_gamelog(player_id, season_year, season_type):
    parameters = {
        'DateFrom': '',
        'DateTo': '',
        'GameSegment': '',
        'LastNGames': '0',
        'LeagueID': '00',
        'Location': '',
        'MeasureType': 'Base',
        'Month': '0',
        'OpponentTeamID': '0',
        'Outcome': '',
        'PORound': '0',
        'PaceAdjust': 'N',
        'PerMode': 'Totals',
        'Period': '0',
        'PlayerID': player_id,
        'PlusMinus': 'N',
        'Rank': 'N',
        'Season': season_year,
        'SeasonSegment': '',
        'SeasonType': season_type,
        'ShotClockRange': '',
        'VsConference': '',
        'VsDivision': ''
        }

    endpoint = 'playergamelogs'
    request_url = f'https://stats.nba.com/stats/{endpoint}?'

    response = requests.get(request_url, headers=HEADERS, params=parameters)

    gamelog_headers = json.loads(response.content.decode())['resultSets'][0]['headers']
    gamelog_data = json.loads(response.content.decode())['resultSets'][0]['rowSet']

    gamelog = []

    for game in gamelog_data:
        gamelog.append(dict(zip(gamelog_headers, game)))

    gamelog_dict = {}
    gamelog_list = []

    for game in gamelog:
        gamelog_dict[game['GAME_DATE'][:10]] = game
        gamelog_list.append(game)

    gamelog_list.reverse()
    return gamelog_dict, gamelog_list


def get_shotchart_data(player_id, season_year, game_id):
    parameters = {
        'AheadBehind': '',
        'CFID': '',
        'CFPARAMS': '',
        'ClutchTime': '',
        'Conference': '',
        'ContextFilter': '',
        'ContextMeasure': 'FGA',
        'DateFrom': '',
        'DateTo': '',
        'Division': '',
        'EndPeriod': '1',
        'EndRange': '0',
        'GROUP_ID': '',
        'GameEventID': '',
        'GameID': game_id,
        'GameSegment': '',
        'GroupID': '',
        'GroupMode': '',
        'GroupQuantity': '0',
        'LastNGames': '0',
        'LeagueID': '00',
        'Location': '',
        'Month': '0',
        'OnOff': '',
        'OpponentTeamID': '0',
        'Outcome': '',
        'PORound': '0',
        'Period': '0',
        'PlayerID': player_id,
        'PlayerID1': '',
        'PlayerID2': '',
        'PlayerID3': '',
        'PlayerID4': '',
        'PlayerID5': '',
        'PlayerPosition': '',
        'PointDiff': '',
        'Position': '',
        'RangeType': '0',
        'RookieYear': '',
        'Season': season_year,
        'SeasonSegment': '',
        'SeasonType': 'Regular Season',
        'ShotClockRange': '',
        'StartPeriod': '1',
        'StartRange': '0',
        'StarterBench': '',
        'TeamID': '0',
        'VsConference': '',
        'VsDivision': '',
        'VsPlayerID1': '',
        'VsPlayerID2': '',
        'VsPlayerID3': '',
        'VsPlayerID4': '',
        'VsPlayerID5': '',
        'VsTeamID': ''
        }

    endpoint = 'shotchartdetail'
    request_url = f'https://stats.nba.com/stats/{endpoint}?'

    response = requests.get(request_url, headers=HEADERS, params=parameters)
    # clean_response = clean_data(response)
    # all_shot_data = clean_response['Shot_Chart_Detail']

    all_shot_data = json.loads(response.content.decode())['resultSets'][0]

    all_shot_data_list = []

    name = all_shot_data['name']
    headers = all_shot_data['headers']
    row_set = all_shot_data['rowSet']

    for shot in row_set:
        all_shot_data_list.append(dict(zip(headers, shot)))
    #
    # for shot in all_shot_data:
    #     rows = []
    #     for raw_row in row_set:
    #         row = {}
    #         for i in range(len(headers)):
    #             row[headers[i]] = raw_row[i]
    #         rows.append(row)
    #     all_shot_data_list[name] = rows

    return all_shot_data_list


def plot_short_chart(all_shots, player_name, team_name, matchup, game_date,
                     scoring_headline):
    # TODO D. Rodriguez 2020-04-22: Cleanup variable quantity, maybe read
    #  data directly from all_shots?

    x_all = []
    y_all = []

    x_made = []
    y_made = []

    x_miss = []
    y_miss = []

    for shot in all_shots:
        x_all.append(shot['LOC_X'])
        y_all.append(shot['LOC_Y'])

        if shot['SHOT_MADE_FLAG']:
            x_made.append(shot['LOC_X'])
            y_made.append(shot['LOC_Y'])
        else:
            x_miss.append(shot['LOC_X'])
            y_miss.append(shot['LOC_Y'])

    # TODO D. Rodriguez 2020-04-22: Add shot info to each shot marker
    #  while hovering

    im = plt.imread('shotchart-blue.png')
    fig, ax = plt.subplots()
    ax.imshow(im, extent=[-260, 260, -65, 424])

    ax.scatter(x_miss, y_miss, marker='x', c='red')
    ax.scatter(x_made, y_made, facecolors='none', edgecolors='green')

    plt.title(f'{player_name} ({team_name})\n{scoring_headline}\n{matchup} {game_date}')
    ax.axes.xaxis.set_visible(False)
    ax.axes.yaxis.set_visible(False)

    plt.show()


if __name__ == '__main__':

    player_full_name = input('Enter player name (Last, First): ')

    # TODO (D. Rodriguez 2020-05-14): Fix code sequence.
    player = Players(player_full_name)

    # Updates Player team-related attributes
    # player_current_team = Teams(player.current_team_id)

    player.get_player_per_season_totals()
    player.get_player_seasons_played()

    all_seasons = player.seasons_played

    for season in all_seasons:
        print(season)

    season_year_user_input = input('Enter season: ')

    gamelog_dict, gamelog_list = get_player_gamelog(player.id,
                                                    season_year_user_input,
                                                    'Regular Season')

    # TODO (D. Rodriguez, 2020-04-27): Print games in table format
    game_count = 0
    for game in gamelog_list:
        game_count += 1
        print(game_count, game['GAME_DATE'][:10], game['MATCHUP'], f"({game['PTS']} pts, "
                                                       f"on {game['FGM']}/"
                                                       f"{game['FGA']} "
                                                       f"shooting)")

    game_date_user_input = input('Game date: ')

    game_id = gamelog_dict[game_date_user_input]['GAME_ID']
    matchup = gamelog_dict[game_date_user_input]['MATCHUP']
    game_date = gamelog_dict[game_date_user_input]['GAME_DATE'][:10]
    player_name = gamelog_dict[game_date_user_input]['PLAYER_NAME']
    team_name = gamelog_dict[game_date_user_input]['TEAM_ABBREVIATION']

    scoring_headline = f"{gamelog_dict[game_date_user_input]['PTS']} pts " \
                       f"on {gamelog_dict[game_date_user_input]['FGM']}/" \
                       f"{gamelog_dict[game_date_user_input]['FGA']} shooting " \
                       f"{gamelog_dict[game_date_user_input]['FG3M']}/" \
                       f"{gamelog_dict[game_date_user_input]['FG3A']} from three"

    all_shots = get_shotchart_data(player.id, season_year_user_input, game_id)

    plot_short_chart(all_shots, player_name, team_name, matchup, game_date, scoring_headline)

    # TODO (D. Rodriguez 2020-05-15): Move this to a new module? function?
    # Display teams played each season
    # for key, value in player.season_totals.items():
        # team = Teams(player.season_totals[key]["TEAM_ID"])
        # print(f'{key}: {team.nickname}')
