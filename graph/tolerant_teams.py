import collections
def tolerant_teams(edges):

    graph = build_graph(edges) 

    coloring = {} 
    for node in graph:
        if node not in coloring:
            if _tolerant_teams(graph, node, coloring, False) == False:
                return False 

    return True 

def _tolerant_teams(graph, node, coloring, current_color):
    if node in coloring:
        return coloring[node] == current_color 

    coloring[node] = current_color 

    for neighbor in graph[node]:
        if _tolerant_teams(graph, neighbor, coloring, not current_color) == False:
            return False 

    return True 

def build_graph(edges):

    graph = collections.defaultdict(list)

    for x,y in edges:
        graph[x].append(y)
        graph[y].append(x) 

    return graph 


if __name__ == "__main__":
    print(tolerant_teams([
    ('philip', 'seb'),
    ('raj', 'nader')
    ])) # -> True

    # Test case 02
    print(tolerant_teams([
    ('philip', 'seb'),
    ('raj', 'nader'),
    ('raj', 'philip'),
    ('seb', 'raj')
    ])) # -> False 

    # Test case 03
    print(tolerant_teams([
    ('cindy', 'anj'),
    ('alex', 'matt'),
    ('alex', 'cindy'),
    ('anj', 'matt'),
    ('brando', 'matt')
    ])) # -> True

    # Test case 04
    print(tolerant_teams([
    ('alex', 'anj'),
    ('alex', 'matt'),
    ('alex', 'cindy'),
    ('anj', 'matt'),
    ('brando', 'matt')
    ])) # -> False