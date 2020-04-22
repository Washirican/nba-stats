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
import numpy as np

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


def get_boxscore_data():
    parameters = {'GameID': '0021900652'}
    endpoint = 'boxscoresummaryv2'
    request_url = f'https://stats.nba.com/stats/{endpoint}?'

    response = requests.get(request_url, headers=HEADERS, params=parameters)
    result = clean_data(response)

    return result


def get_shotchart_data():
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
                  'EndPeriod': '10',
                  'EndRange': '28800',
                  'GROUP_ID': '',
                  'GameEventID': '',
                  'GameID': '0021900652',
                  'GameSegment': '',
                  'GroupID': '',
                  'GroupMode': '',
                  'GroupQuantity': '5',
                  'LastNGames': '0',
                  'LeagueID': '00',
                  'Location': '',
                  'Month': '0',
                  'OnOff': '',
                  'OpponentTeamID': '0',
                  'Outcome': '',
                  'PORound': '0',
                  'Period': '0',
                  'PlayerID': '203081',
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
                  'Season': '2019-20',
                  'SeasonSegment': '',
                  'SeasonType': 'Regular Season',
                  'ShotClockRange': '',
                  'StartPeriod': '1',
                  'StartRange': '0',
                  'StarterBench': '',
                  'TeamID': '1610612757',
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

    # fig = plt.figure()
    # ax = fig.add_subplot()
    #
    # ax.scatter(x_miss, y_miss, marker='x', c='red')  # c=color, marker=marker)
    # ax.scatter(x_made, y_made, facecolors='none', edgecolors='green')  # c=color, marker=marker)
    #
    # plt.title('Dame Dolla 61 Points')
    # plt.show()

    # TODO D. Rodriguez 2020-04-21: Try to plot shots over image
    im = plt.imread('shotchart-blue.png')
    fig, ax = plt.subplots()
    ax.imshow(im, extent=[-260, 260, -65, 424])

    ax.scatter(x_miss, y_miss, marker='x', c='red')  # c=color, marker=marker)
    ax.scatter(x_made, y_made, facecolors='none', edgecolors='green')  # c=color, marker=marker)

    plt.title('Dame Dolla 61 Points')
    plt.show()


if __name__ == '__main__':
    # boxscore_data = get_boxscore_data()
    # print('Box Score data keys: ')
    # print(boxscore_data['InactivePlayers'])

    shot_data = get_shotchart_data()
    # print('Shot Chart data keys: ')
    # print(shot_data)
    plot_short_chart(shot_data)
