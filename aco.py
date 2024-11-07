import heapq
import networkx as nx
import numpy as np
import random

class AntColony:
    def __init__(self, graph, n_ants, alpha=1, beta=5, evaporation_rate=0.5, iterations=100):
        self.graph = graph
        self.n_ants = n_ants
        self.alpha = alpha
        self.beta = beta
        self.evaporation_rate = evaporation_rate
        self.iterations = iterations
        self.pheromones = {edge: 1 for edge in graph.edges}  # Inicializa las feromonas
    
    def run(self):
        best_route = None
        best_cost = float('inf')
        
        for _ in range(self.iterations):
            all_routes = self.construct_routes()
            self.update_pheromones(all_routes)
            # Encuentra la mejor ruta
            for route, cost in all_routes:
                if cost < best_cost:
                    best_cost = cost
                    best_route = route
        return best_route, best_cost
    
    def construct_routes(self):
        routes = []
        for _ in range(self.n_ants):
            route = [random.choice(list(self.graph.nodes))]  # Selecciona un nodo inicial al azar
            while len(route) < len(self.graph.nodes):
                current_node = route[-1]
                probabilities = self.calculate_transition_probabilities(current_node, route)
                next_node = self.select_next_node(probabilities)
                route.append(next_node)
            cost = sum(self.graph[route[i]][route[i+1]]['weight'] for i in range(len(route) - 1))
            routes.append((route, cost))
        return routes
    
    def calculate_transition_probabilities(self, current, visited):
        probabilities = {}
        for neighbor in self.graph.neighbors(current):
            if neighbor not in visited:
                pheromone = self.pheromones[(current, neighbor)]
                weight = self.graph[current][neighbor]['weight']
                probabilities[neighbor] = (pheromone * self.alpha) * ((1.0 / weight) * self.beta)
        return probabilities
    
    def select_next_node(self, probabilities):
        total = sum(probabilities.values())
        threshold = random.uniform(0, total)
        cumulative = 0
        for node, prob in probabilities.items():
            cumulative += prob
            if cumulative >= threshold:
                return node
        return list(probabilities.keys())[0]
    
    def update_pheromones(self, routes):
        for edge in self.pheromones:
            self.pheromones[edge] *= (1 - self.evaporation_rate)
        for route, cost in routes:
            for i in range(len(route) - 1):
                self.pheromones[(route[i], route[i+1])] += 1.0 / cost
