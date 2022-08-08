
def has_path(graph, src, dst):

    visited = set() 

    for node in graph[src]:
        if explore(graph, node, dst, visited) == True:
            return True 

    return False 

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

    

graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

# Driver code
# Test case 01 
if __name__ == "__main__":
    print(has_path(graph, 'f', 'k'))

# Test case 02
graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}
if __name__ == "__main__":
    print(has_path(graph, 'f', 'j')) # False

# Test case 03 
graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

print(has_path(graph, 'i', 'h')) # True

# Test case 04
graph = {
  'v': ['x', 'w'],
  'w': [],
  'x': [],
  'y': ['z'],
  'z': [],  
}

print(has_path(graph, 'v', 'w')) # True

# Test case 05
graph = {
  'v': ['x', 'w'],
  'w': [],
  'x': [],
  'y': ['z'],
  'z': [],  
}

print(has_path(graph, 'v', 'z')) # False