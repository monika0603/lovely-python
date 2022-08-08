graph = {
    "a": ["b", "c"], 
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

def graph_dfs_stack(graph, node):

    stack = [node]
    result = []

    while stack:
        current = stack.pop()
        result.append(current) 

        for neighbor in graph[current]:
            stack.append(neighbor)

    return result 

if __name__ == "__main__":
    print(graph_dfs_stack(graph, "a"))