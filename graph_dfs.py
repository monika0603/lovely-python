
graph = {
    "a": ["b", "c"], 
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

def dfs(graph):

    visited = set() 
    count = 0 
    for node in graph:
        count += 1 
        explore(graph, node, visited)

    return len(visited), count

def explore(graph, node, visited):
    if node in visited:
        return 

    visited.add(node) 

    for neighbor in graph[node]:
        explore(graph, neighbor, visited)


if __name__ == "__main__":
    print(dfs(graph))