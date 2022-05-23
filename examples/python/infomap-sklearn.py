import networkx as nx
import numpy as np
from sklearn.model_selection import ParameterGrid

from infomap import Infomap

grid = ParameterGrid({"markov_time": np.linspace(0.8, 2, 5)})

im = Infomap(two_level=True, silent=True, num_trials=10)
im.add_networkx_graph(nx.karate_club_graph())

for params in grid:
    im.run(**params)
    print(
        f"markov_time={params['markov_time']:0.2f}: number of modules: {im.num_top_modules}"
    )
