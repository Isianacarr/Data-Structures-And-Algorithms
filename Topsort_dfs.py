from Graph import *

def dfs(graph, vertex, stack, visited):
    visited.append(vertex)
    neighbors = graph.adjacent_vertex(vertex)
    for neighbor in neighbors:
        if neighbor not in visited:
            dfs(graph, neighbor, stack, visited)
    stack.append(vertex)

def topsort(graph):
    stack = []
    visited = []

    if graph.is_directed():
        for vertex in graph.vertex_iter():
            if vertex not in visited:
                dfs(graph, vertex, stack, visited)
    else:
        -1

    order = []
    while stack:
        order.append(stack.pop())

    return order
