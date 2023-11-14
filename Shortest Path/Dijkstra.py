import networkx as nx
import matplotlib.pyplot as plt
import heapq


class Graph:
    def __int__(self, g):
        self.g = g

    def dijkstra(self, start):
        # Initialize distances and predecessors
        distances = {node: float('infinity') for node in self.g}
        distances[start] = 0
        predecessors = {node: None for node in self.g}

        # Priority queue to keep track of the next node to visit
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            # Check if the current path is shorter than the stored distance
            if current_distance > distances[current_node]:
                continue

            for neighbor, weights in self.g[current_node].items():
                distance = current_distance + weights

                # Update the distance and predecessor if a shorter path is found
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances, predecessors

    def reconstruct_path(self, start, end):
        _, predecessors = self.dijkstra(start)

        path = []
        current_node = end

        while current_node is not None:
            path.insert(0, current_node)
            current_node = predecessors[current_node]

        return path

    def plot_graph(self):
        graph_to_plot = nx.Graph()
        for node, neighbors in self.g.items():
            for neighbor, weight in neighbors.items():
                graph_to_plot.add_edge(node, neighbor, weight=weight)

        pos = nx.spring_layout(graph_to_plot)
        labels = nx.get_edge_attributes(graph_to_plot, 'weight')
        nx.draw(graph_to_plot, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, font_color='black')
        # nx.draw(g_draw, with_labels=True)
        nx.draw_networkx_edge_labels(graph_to_plot, pos, edge_labels=labels)
        plt.show()


if __name__ == '__main__':
    graph_example = Graph()
    graph_example.g = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'D': 2, 'E': 5},
        'C': {'A': 4, 'F': 3, 'G': 7},
        'D': {'B': 2},
        'E': {'B': 5, 'H': 6},
        'F': {'C': 3},
        'G': {'C': 7},
        'H': {'E': 6}
    }
    start_node = 'H'
    end_node = 'D'

    distances, _ = graph_example.dijkstra(start_node)
    shortest_path = graph_example.reconstruct_path(start_node, end_node)

    print(f"Shortest distances from {start_node}: {distances}")
    print(f"Shortest path from {start_node} to {end_node}: {shortest_path}")
    graph_example.plot_graph()