from Graph import *


def k_clique(graph, k):
    #combines all of the veertices into a srting
    vertices_str = ""
    for item in graph.vertex_iter():
        vertices_str += item
        print(vertices_str)

    k_clique_lst = []
    for comb in itertools.combinations(vertices_str, k):
        clique = True
        for i in range(k):
            if not clique:
                break
            for j in range(i + 1, k):
                if graph.has_edge(comb[i], comb[j]) and graph.has_edge(comb[j], comb[i]):
                    continue
                else:
                    clique = False
                    break
        if clique:
            k_clique_lst.append(comb)

    return k_clique_lst