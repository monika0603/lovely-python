""" 
For questions like these it is important to be able to track the last node that I was on. I don't want to 
travel between 0 -- > 1 and immediately travel back to 0 from 1. 
"""

import collections 
def rare_routing(no_of_cities, edges):
    graph = build_graph(no_of_cities, edges) 

    visited = set() 
    # Starting the traversal at the zeroth city always!
    # So you don't need a for loop here to iterate over all the nodes in a graph 
    # Basically you are able to visit all part of the graph by starting from the zeroth city
    valid = validate(graph, 0, visited, None)
    return valid and len(visited) == no_of_cities
    

def validate(graph, node, visited, last_node):
    if node in visited:
        return False 

    visited.add(node)

    for neighbor in graph[node]:
        if neighbor != last_node and validate(graph, neighbor, visited, node) == False:
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