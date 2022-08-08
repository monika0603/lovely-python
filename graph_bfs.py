graph = {
    "a": ["b", "c"], 
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

from collections import deque
def graph_bfs(graph, node):

    queue = deque([node]) 

    result = []

    while queue:
        current = queue.popleft() 

        result.append(current)
        for neighbor in graph[current]:
            queue.append(neighbor)

    return result 

if __name__ == "__main__":
    print(graph_bfs(graph, "a"))




