import heapq
import random
import networkx as nx
from aco import AntColony  
from mst import mst_heuristic  

def a_star_combined(graph, start, goal, w1=0.5, w2=0.5):
  # Inicializar la cola de prioridad y el conjunto de nodos visitados
    open_set = [(0, start, [start])]  # (f(n), nodo, camino)
    visited = set()
    
    # Ejecutar ACO para obtener la heurística ACO
    colony = AntColony(graph, n_ants=10, iterations=50)
    _, aco_heuristic_cost = colony.run()  # Obtiene el costo de la mejor ruta de ACO
    
    while open_set:
        cost, current, path = heapq.heappop(open_set)
        
        # Si hemos llegado al objetivo con todos los nodos visitados (solución TSP)
        if current == goal and len(path) == len(graph.nodes):
            return path, cost
        
        if current in visited:
            continue
        visited.add(current)
        
        remaining_nodes = set(graph.nodes) - set(path)
        
        # Calcula la heurística MST para el nodo actual
        mst_heuristic_cost = mst_heuristic(graph, current, remaining_nodes)
        
        # Combinamos ambas heurísticas con sus pesos
        combined_heuristic = w1 * mst_heuristic_cost + w2 * aco_heuristic_cost
        
        # Expande los vecinos del nodo actual
        for neighbor in graph.neighbors(current):
            if neighbor not in path:
                new_cost = cost + graph[current][neighbor]['weight']
                f_cost = new_cost + combined_heuristic  # f(n) = g(n) + h(n)
                heapq.heappush(open_set, (f_cost, neighbor, path + [neighbor]))
    
    return None, float('inf')  # Si no se encuentra una solución
