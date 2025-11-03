from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    traversal_order = []

    # TODO: finish BFS

    return traversal_order


def dfs(graph, start_node):
    visited = set()
    stack = [start_node]
    traversal_order = []

    # TODO: Finish DFS

    return traversal_order

# Example usage and visualization
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs_order = bfs(graph, 'A')
print(f"BFS Traversal Order: {bfs_order}")

dfs_order = dfs(graph, 'A')
print(f"DFS Traversal Order: {dfs_order}")

# Visualization
G = nx.Graph(graph)
pos = nx.spring_layout(G) # Layout for visualization

plt.figure(figsize=(8, 6))
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=700)
nx.draw_networkx_edges(G, pos, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
plt.title("Graph for BFS Visualization")
plt.show()
