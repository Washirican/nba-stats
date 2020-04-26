# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-04-17
# --------------------------------------------------------------------------- #

# TODO D. Rodriguez 2020-04-17: Get box score data for a given game
# TODO D. Rodriguez 2020-04-20: Get player basic data
# TODO D. Rodriguez 2020-04-20: Get game IDs
# TODO D. Rodriguez 2020-04-20: Get team data
# TODO D. Rodriguez 2020-04-20: Create basic UI

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


def clean_data(response):
    raw_data = response.json()
    results = raw_data['resultSets']

    data = {}

    for result in results:
        name = result['name']
        headers = result['headers']
        row_set = result['rowSet']

        rows = []
        for raw_row in row_set:
            row = {}
            for i in range(len(headers)):
                row[headers[i]] = raw_row[i]
            rows.append(row)
        data[name] = rows

    return data


def get_shotchart_data(player_id, season_id, game_id):
    parameters = {'AheadBehind': '',
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
                  'Season': season_id,
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
                  'VsTeamID': ''}

    endpoint = 'shotchartdetail'
    request_url = f'https://stats.nba.com/stats/{endpoint}?'

    response = requests.get(request_url, headers=HEADERS, params=parameters)
    clean_response = clean_data(response)
    all_shot_data = clean_response['Shot_Chart_Detail']

    # returns a list of shot dictionaries
    return all_shot_data


def plot_short_chart(all_shots):
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

    ax.scatter(x_miss, y_miss, marker='x', c='red')  # c=color, marker=marker)
    ax.scatter(x_made, y_made, facecolors='none', edgecolors='green')  # c=color, marker=marker)

    # TODO (D. Rodriguez 2020-04-24): Fix Figure title to show correct teams for player
    # plt.title(f'{all_shots[0]["PLAYER_NAME"]} ({all_shots[0]["HTM"]}) vs {all_shots[0]["VTM"]}')
    plt.show()


if __name__ == '__main__':

    # Player IDs Test Variables:
    # bron_id = '2544'
    # harden_id = '201935'
    # lillard_id = '203081'
    # mj_id = '893'
    # kobe_id = '977'

    # Team IDs Test Variables
    # LAL_id = '1610612747'

    # Test Game IDs
    # kobe_81_id = 0020500591 (2005-06)

    player_id = '977'
    season_id = '1996-97'
    game_id = '0029601189'
    #
    shot_data = get_shotchart_data(player_id, season_id, game_id)
    plot_short_chart(shot_data)

