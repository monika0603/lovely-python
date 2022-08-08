def has_path(graph, src, dst):

    if src == dst:
        return True 
    
    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst) == True:
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