# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-02-08
# --------------------------------------------------------------------------- #

# Using requests package

import requests
import matplotlib.pyplot as plt
import numpy as np

bron_id = 2544
LAL_id = 1610612747

im = plt.imread('shotchart-blue.png')
# implot = plt.imshow(im, extent=[0, 400, 0, 900])

fig, ax = plt.subplots()
x = range(300)
ax.imshow(im, extent=[0, 400, 0, 300])
ax.plot(x, x, '--', linewidth=5, color='firebrick')
plt.show()