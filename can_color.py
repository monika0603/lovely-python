""" 
Write a function, can_color, that takes in a dictionary representing the adjacency list of an 
undirected graph. The function should return a boolean indicating whether or not it is possible 
to color nodes of the graph using two colors in such a way that adjacent nodes are always 
different colors.
"""

def can_color(graph):
    coloring = {}
    for node in graph:
        if node not in coloring:
            if _can_color(graph, node, coloring, False) == False:
                return False 

    return True 

def _can_color(graph, node, coloring, current_color):
    # Base case: if the node that I am at, is already colored then I want to 
    # make sure that the color assigned matches with the current_color passed
    if node in coloring:
        return current_color == coloring[node] 

    # Otherwise the node has not been colored and we want to color it. 
    # So assining the color passed
    coloring[node] = current_color
    
    for neighbor in graph[node]:
        if _can_color(graph, neighbor, coloring, not current_color) == False:
            return False  

    return True 

# Driver code 
if __name__ == "__main__":
    print(can_color({
    "x": ["y"],
    "y": ["x","z"],
    "z": ["y"]
    })) # -> True

    # Test case 02
    print(can_color({
    "a": ["b", "c", "d"],
    "b": ["a"],
    "c": ["a"],
    "d": ["a"],
    })) # -> True

    # Test case 03
    print(can_color({
    "h": ["i", "k"],
    "i": ["h", "j"],
    "j": ["i", "k"],
    "k": ["h", "j"],
    })) # -> True

    # Test case 04
    print(can_color({
    "z": []
    })) # -> True

    # Test case 05
    print(can_color({
    "a": ["b", "c", "d"],
    "b": ["a"],
    "c": ["a", "d"],
    "d": ["a", "c"],
    })) # -> False

    # Test case 06
    print(can_color({
    "h": ["i", "k"],
    "i": ["h", "j"],
    "j": ["i", "k"],
    "k": ["h", "j"],
    "q": ["r", "s"],
    "r": ["q", "s"],
    "s": ["r", "q"]
    })) # -> False


