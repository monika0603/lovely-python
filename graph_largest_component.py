
def largest_component(graph):

    visited = set() 
    max_component = 0
    output = []

    for node in graph:
        size = explore(graph, node, visited)
        max_component = max(max_component, size) 
        output.append(size)

    return max_component, output

def explore(graph, node, visited):
    if node in visited:
        return 0 

    visited.add(node) 

    size = 1 
    for neighbor in graph[node]:
        size += explore(graph, neighbor, visited) 

    return size 

# Driver code 
# Test case 01 
if __name__ == "__main__":
    print(largest_component({
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
    })) # -> 4

# Test case 02
    print(largest_component({
    1: [2],
    2: [1,8],
    6: [7],
    9: [8],
    7: [6, 8],
    8: [9, 7, 2]
    })) # -> 6

# Test case 03
    print(largest_component({
    3: [],
    4: [6],
    6: [4, 5, 7, 8],
    8: [6],
    7: [6],
    5: [6],
    1: [2],
    2: [1]
    })) # -> 5

# Test case 04 
    print(largest_component({})) # -> 0

# Test case 05
    print(largest_component({
    0: [4,7],
    1: [],
    2: [],
    3: [6],
    4: [0],
    6: [3],
    7: [0],
    8: []
    })) # -> 3