import time
import random
import networkx as nx
from mst import a_star_mst
from aco import a_star_aco
from combined import a_star_combined

# Crear un grafo TSP de ejemplo (grafo completo)
def create_graph(num_nodes):
    G = nx.complete_graph(num_nodes)
    for u, v in G.edges():
        G[u][v]['weight'] = random.randint(1, 10)  # Asignar pesos aleatorios
    return G

# Función para evaluar el desempeño
def evaluate_performance(graph, start, goal):
    # Evaluar A* con MST
    start_time = time.time()
    path_mst, cost_mst = a_star_mst(graph, start, goal)
    end_time = time.time()
    time_mst = end_time - start_time
    print(f"Tiempo A* con MST: {time_mst:.4f} segundos")
    print(f"Costo A* con MST: {cost_mst}")
    
    # Evaluar A* con ACO
    start_time = time.time()
    path_aco, cost_aco = a_star_aco(graph, start, goal)
    end_time = time.time()
    time_aco = end_time - start_time
    print(f"Tiempo A* con ACO: {time_aco:.4f} segundos")
    print(f"Costo A* con ACO: {cost_aco}")
    
    # Evaluar A* con ambas heurísticas (MST y ACO combinados)
    start_time = time.time()
    path_combined, cost_combined = a_star_combined(graph, start, goal)
    end_time = time.time()
    time_combined = end_time - start_time
    print(f"Tiempo A* con heurísticas combinadas (MST + ACO): {time_combined:.4f} segundos")
    print(f"Costo A* con heurísticas combinadas: {cost_combined}")

# Parámetros de entrada
num_nodes = 5  # Número de nodos en el grafo (puedes cambiarlo para experimentar con grafos más grandes)
graph = create_graph(num_nodes)
start_node = 0
goal_node = 0  # En el TSP, el objetivo es recorrer todos los nodos

# Evaluar el desempeño de los tres algoritmos
evaluate_performance(graph, start_node, goal_node)
