""" 
Write a function, topological_order, that takes in a dictionary representing the adjacency list 
for a directed-acyclic graph. The function should return a list containing the topological-order 
of the graph.

The topological ordering of a graph is a sequence where "parent nodes" appear before their 
"children" within the sequence.

Algorithm:

1. Create a hash-map where keys are nodes of the graph and values are number of arrows pointing to it. 

    e -- c    f
    \     \   |  \ 
     \      \ |  d
       b ---- a/

       a: 2
       b: 1
       c: 1
       d: 2
       e: 0
       f: 1

2. Start with nodes that have no parents, i.e., values of 0. 
3. Then go to the next nodes that have value = 1 and decrement them by 1. Now they are ready to be visited. 
4. I maintin two lists here. Order list will contain the final output while ready list is an intermediate 
list that will help me keep track of the nodes that have a value 1 to start with. When we decremented the 
value we have 0. We may have many such nodes. So all of them must be visited at once. 
"""

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

    # Test case 04
    print(topological_order({
    "v": ["z", "w"],
    "w": [],
    "x": ["w", "v", "z"],
    "y": ["x"],
    "z": ["w"],
    })) # -> ['y', 'x', 'v', 'z', 'w']