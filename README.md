## Juan Manuel Agudelo Aguirre - Inteligencia Artificial - 06 - 11 - 2024 
# Resolución del Problema del Viajante de Comercio (TSP) con Heurísticas de A* Basadas en Árbol de Expansión Mínima (MST) y Colonia de Hormigas (ACO)
Este proyecto aborda la resolución del Problema del Viajante de Comercio (TSP) utilizando el algoritmo A* con dos heurísticas diferentes: Árbol de Expansión Mínima (MST) y Colonia de Hormigas (ACO). El objetivo es evaluar y comparar el rendimiento de estas dos heurísticas para resolver el TSP, en términos de calidad de la solución (costo de la ruta) y tiempo de ejecución.

## Descripción
El Problema del Viajante de Comercio (TSP) consiste en encontrar la ruta más corta que pase por un conjunto de ciudades, visitando cada ciudad una sola vez y regresando al punto de inicio. Este es un problema NP-hard, lo que significa que no existe una solución eficiente en tiempo polinomial para instancias grandes.

En este proyecto, utilizamos el algoritmo A*, que es un algoritmo de búsqueda informada, combinando dos heurísticas para mejorar la eficiencia en la búsqueda:

1. **Heurística MST (Árbol de Expansión Mínima)**: Utiliza el peso de un árbol de expansión mínima sobre los nodos restantes como una estimación del costo mínimo para completar el recorrido. Esta heurística es admisible y consistente.

2. **Heurística ACO (Colonia de Hormigas):** Emula el comportamiento de una colonia de hormigas para explorar el espacio de soluciones de manera estocástica. Utiliza un proceso iterativo para encontrar soluciones aproximadas, basándose en la actualización de feromonas.

La comparación de ambas heurísticas se realiza en términos de:

- Tiempo de ejecución: Cuánto tarda cada algoritmo en encontrar una solución.
- Calidad de la solución: Qué tan cerca se encuentra la solución de cada algoritmo del valor óptimo.

## Funcionalidades
- Generación de grafos aleatorios con diferentes tamaños y características (densidad, pesos, etc.).
- Implementación de A* con la heurística MST**: A* utiliza el árbol de expansión mínima para estimar el costo restante.
- Implementación de A* con la heurística ACO: A* utiliza el costo de la mejor ruta encontrada por la colonia de hormigas como una heurística para guiar la búsqueda.
- Evaluación del desempeño de las heurísticas en función de:
  - Tiempo de ejecución
  - Calidad de la solución
- Generación de resultados y comparación: Se comparan los resultados de las dos heurísticas en términos de tiempo y calidad de las soluciones.

## Archivos 
- **graph_generator.py:** Función para generar grafos aleatorios de diferentes tamaños.
- **mst.py:** Implementación de la heurística de Árbol de Expansión Mínima (MST) y su uso en A*.
- **aco.py:** Implementación de la heurística de Colonia de Hormigas (ACO) y su uso en A*.
- **a_star_combined.py:** Implementación de A* utilizando las heurísticas combinadas (MST + ACO).
- **eficiency_comparison.py:**Código para realizar la comparación entre las heurísticas, midiendo tiempo de ejecución y calidad de la solución.
- **main.py:** Archivo principal que crea el grafo, llama a los algoritmos A*, y evalúa su desempeño (tiempo de ejecución y calidad de la solución).

## Requisitos
Para ejecutar este proyecto, necesitarás tener instalados los siguientes paquetes en Python:

`networkx:` para manipulación de grafos y cálculo de árboles de expansión mínima.
`numpy:` para manipulación de matrices y cálculos numéricos.
`heapq:` para la implementación de colas de prioridad en A*.
`random:` para la simulación de comportamiento estocástico en ACO.
`matplotlib` (opcional): para visualización de resultados.
Instala las dependencias con:

```
pip install networkx numpy matplotlib
```
## Ejecución
Para ejecutar el proyecto y realizar comparaciones entre las heurísticas, simplemente ejecuta el script principal test_comparisons.py, que genera grafos aleatorios y ejecuta los algoritmos A* con las heurísticas MST y ACO:
```
python eficiency_comparison.py
```
Esto ejecutará una serie de pruebas y mostrará los resultados de comparación entre las dos heurísticas.

## Resultados Esperados
Los resultados esperados incluyen la evaluación del desempeño de las dos heurísticas en términos de:

- **Tiempo de ejecución:** Se espera que ACO sea más lento debido a su naturaleza estocástica, mientras que MST podría ser más rápido dado que calcula un árbol de expansión mínima.
- **Calidad de la solución:** ACO puede encontrar soluciones más cercanas al óptimo, pero depende de la configuración de parámetros, mientras que MST proporciona una solución bastante competitiva debido a su estructura de mínimo costo.
