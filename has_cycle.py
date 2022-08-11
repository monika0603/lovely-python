
def has_cycle(graph):

    visited = set() 
    visiting = set() 

    for node in graph:
        if traverse(graph, node, visited, visiting) == True:
            return True 

    return False 

def traverse(graph, node, visited, visiting):

    if node in visited:
        return False 
    
    if node in visiting:
        return True 

    visiting.add(node) 

    for neighbor in graph[node]:
        if traverse(graph, neighbor, visited, visiting) == True:
            return True

    visiting.remove(node) 
    visited.add(node) 

    return False 

# Driver code 
# Test case 01
if __name__ == "__main__":
    print(has_cycle({
    "a": ["b"],
    "b": ["c"],
    "c": ["a"],
    })) # -> True

    # Test case 02 
    print(has_cycle({
    "a": ["b", "c"],
    "b": ["c"],
    "c": ["d"],
    "d": [],
    })) # -> False

    # Test case 03 
    print(has_cycle({
    "a": ["b", "c"],
    "b": [],
    "c": [],
    "e": ["f"],
    "f": ["e"],
    })) # -> True

    # Test case 04 
    print(has_cycle({
    "q": ["r", "s"],
    "r": ["t", "u"],
    "s": [],
    "t": [],
    "u": [],
    "v": ["w"],
    "w": [],
    "x": ["w"],
    })) # -> False

    # Test case 05
    print(has_cycle({
    "a": ["b"],
    "b": ["c"],
    "c": ["a"],
    "g": [],
    })) # -> True