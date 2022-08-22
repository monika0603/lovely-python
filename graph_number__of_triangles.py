""" 
Problem: Find the number of triangles in the edges list below. 
"""

import collections 
def number_of_triangles(edges):

    graph = build_graph(edges) 

    count = 0 

    for x, y in edges:
        for node in graph:
            if x in graph[node] and y in graph[node]:
                count += 1 

    return count//3

def build_graph(edges):

    graph = collections.defaultdict(list)

    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x) 

    return graph 


edges = [[0,1], [3,0], [0,2], [3,2], [1,2], [4,0], [3,4], [3,5], [4,5], [1,5], [1,3]]
print(number_of_triangles(edges))