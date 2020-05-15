# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-14
# --------------------------------------------------------------------------- #

from players import Players
from teams import Teams

# TODO (D. Rodriguez 2020-05-14): Fix code sequence.


sc30 = Players('Curry', 'Stephen')

lbj = Players('James', 'LeBron')

pg13 = Players('George', 'Paul')

mj = Players('Jordan', 'Michael')

td = Players('Duncan', 'Tim')

sc30_current_team = Teams(sc30.current_team_id)

sc30.get_player_per_season_totals()
sc30.get_player_seasons_played()

