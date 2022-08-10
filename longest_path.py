
def longest_path(graph):

    distance = {} 

    # Find a terminal node first 
    for node in graph:
        if len(graph[node]) == 0:
            distance[node] = 0 

    for node in graph:
        traverse(graph, node, distance) 

    return max(distance.values()) 

def traverse(graph, node, distance):
    # Base case if I have already visited a node and already stored it's distance 
    # Then simply return the distance
    if node in distance:
        return distance[node] 

    longest = 0 
    for neighbor in graph[node]:
        attempt = traverse(graph, neighbor, distance)
        longest = max(attempt, longest) 

    # [Important]: The reason we add 1 here is because longest contains the distance from 
    # the neighbor instead of the current node!
    distance[node] = 1 + longest 
    return distance[node] 

# Driver code 
# Test case 01
if __name__ == "__main__":
    graph = {
    'a': ['c', 'b'],
    'b': ['c'],
    'c': []
    }

    """ 
    a -- > c
    |    /
    |  /
    b 
    So 'c' is the only terminal node. Whereas a and b are not
    """
    print(longest_path(graph)) # -> 2 

# Test case 02
    graph = {
    'a': ['c', 'b'],
    'b': ['c'],
    'c': [],
    'q': ['r'],
    'r': ['s', 'u', 't'],
    's': ['t'],
    't': ['u'],
    'u': []
    }

    print(longest_path(graph)) # -> 4 

# Test case 03 
    graph = {
    'h': ['i', 'j', 'k'],
    'g': ['h'],
    'i': [],
    'j': [],
    'k': [],
    'x': ['y'],
    'y': []
    }

    print(longest_path(graph)) # -> 2

# Test case 04
    graph = {
    'a': ['b'],
    'b': ['c'],
    'c': [],
    'e': ['f'],
    'f': ['g'],
    'g': ['h'],
    'h': []
    }

    print(longest_path(graph)) # -> 3