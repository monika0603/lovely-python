""" 
Algorithm:

1. Create an adjacency list based on the number of cities variable provided. 
2. Check if the grapg created is bipartite or not. 
"""

import collections 
def rare_routing(no_of_cities, edges):
    graph = build_graph(no_of_cities, edges) 

    coloring = {} 
    for node in graph:
        if node not in coloring and validate(graph, node, coloring, False) == False:
            return False 

    return True 

def validate(graph, node, coloring, current_color):
    if node in coloring:
        return current_color == coloring[node] 

    coloring[node] = current_color 

    for neighbor in graph[node]:
        if validate(graph, neighbor, coloring, not current_color) == False:
            return False 

    return True 

def build_graph(no_of_cities, edges):

    graph = collections.defaultdict(list) 

    for i in range(no_of_cities):
        graph[i] = [] 

    for x,y in edges:
        graph[x].append(y) 
        graph[y].append(x) 

    return graph 

if __name__ == "__main__":
    print(rare_routing(4, [
    (0, 1),
    (0, 2),
    (0, 3)
    ])) # -> True

    # Test case 01
    print(rare_routing(4, [
    (0, 1),
    (0, 2),
    (0, 3),
    (3, 2)
    ])) # -> False 

    # Test case 02 
    print(rare_routing(6, [
    (1, 2),
    (5, 4),
    (3, 0),
    (0, 1),
    (0, 4),
    ])) # -> True

    # Test case 03 
    print(rare_routing(6, [
    (1, 2),
    (4, 1),
    (5, 4),
    (3, 0),
    (0, 1),
    (0, 4),
    ])) # -> False

    # Test case 04
    print(rare_routing(4, [
    (0, 1),
    (3, 2),
    ])) # -> False
