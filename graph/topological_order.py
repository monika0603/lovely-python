
def topological_order(graph):
    num_parents = {} 

    for node in graph:
        num_parents[node] = 0 

    for node in graph:
        for child in graph[node]:
            num_parents[child] += 1 

    ready = [node for node in num_parents if num_parents[node] == 0]
    order = []

    while ready:
        current = ready.pop()
        order.append(current)

        for child in graph[current]:
            num_parents[child] -= 1

            if num_parents[child] == 0:
                ready.append(child)

    return order 


if __name__ == "__main__":
    print(topological_order({
    "a": ["f"],
    "b": ["d"],
    "c": ["a", "f"],
    "d": ["e"],
    "e": [],
    "f": ["b", "e"],
    })) # -> ['c', 'a', 'f', 'b', 'd', 'e']

    # Test case 02
    print(topological_order({
    "h": ["l", "m"],
    "i": ["k"],
    "j": ["k", "i"],
    "k": ["h", "m"],
    "l": ["m"],
    "m": [],
    })) # -> ['j', 'i', 'k', 'h', 'l', 'm'] 

    # Test case 03
    print(topological_order({
    "q": [],
    "r": ["q"],
    "s": ["r"],
    "t": ["s"],
    })) # -> ['t', 's', 'r', 'q']