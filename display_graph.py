from typing import Dict, List

import matplotlib.pyplot as plt
import networkx as nx


def display_graphic_graph(adjacency_list: Dict[str, List[str]], sequence: List[int]):
    for vertex in adjacency_list:
        print(vertex, " -> ", adjacency_list[vertex])

    G = nx.to_networkx_graph(adjacency_list)
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.title(f'{sequence}')
    plt.show()

    # plt.savefig(f'{sequence}.png', bbox_inches='tight')
