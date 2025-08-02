import json
import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(json_file="output/results.json"):
    with open(json_file) as f:
        data = json.load(f)

    G = nx.DiGraph()
    for entry in data:
        src = entry['domain']
        dst = entry['url']
        G.add_edge(src, dst)

    nx.draw(G, with_labels=True, node_color='skyblue', font_size=8)
    plt.title("Linked Domains and Resources")
    plt.show()
