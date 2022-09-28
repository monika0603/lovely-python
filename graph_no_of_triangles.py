""" 
Problem: Find the number of triangles in the edges list below. 
"""
import collections 
def number_of_triangles(edges):

    graph = build_graph(edges) 
    visited = set() 

    max_size = float("-inf")
    for node in graph:
        size = explore(graph, node, visited)
        max_size = max(max_size, size) 

    return max_size 

def explore(graph, node, visited):
    if node in visited:
        return 0 

    visited.add(node) 

    size = 1
    for neighbor in graph[node]:
        size += explore(graph, neighbor, visited)

    return size 

def build_graph(edges):

    graph = collections.defaultdict(list)

    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x) 

    return graph 


edges = [[0,1], [3,0], [0,2], [3,2], [1,2], [4,0], [3,4], [3,5], [4,5], [1,5], [1,3]]
print(number_of_triangles(edges))