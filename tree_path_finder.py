""" 
Write a function, path_finder, that takes in the root of a binary tree and a target value. 
The function should return an array representing a path to the target value. If the target 
value is not found in the tree, then return None.

You may assume that the tree contains unique values.

Time complexity: O(n^2)
"""

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def path_finder(node, target):
    if node is None:
        return None  

    if node.val == target:
        return [node.val] 

    left_path = path_finder(node.left, target)
    if left_path is not None:
        return [node.val, *left_path]

    right_path = path_finder(node.right, target)
    if right_path is not None:
        return [node.val, *right_path]

    return None

# Driver code 
# Test case 
if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f

    print(path_finder(a, 'e')) # -> [ 'a', 'b', 'e' ]

    # Test case 02
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f

    print(path_finder(a, 'p')) # -> None

    # Test case 03
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    g = Node("g")
    h = Node("h")

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f
    #    /       \
    #   g         h

    print(path_finder(a, "c")) # -> ['a', 'c']

    # Test case 04
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    g = Node("g")
    h = Node("h")

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f
    #    /       \
    #   g         h

    print(path_finder(a, "h")) # -> ['a', 'c', 'f', 'h']

    # Test case 05
    curr = Node(0)
    root = curr
    for i in range(1, 19500):
        curr.right = Node(i)
        curr = curr.right

    #      0
    #       \
    #        1
    #         \
    #          2
    #           \
    #            3
    #             .
    #              .
    #               .
    #              19498
    #                \
    #                19499

    print(path_finder(root, 16281)) # -> [0, 1, 2, 3, ..., 16280, 16281]