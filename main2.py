# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-04-26
# --------------------------------------------------------------------------- #

import json
import requests
import matplotlib.pyplot as plt


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


def get_player_data(last_name, first_name):
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


def get_player_seasons(player_id):
    """Get player career stats per player ID"""
    parameters = {
        'LeagueID': '00',
        'PerMode': 'PerGame',
        'PlayerID': player_id
        }

    endpoint = 'playerprofilev2'
    request_url = f'https://stats.nba.com/stats/{endpoint}?'

    response = requests.get(request_url, headers=HEADERS, params=parameters)
    player_career_stats_dict = \
    json.loads(response.content.decode())['resultSets'][0]['rowSet']

    player_career_seasons = []

    for season in player_career_stats_dict:
        player_career_seasons.append(season[1])

    return player_career_seasons


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

    # TODO (D. Rodriguez 2020-04-26): Fix getting all shot data from API
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


def plot_shortchart(all_shots, player_name, team_name, matchup, game_date):
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

    plt.title(f'{player_name} ({team_name}), \n{matchup} {game_date}')
    ax.axes.xaxis.set_visible(False)
    ax.axes.yaxis.set_visible(False)

    plt.show()


if __name__ == '__main__':
    first_name = 'Damian'
    last_name = 'Lillard'

    player_info = get_player_data(last_name, first_name)
    player_id = player_info[0]
    player_name = player_info[1]

    all_seasons = get_player_seasons(player_id)
    # Selects Rookie Season
    season = len(all_seasons) - 1
    season_year = all_seasons[season]

    gamelog_dict, gamelog_list = get_player_gamelog(player_id, season_year, 'Regular Season')
    # Select first game of the season
    game = 0
    game_id = gamelog_list[game]['GAME_ID']
    matchup = gamelog_list[game]['MATCHUP']
    game_date = gamelog_list[game]['GAME_DATE'][:10]
    player_name = gamelog_list[game]['PLAYER_NAME']
    team_name = gamelog_list[game]['TEAM_ABBREVIATION']

    all_shots = get_shotchart_data(player_id, season_year, game_id)

    plot_shortchart(all_shots, player_name, team_name, matchup, game_date)

