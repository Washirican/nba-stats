# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-02-08
# --------------------------------------------------------------------------- #

# Using requests package

import requests

bron_id = 2544
LAL_id = 1610612747

request_url = 'http://stats.nba.com/stats/shotchartdetail'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) \
           Gecko/20100101 Firefox/72.0',
           'Host': 'stats.nba.com',
           'Connection': 'keep-alive',
           'Accept-Language': 'en-US,en;q=0.5',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept': 'application/json, text/plain, */*'}

parameters = {'LeagueID': '00',
              'Season': '2019-20',
              'SeasonType': 'Regular Season',
              'TeamID': 1610612745,
              'PlayerID': 201935,
              'GameID': '0021900282',
              'Outcome': '',
              'Location': '',
              'Month': 0,
              'SeasonSegment': '',
              'DateFrom': '',
              'DateTo': '',
              'OpponentTeamID': 0,
              'VsConference': '',
              'VsDivision': '',
              'Position': '',
              'RookieYear': '',
              'GameSegment': '',
              'Period': 0,
              'LastNGames': 0,
              'ClutchTime': '',
              'AheadBehind': '',
              'PointDiff': '',
              'RangeType': 0,
              'StartPeriod': 1,
              'EndPeriod': 10,
              'StartRange': 0,
              'EndRange': 28800,
              'ContextFilter': '',
              'ContextMeasure': 'FGA'}

response = requests.get(request_url, headers=headers, params=parameters)
