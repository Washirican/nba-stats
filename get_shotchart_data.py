# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-04-17
# --------------------------------------------------------------------------- #

# TODO D. Rodriguez 2020-04-17: Get box score data for a given game
# TODO D. Rodriguez 2020-04-20: Get player basic data
# TODO D. Rodriguez 2020-04-20: Get game IDs
# TODO D. Rodriguez 2020-04-20: Get team data
# TODO D. Rodriguez 2020-04-20: Create basic UI

import requests
import json

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


# if __name__ == '__main__':

    # Player IDs Test Variables:
    # bron_id = '2544'
    # harden_id = '201935'
    # lillard_id = '203081'
    # mj_id = '893'
    # kobe_id = '977'

    # Test Game IDs
    # kobe_81_id = 0020500591 (2005-06)

    # game_id = '0020300014'
    # player_id = '2544'
    # season_year = '2003-04'


    # shot_data = get_shotchart_data(player_id, season_year, game_id)
    # plot_shortchart(shot_data)



