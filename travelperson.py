import heapq
import networkx as nx
import numpy as np
import random

# Implementación de A* con Heurística de MST
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

# Implementación de A* usando MST
def a_star_mst(graph,start,goal):
    # Inicializar la cola de prioridad y el conjunto de nodos visitados
    open_set = [(0, start, [start])]
    visited = set()
    while open_set:
        # Expande el nodo con menor costo
        cost, current, path = heapq.heappop(open_set)
        if current == goal and len(path) == len(graph.nodes):  # Verifica si es una solución TSP completa
            return path, cost
        if current in visited:
            continue
        visited.add(current)
        # Expande los vecinos y calcula f(n) usando MST como heurística
        remaining_nodes = set(graph.nodes) - set(path)
        for neighbor in graph.neighbors(current):
            if neighbor not in path:
                new_cost = cost + graph[current][neighbor]['weight']
                f_cost = new_cost + mst_heuristic(graph, neighbor, remaining_nodes)
                heapq.heappush(open_set, (f_cost, neighbor, path + [neighbor]))
    return None, float('inf')
