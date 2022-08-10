
import collections
def semesters_required(num_courses, prereqs):

    graph = build_graph(num_courses, prereqs)

    distance = {} 
    for node in graph:
        if len(graph[node]) == 0:
            # It will take at least one semester to complete a course 
            distance[node] = 1

    for node in graph:
        traverse_nodes(graph, node, distance) 

    return max(distance.values())

def traverse_nodes(graph, node, distance):
    if node in distance:
        return distance[node] 

    # You need at least one semester to complete a course 
    semester = 1
    for neighbor in graph[node]:
        attempt = traverse_nodes(graph, neighbor, distance)
        semester = max(attempt, semester) 

    distance[node] = 1 + semester 
    return distance[node] 

def build_graph(num_courses, prereqs):

    graph = collections.defaultdict(list)

    for i in range(num_courses):
        graph[i] = []

    for x, y in prereqs:
        graph[x].append(y)

    return graph 

# Driver code 
if __name__ == "__main__":
    # Test case 01
    num_courses = 6
    prereqs = [
    (1, 2),
    (2, 4),
    (3, 5),
    (0, 5),
    ]
    print(semesters_required(num_courses, prereqs)) # -> 3

    # Test case 02 
    num_courses = 7
    prereqs = [
    (4, 3),
    (3, 2),
    (2, 1),
    (1, 0),
    (5, 2),
    (5, 6),
    ]
    print(semesters_required(num_courses, prereqs)) # -> 5

    # Test case 03
    num_courses = 5
    prereqs = [
    (1, 0),
    (3, 4),
    (1, 2),
    (3, 2),
    ]
    print(semesters_required(num_courses, prereqs)) # -> 2

    # Test case 04
    num_courses = 12
    prereqs = []
    print(semesters_required(num_courses, prereqs)) # -> 1

    # Test case 05
    num_courses = 3
    prereqs = [
    (0, 2),
    (0, 1),
    (1, 2),
    ]
    print(semesters_required(num_courses, prereqs)) # -> 3

    # Test case 06
    num_courses = 6
    prereqs = [
    (3, 4),
    (3, 0),
    (3, 1),
    (3, 2),
    (3, 5),
    ]
    print(semesters_required(num_courses, prereqs)) # -> 2