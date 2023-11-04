#This is a graph class to implement graph algorithms

import itertools
import Topsort_dfs
from bfs import BFS
import K_Clique


class Graph:

	def __init__(self, vertices, directed=False):
		self.vertices = str(vertices).split()
		self.directed = directed
		self.graph = {v:{} for v in self.vertices}

	def add_edge(self, vertex1, vertex2, weight=1):

		self.graph[vertex1][vertex2] = weight

		if not self.directed:
			self.graph[vertex2][vertex1] = weight


	def has_edge(self, v1, v2):
		"returns a Boolean indicating v2 is adjacent to v1"

		return self.graph[v1].has_key(v2)

	def weight(self, v1, v2):
		"returns the weight of edge from v2 to v1"

		return self.graph[v1][v2]

	def vertex_iter(self):
		"returns an iterator for vertices"
		for v in self.graph:
			yield v

	def edge_iter(self):
		"returns an iterator for edges"
		for v1 in self.graph:
			for v2 in self.graph[v1]:
				w = self.weight(v1,v2)
				yield v1, v2, w

	def adjacent(self, v):
		"returns adjacency list for v as a dictionary"
		return self.graph[v]

	def adjacent_vertex(self, v):
		return tuple(self.graph[v].keys())

	def is_directed(self):
		return self.directed

def fromfile(filename):
	with open(filename) as infile:
		direction = infile.readline().strip()
		if direction == 'undirected':
			direction = False

		vertices = infile.readline().strip()
		graph = Graph(vertices, direction)

		edges = []
		for line in infile:
			edges = line.split()
			if len(edges) == 3:
				graph.add_edge(edges[0], edges[1], edges[2])
			elif len(edges) == 2:
				graph.add_edge(edges[0], edges[1])
			else:
				pass

		return graph

def main():


	fname = input("file: ")
	graph = fromfile(fname)

	lst = []

	#for vertex in graph.vertex_iter():
		#print(vertex, ':', graph.adjacent_vertex(vertex))



	#order = Topsort_dfs.topsort(graph)
	#print(order)


	bfs = BFS(graph)
	#order2 = BFS.bfs(graph).order()
	order2 = bfs.order()
	print(order2)

	'''k_clique = K_Clique.k_clique(graph, 5)
	print(k_clique)'''

if __name__ == "__main__":
    main()