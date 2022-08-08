
import collections 

def undirected_path(edges, src, dst):

    graph = build_graph(edges) 
    
    visited = set()
    return explore(graph, src, dst, visited)

def explore(graph, node, dst, visited):
    if node in visited:
        return False 

    visited.add(node) 

    if node == dst:
        return True 

    for neighbor in graph[node]:
        if explore(graph, neighbor, dst, visited) == True:
            return True 

    return False 

def build_graph(edges):
    graph = collections.defaultdict(list)

    for x, y in edges:
        graph[x].append(y) 
        graph[y].append(x)

    return graph


edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

# Driver code 
# Test case 01
print(undirected_path(edges, 'j', 'm')) # -> True

# Test case 02 
edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

print(undirected_path(edges, 'm', 'j')) # -> True

# Test case 03
edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

print(undirected_path(edges, 'l', 'j')) # -> True

# Test case 04
edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

print(undirected_path(edges, 'k', 'o')) # -> False

# Test case 05
edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

print(undirected_path(edges, 'i', 'o')) # -> False

# Test case 06
edges = [
  ('b', 'a'),
  ('c', 'a'),
  ('b', 'c'),
  ('q', 'r'),
  ('q', 's'),
  ('q', 'u'),
  ('q', 't'),
]

print(undirected_path(edges, 'a', 'b')) # -> True

# Test case 07
edges = [
  ('b', 'a'),
  ('c', 'a'),
  ('b', 'c'),
  ('q', 'r'),
  ('q', 's'),
  ('q', 'u'),
  ('q', 't'),
]

print(undirected_path(edges, 'a', 'c')) # -> True

# Test case 08
edges = [
  ('b', 'a'),
  ('c', 'a'),
  ('b', 'c'),
  ('q', 'r'),
  ('q', 's'),
  ('q', 'u'),
  ('q', 't'),
]

print(undirected_path(edges, 'r', 't')) # -> True

# Test case 09
edges = [
  ('b', 'a'),
  ('c', 'a'),
  ('b', 'c'),
  ('q', 'r'),
  ('q', 's'),
  ('q', 'u'),
  ('q', 't'),
]

print(undirected_path(edges, 'r', 'b')) # -> False

# Test case 10 
edges = [
  ('s', 'r'),
  ('t', 'q'),
  ('q', 'r'),
]

print(undirected_path(edges, 'r', 't')) # -> True