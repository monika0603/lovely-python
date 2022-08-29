
from turtle import color


def can_color(graph):
    coloring = {} 

    for node in graph:
        if node not in coloring:
            if _can_color(graph, node, coloring, False) == False:
                return False 

    return True 

def _can_color(graph, node, coloring, current_color):
    if node in coloring:
        return coloring[node] == current_color 

    coloring[node] = current_color 

    for neighbor in graph[node]:
        if _can_color(graph, neighbor, coloring, not current_color) == False:
            return False 

    return True 


if __name__ == "__main__":
    # Test case 01
    print(can_color({
    "x": ["y"],
    "y": ["x","z"],
    "z": ["y"]
    })) # -> True

    # Test case 02
    print(can_color({
    "q": ["r", "s"],
    "r": ["q", "s"],
    "s": ["r", "q"]
    })) # -> False 

    # Test case 03
    print(can_color({
    "a": ["b", "c", "d"],
    "b": ["a"],
    "c": ["a", "d"],
    "d": ["a", "c"],
    })) # -> False