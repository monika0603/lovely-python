
import collections 
def prereqs_possible(numCourses, prereqs):

    graph = build_graph(numCourses, prereqs)

    visited = set()
    visiting = set() 

    for node in graph:
        if traverse(graph, node, visiting, visited) == True:
            return False 

    return True  

def traverse(graph, node, visiting, visited):
    if node in visited:
        return False 

    if node in visiting:
        return True 

    visiting.add(node) 

    for neighbor in graph[node]:
        if traverse(graph, neighbor, visiting, visited) == True:
            return True 

    visiting.remove(node)
    visited.add(node)

    return False 

def build_graph(numCourses, prereqs):

    graph = collections.defaultdict(list) 

    for i in range(numCourses):
        graph[i] = [] 

    for x,y in prereqs:
        graph[x].append(y) 

    return graph 

# Driver code 
# Test case 01 
if __name__ == "__main__":
    numCourses = 6
    prereqs = [
    (0, 1),
    (2, 3),
    (0, 2),
    (1, 3),
    (4, 5),
    ]
    print(prereqs_possible(numCourses, prereqs)) # -> True

    # Test case 02 
    numCourses = 6
    prereqs = [
    (0, 1),
    (2, 3),
    (0, 2),
    (1, 3),
    (4, 5),
    (3, 0),
    ]
    print(prereqs_possible(numCourses, prereqs)) # -> False

    # Test case 03 
    numCourses = 5
    prereqs = [
    (2, 4),
    (1, 0),
    (0, 2),
    (0, 4),
    ]
    print(prereqs_possible(numCourses, prereqs)) # -> True

    # Test case 04 
    numCourses = 6
    prereqs = [
    (2, 4),
    (1, 0),
    (0, 2),
    (0, 4),
    (5, 3),
    (3, 5),
    ]
    print(prereqs_possible(numCourses, prereqs)) # -> False

    # Test case 05 
    numCourses = 8
    prereqs = [
    (1, 0),
    (0, 6),
    (2, 0),
    (0, 5),
    (3, 7),
    (4, 3),
    ]
    prereqs_possible(numCourses, prereqs) # -> True 

    # Test case 06
    numCourses = 8
    prereqs = [
    (1, 0),
    (0, 6),
    (2, 0),
    (0, 5),
    (3, 7),
    (7, 4),
    (4, 3),
    ]
    print(prereqs_possible(numCourses, prereqs)) # -> False

    # Test case 07
    numCourses = 42
    prereqs = [(6, 36)]
    print(prereqs_possible(numCourses, prereqs)) # -> True