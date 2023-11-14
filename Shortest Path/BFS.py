from collections import defaultdict, deque
import networkx as nx
import matplotlib.pyplot as plt


class Graph:
	def __int__(self, g):
		self.g = g

	def bfs_shortest_path(self, start, end):
		queue = deque([(start, [start])])  # Initialize the queue with the starting node and its path
		while queue:
			current_node, path = queue.popleft()
			for neighbor in self.g[current_node]:
				if neighbor == end:
					return path + [neighbor]  # Return the path if the destination is reached
				if neighbor not in path:
					queue.append((neighbor, path + [neighbor]))
		return None  # Return None if no path is found

	def plot_graph(self):
		g_draw = nx.Graph(self.g)
		nx.draw(g_draw, with_labels=True)
		plt.show()


# Driver code
if __name__ == '__main__':
	graph_example = Graph()
	graph_example.g = {
		'A': ['B', 'C'],
		'B': ['A', 'D', 'E'],
		'C': ['A', 'F', 'G'],
		'D': ['B'],
		'E': ['B', 'H'],
		'F': ['C'],
		'G': ['C', 'H'],
		'H': ['E', 'G']
	}
	start_node = 'H'
	end_node = 'D'

	# graph_example = Graph(g)
	shortest_path = graph_example.bfs_shortest_path(start_node, end_node)
	if shortest_path:
		print(f"Shortest path from {start_node} to {end_node}: {shortest_path}")
	else:
		print(f"No path from {start_node} to {end_node}")
	graph_example.plot_graph()
