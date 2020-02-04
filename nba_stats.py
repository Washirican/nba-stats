# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-01-18
# References:
#   https://github.com/seemethere/nba_py/wiki/stats.nba.com-Endpoint-Documentation
# --------------------------------------------------------------------------- #
import requests

# Make an API call and store the response.
base_url = 'https://stats.nba.com/'

# Harden 60 point shot chart
# ?flag=3&CFID=&CFPARAMS=&PlayerID=201935&TeamID=1610612745&GameID=0021900282&ContextMeasure=FGA&Season=2019-20&SeasonType=Regular%20Season&RangeType=0&StartPeriod=1&EndPeriod=10&StartRange=0&EndRange=28800&section=game&sct=plot
# Lillard 60 point shot chart
# ?flag=3&CFID=&CFPARAMS=&PlayerID=203081&TeamID=1610612757&GameID=0021900125&ContextMeasure=FGA&Season=2019-20&SeasonType=Regular%20Season&RangeType=0&StartPeriod=1&EndPeriod=10&StartRange=0&EndRange=28800&section=game&sct=plot
# Total Points Leaders
# events/
# endpoint = 'players/traditional/'
# params = '?PerMode=Totals&sort=PTS&dir=-1'

endpoint = 'game/'
params = '0021900741/shotchart/'


url = base_url + endpoint + params

print(url)

headers = {'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/45.0.2454.101 Safari/537.36'),
           'referer': 'http://stats.nba.com/scores/'}

r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
print(r.headers['content-type'])

f = open('nba-data.html', 'wb')
f.write(r.content)
f.close()


