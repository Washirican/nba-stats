# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-04-17
# --------------------------------------------------------------------------- #

# TODO D. Rodriguez 2020-04-17: Get box score data for a given game
# TODO D. Rodriguez 2020-04-20: Get player basic data
# TODO D. Rodriguez 2020-04-20: Get game IDs
# TODO D. Rodriguez 2020-04-20: Get team data
# TODO D. Rodriguez 2020-04-20: Create basic UI

import requests

HEADERS = {
        'Host': 'stats.nba.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'x-nba-stats-origin': 'stats',
        'x-nba-stats-token': 'true',
        'Connection': 'keep-alive',
        'Referer': 'https://stats.nba.com/',
        # 'Referer': 'https://stats.nba.com/events/?flag=3&CFID=&CFPARAMS=&PlayerID=203081&TeamID=1610612757&GameID=0021900652&ContextMeasure=FGA&Season=2019-20&SeasonType=Regular%20Season&LeagueID=00&PlusMinus=N&PaceAdjust=N&Rank=N&Outcome=&Location=&Month=0&SeasonSegment=&OpponentTeamID=0&VsConference=&VsDivision=&GameSegment=&Period=0&LastNGames=0&DateFrom=&DateTo=&PORound=0&ShotClockRange=&PerMode=Totals&MeasureType=Base&section=player&sct=plot',
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
    # game_id = '0021800944'
    parameters = {'GameID': '0021800944'}
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

    return all_shot_data


def plot_shortchart(shot_data):
    pass


if __name__ == '__main__':
    # boxscore_data = get_boxscore_data()
    # print('Box Score data keys: ')
    # print(boxscore_data['InactivePlayers'])

    shot_data = get_shotchart_data()
    print('Shot Chart data keys: ')
    print(shot_data)
