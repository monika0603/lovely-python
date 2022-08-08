
def connected_components_count(graph):

    visited = set()
    count = 0 

    for node in graph:
        if explore(graph, node, visited) == True:
            count += 1 

    return count 

def explore(graph, node, visited):
    if node in visited:
        return False 

    visited.add(node) 

    for neighbor in graph[node]:
        explore(graph, neighbor, visited) 

    # If I get to this return statement of True then I have finished exploring all the 
    # components of the current node which I had not visited previously. 
    # This is when I want to increment my counter of connected component     
    return True  

# Driver code
# Test case 01
print(connected_components_count({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
})) # -> 2

# Test case 02
print(connected_components_count({
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
})) # -> 1

# Test case 03
print(connected_components_count({
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1]
})) # -> 3

# Test case 04
print(connected_components_count({})) # -> 0 

# Test case 05
print(connected_components_count({
  0: [4,7],
  1: [],
  2: [],
  3: [6],
  4: [0],
  6: [3],
  7: [0],
  8: []
})) # -> 5
