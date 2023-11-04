import Graph
from Graph import *
from collections import deque




class BFS:


    def __init__(self,graph):
        self.graph = graph
        self.vertices = {vertex : 0 for vertex in graph.vertex_iter()}
        self.count = 0

        for v in self.vertices:
            if self.vertices[v] == 0:
                print("hi")
                self.bfs(v)

    def bfs(self, v):
        self.count +=1
        self.vertices[v] = self.count
        q = deque()
        q.append(v)

        while len(q) > 0:
            for neighbor in self.graph.adjacent_vertex(q[0]):
                if self.vertices[neighbor] == 0:
                    self.count +=1
                    q.append(neighbor)
                    self.vertices[neighbor] = self.count
            q.popleft()

    def order(self):
        return self.vertices

