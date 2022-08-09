
import collections
from collections import deque
def shortest_path(edges, src, dst):

    graph = build_graph(edges) 
    queue = deque([(src, 0)])
    visited = set() 

    while queue:
        current, distance = queue.popleft()

        if current == dst:
            return distance 

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance+1))

    return -1 


def build_graph(edges):

    graph = collections.defaultdict(list) 
    for x,y in edges:
        graph[x].append(y)
        graph[y].append(x) 

    return graph 

# Driver code 
# Test case 01 
if __name__ == "__main__":
    edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
    ]

    print(shortest_path(edges, 'w', 'z')) # -> 2

    edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
    ]

    print(shortest_path(edges, 'y', 'x')) # -> 1

    edges = [
    ['a', 'c'],
    ['a', 'b'],
    ['c', 'b'],
    ['c', 'd'],
    ['b', 'd'],
    ['e', 'd'],
    ['g', 'f']
    ]

    print(shortest_path(edges, 'a', 'e')) # -> 3

    edges = [
    ['a', 'c'],
    ['a', 'b'],
    ['c', 'b'],
    ['c', 'd'],
    ['b', 'd'],
    ['e', 'd'],
    ['g', 'f']
    ]

    print(shortest_path(edges, 'e', 'c')) # -> 2

    edges = [
    ['a', 'c'],
    ['a', 'b'],
    ['c', 'b'],
    ['c', 'd'],
    ['b', 'd'],
    ['e', 'd'],
    ['g', 'f']
    ]

    print(shortest_path(edges, 'b', 'g')) # -> -1

    edges = [
    ['c', 'n'],
    ['c', 'e'],
    ['c', 's'],
    ['c', 'w'],
    ['w', 'e'],
    ]

    print(shortest_path(edges, 'w', 'e')) # -> 1

    edges = [
    ['c', 'n'],
    ['c', 'e'],
    ['c', 's'],
    ['c', 'w'],
    ['w', 'e'],
    ]

    print(shortest_path(edges, 'n', 'e')) # -> 2

    edges = [
    ['m', 'n'],
    ['n', 'o'],
    ['o', 'p'],
    ['p', 'q'],
    ['t', 'o'],
    ['r', 'q'],
    ['r', 's']
    ]

    print(shortest_path(edges, 'm', 's')) # -> 6