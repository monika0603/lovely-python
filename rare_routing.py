""" 
Write a function, rare_routing, that takes in a number of cities (n) and a list of tuples where 
each tuple represents a direct road that connects a pair of cities. The function should return 
a boolean indicating whether or not there exists a unique route for every pair of cities. A route 
is a sequence of roads that does not visit a city more than once.

Cities will be numbered 0 to n - 1.

You can assume that all roads are two-way roads. This means if there is a road between A and B, 
then you can use that road to go from A to B or go from B to A.
"""
import collections 
def rare_routing(cities, edges):

    graph = build_graph(cities, edges)
    coloring = {} 

    for node in graph:
        if node not in coloring:
            if _rare_routing(graph, node, coloring, False) == False:
                return False 

    return True 

def _rare_routing(graph, node, coloring, current_color):
    if node in coloring:
        return coloring[node] == current_color 

    coloring[node] = current_color 

    for neighbor in graph[node]:
        if _rare_routing(graph, neighbor, coloring, not current_color) == False:
            return False 
    return True 

def build_graph(cities, edges):

    graph = collections.defaultdict(list)

    for city in range(cities):
        graph[city] = [] 

    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x) 

    return graph 


if __name__ == "__main__":
    print(rare_routing(4, [
    (0, 1),
    (0, 2),
    (0, 3)
    ])) # -> True

    # Test case 02
    print(rare_routing(4, [
    (0, 1),
    (0, 2),
    (0, 3),
    (3, 2)
    ])) # -> False

    # Test case 03
    print(rare_routing(6, [
    (1, 2),
    (5, 4),
    (3, 0),
    (0, 1),
    (0, 4),
    ])) # -> True

    # Test case 04
    print(rare_routing(6, [
    (1, 2),
    (4, 1),
    (5, 4),
    (3, 0),
    (0, 1),
    (0, 4),
    ])) # -> False

    # Test case 05
    print(rare_routing(4, [
    (0, 1),
    (3, 2),
    ])) # -> False