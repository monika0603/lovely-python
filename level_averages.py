""" 
Write a function, level_averages, that takes in the root of a binary tree that contains number values. 
The function should return a list containing the average value of each level.
"""

from collections import deque

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def level_averages(root):
    if root is None:
        return [] 

    queue = deque([(root, 0)])
    result = []

    while queue:
        current, level = queue.popleft() 

        if level == len(result):
            result.append([current.val])
        else:
            result[level].append(current.val) 

        if current.left is not None:
            queue.append((current.left, level+1))
        if current.right is not None:
            queue.append((current.right, level+1))

    output = []
    for levels in result:
        average = sum(levels)/len(levels)
        output.append(average)

    return output

# Driver code 
if __name__ == "__main__":
    a = Node(3)
    b = Node(11)
    c = Node(4)
    d = Node(4)
    e = Node(-2)
    f = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #       3
    #    /    \
    #   11     4
    #  / \      \
    # 4   -2     1

    print(level_averages(a)) # -> [ 3, 7.5, 1 ] 

    # Test case 02
    a = Node(5)
    b = Node(11)
    c = Node(54)
    d = Node(20)
    e = Node(15)
    f = Node(1)
    g = Node(3)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    e.left = f
    e.right = g

    #        5
    #     /    \
    #    11    54
    #  /   \
    # 20   15
    #      / \
    #     1  3

    print(level_averages(a)) # -> [ 5, 32.5, 17.5, 2 ]

    # Test case 03
    a = Node(-1)
    b = Node(-6)
    c = Node(-5)
    d = Node(-3)
    e = Node(0)
    f = Node(45)
    g = Node(-1)
    h = Node(-2)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h

    #        -1
    #      /   \
    #    -6    -5
    #   /  \     \
    # -3   0     45
    #     /       \
    #    -1       -2

    print(level_averages(a)) # -> [ -1, -5.5, 14, -1.5 ]

    # Test case 04
    q = Node(13)
    r = Node(4)
    s = Node(2)
    t = Node(9)
    u = Node(2)
    v = Node(42)

    q.left = r
    q.right = s
    r.right = t
    t.left = u
    u.right = v

    #        13
    #      /   \
    #     4     2
    #      \
    #       9
    #      /
    #     2
    #    /
    #   42

    print(level_averages(q)) # -> [ 13, 3, 9, 2, 42 ]

    # Test case 05
    print(level_averages(None)) # -> [ ]