# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-04-22
# --------------------------------------------------------------------------- #

import requests
from bs4 import BeautifulSoup as BS

# TODO D. Rodriguez 2020-04-22: Scrape NBA Stats Team Index for player
#  names and IDs

player_index_url = 'https://stats.nba.com/players/list/?Historic=Y'
page = requests.get(player_index_url)

soup = BS(page.content, 'html.parser')

players_list = soup.find_all('li', attrs={'class': 'players-list__name'})

# players_list = soup.find_all(class_='players-list__name')

# players = []
# for player in players_list.find_all('li', attrs={'class': 'players-list__name'}):
#     players.append(player)
    # players['url'] = a['href']