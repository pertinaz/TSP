import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt

def generate_random_graph(num_nodes, density=1.0, max_weight=10):
    """
    Genera un grafo aleatorio de TSP con una cantidad de nodos `num_nodes` y una densidad de conexiones `density`.
    
    :param num_nodes: Número de nodos en el grafo (puedes variar este valor).
    :param density: La densidad de las conexiones (0.0 = sin conexiones, 1.0 = grafo completo).
    :param max_weight: El valor máximo para los pesos de las aristas.
    :return: Un grafo de NetworkX con los nodos y pesos asignados.
    """
    G = nx.Graph()
    G.add_nodes_from(range(num_nodes))  # Añadir los nodos
    
    # Determinar el número de aristas a agregar según la densidad
    num_edges = int(density * num_nodes * (num_nodes - 1) / 2)
    
    edges_added = 0
    while edges_added < num_edges:
        node1, node2 = random.sample(range(num_nodes), 2)
        
        # Asegurarse de que no haya una arista duplicada
        if not G.has_edge(node1, node2):
            weight = random.randint(1, max_weight)  # Asignar peso aleatorio
            G.add_edge(node1, node2, weight=weight)
            edges_added += 1
    
    return G

def generate_euclidean_graph(num_nodes, max_coord=10, max_weight=10):
    """
    Genera un grafo aleatorio basado en coordenadas Euclidianas (para el TSP Euclidiano).
    
    :param num_nodes: Número de nodos en el grafo.
    :param max_coord: El valor máximo para las coordenadas de los nodos (espacio 2D).
    :param max_weight: El valor máximo para los pesos de las aristas (en función de la distancia euclidiana).
    :return: Un grafo de NetworkX con pesos calculados usando distancias euclidianas.
    """
    G = nx.Graph()
    coords = np.random.randint(0, max_coord, size=(num_nodes, 2))  # Generar coordenadas aleatorias en 2D
    
    # Añadir los nodos
    for i in range(num_nodes):
        G.add_node(i, pos=coords[i])

    # Calcular la distancia euclidiana entre todos los pares de nodos
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            x1, y1 = coords[i]
            x2, y2 = coords[j]
            dist = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)  # Distancia Euclidiana
            weight = int(dist)  # Puedes ajustar esto para ser más preciso
            G.add_edge(i, j, weight=weight)
    
    return G

# Visualización del grafo (opcional, para ver cómo se ve el grafo generado)
def plot_graph(G):
    pos = nx.spring_layout(G)  # Determina la disposición de los nodos
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=15, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

# Ejemplo de uso
if __name__ == '__main__':
    num_nodes = 10  # Cambia el número de nodos para probar diferentes tamaños
    graph = generate_random_graph(num_nodes, density=0.8, max_weight=10)  # Grafo aleatorio
    plot_graph(graph)  # Visualiza el grafo generado
    
    # Para generar un grafo basado en coordenadas euclidianas
    euclidean_graph = generate_euclidean_graph(num_nodes, max_coord=10, max_weight=10)
    plot_graph(euclidean_graph)
