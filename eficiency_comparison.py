import time
import networkx as nx
import numpy as np
from a_star_aco import a_star_aco  
from a_star_mst import a_star_mst  
from generate_graphs import graph_generator  
import matplotlib.pyplot as plt

def compare_heuristics(graph, start, goal, iterations=10):
    # Variables para almacenar los resultados
    aco_times = []
    mst_times = []
    aco_costs = []
    mst_costs = []
    
    for _ in range(iterations):
        # Ejecutar A* con heurística ACO
        start_time = time.time()
        path_aco, cost_aco = a_star_aco(graph, start, goal)
        aco_times.append(time.time() - start_time)
        aco_costs.append(cost_aco)
        
        # Ejecutar A* con heurística MST
        start_time = time.time()
        path_mst, cost_mst = a_star_mst(graph, start, goal)
        mst_times.append(time.time() - start_time)
        mst_costs.append(cost_mst)
    
    # Promediar los resultados
    avg_aco_time = np.mean(aco_times)
    avg_mst_time = np.mean(mst_times)
    avg_aco_cost = np.mean(aco_costs)
    avg_mst_cost = np.mean(mst_costs)
    
    print(f"Promedio de tiempo de ejecución con ACO: {avg_aco_time:.5f} segundos")
    print(f"Promedio de tiempo de ejecución con MST: {avg_mst_time:.5f} segundos")
    print(f"Promedio del costo con ACO: {avg_aco_cost:.2f}")
    print(f"Promedio del costo con MST: {avg_mst_cost:.2f}")
    
    # Comparar el desempeño: ¿Qué heurística encontró la solución más barata?
    if avg_aco_cost < avg_mst_cost:
        print("ACO generó una mejor solución (costo menor).")
    else:
        print("MST generó una mejor solución (costo menor).")

    # Comparar el desempeño en cuanto a tiempo
    if avg_aco_time < avg_mst_time:
        print("ACO fue más rápido en promedio.")
    else:
        print("MST fue más rápido en promedio.")

# Función para generar grafos de diferentes tamaños y compararlos
def test_comparisons():
    for num_nodes in [5, 10, 15, 20]:  # Variar el tamaño del grafo
        graph = generate_random_graph(num_nodes, density=0.8)
        print(f"\nComparación de heurísticas para un grafo de {num_nodes} nodos:")
        compare_heuristics(graph, start=0, goal=num_nodes - 1, iterations=5)  # Realiza 5 iteraciones para obtener resultados más robustos

if __name__ == '__main__':
    test_comparisons()


def plot_comparison_results(aco_times, mst_times, aco_costs, mst_costs):
    # Graficar tiempos de ejecución
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.boxplot([aco_times, mst_times], labels=["ACO", "MST"])
    plt.title("Comparación de Tiempos de Ejecución")
    plt.ylabel("Tiempo (segundos)")
    
    # Graficar costos de la solución
    plt.subplot(1, 2, 2)
    plt.boxplot([aco_costs, mst_costs], labels=["ACO", "MST"])
    plt.title("Comparación de Costos de Solución")
    plt.ylabel("Costo de la Ruta")
    
    plt.tight_layout()
    plt.show()

# Luego puedes llamar a `plot_comparison_results` después de las comparaciones
