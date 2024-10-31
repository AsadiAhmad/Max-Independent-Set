import networkx as nx
import matplotlib.pyplot as plt

# Create graph
graph = nx.Graph()
A, B, C, D, E, F, G = 'A', 'B', 'C', 'D', 'E', 'F', 'G'
graph.add_nodes_from([A, B, C, D, E, F, G])
graph.add_edges_from([(A, B), (B, C), (C, D), (D, E), (E, F), (F, A), (A, G)])
graph_copy = graph.copy()

def maxIndependentSetGraph(Graph):
    IndependentSet = []
    while Graph.number_of_nodes() != 0:
        min_degree_node = min(graph.degree, key=lambda x: x[1])
        IndependentSet.append(min_degree_node[0])
        adjacent_nodes = list(Graph.neighbors(min_degree_node[0]))
        graph.remove_node(min_degree_node[0])
        for node in adjacent_nodes:
            Graph.remove_node(node)
    return IndependentSet

print(maxIndependentSetGraph(graph))
# Draw the graph
nx.draw(graph_copy, with_labels=True, node_color="skyblue", font_weight="bold")
plt.show()
