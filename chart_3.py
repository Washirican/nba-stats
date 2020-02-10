# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-02-09
# --------------------------------------------------------------------------- #
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Arc, Polygon

color = 'gray'
lw = 1

fig = plt.figure()
ax = fig.add_subplot()

rect = Rectangle((0.2, 0.75), 0.4, 0.15, color='k', alpha=0.3)
circ = Circle((0.7, 0.2), 0.15, color='b', alpha=0.3)
pgon = Polygon([[0.15, 0.15], [0.35, 0.4], [0.2, 0.6]],
               color='g', alpha=0.5)

ax.add_patch(rect)
ax.add_patch(circ)
ax.add_patch(pgon)

hoop = Circle((0, 0), radius=7.5, linewidth=lw, color=color)

ax.add_patch(hoop)


plt.show()

