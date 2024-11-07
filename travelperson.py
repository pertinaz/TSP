import heapq
import networkx as nx
import numpy as np
import random


def mst_heuristic(graph, current_node, remaining_nodes):
    if not remaining_nodes:
        return 0  # No quedan nodos, no necesita conectar más

    # Construye el subgrafo con los nodos restantes
    subgraph = graph.subgraph(remaining_nodes)

    # Calcula el MST para el subgrafo
    mst = nx.minimum_spanning_tree(subgraph)

    # Calcula el peso total del MST
    mst_weight = mst.size(weight='weight')

    # Encuentra el costo mínimo desde el nodo actual al subgrafo (cualquier nodo en remaining_nodes)
    min_cost_to_mst = min(graph[current_node][node]['weight'] for node in remaining_nodes)

    # Retorna la heurística como el costo mínimo hacia el MST + peso del MST
    return min_cost_to_mst + mst_weight

