# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-04-17
# --------------------------------------------------------------------------- #

# TODO D. Rodriguez 2020-04-17: Get box score data for a given game

import requests


def get_box_score():
    # request_url = 'https://stats.nba.com/game/0021900973/'
    request_url = 'https://stats.nba.com/stats/boxscoresummaryv2?GameID=0021900973'
    return requests.get(request_url)


if __name__ == '__main__':
    print('NBA Box Score')
    box_score_data = get_box_score()
    print(box_score_data)
