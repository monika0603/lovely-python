""" 
Algorithm:

1. Define a dictionary called coloring which will keep track of the color of each node. 
2. If a given node is in coloring, then check if the color matches with the previously assign node. 
3. Anytime I find above condition to not be true, return False. 
4. Else return True 
"""

def can_color(graph):
    coloring = {} 

    for node in graph:
        if node not in coloring and validate(graph, node, coloring, False) == False:
            return False 

    return True 

def validate(graph, node, coloring, current_color):
    if node in coloring:
        return current_color == coloring[node] 

    coloring[node] = current_color 

    for neighbor in graph[node]:
        if validate(graph, neighbor, coloring, not current_color) == False:
            return False 

    return True 

if __name__ == "__main__":
    print(can_color({
    "x": ["y"],
    "y": ["x","z"],
    "z": ["y"]
    })) # -> True

    # Test case 01
    print(can_color({
    "q": ["r", "s"],
    "r": ["q", "s"],
    "s": ["r", "q"]
    })) # -> False

    # Test case 02
    print(can_color({
    "a": ["b", "c", "d"],
    "b": ["a"],
    "c": ["a"],
    "d": ["a"],
    })) # -> True