""" 
Write a function, tree_min_value, that takes in the root of a binary tree that contains 
number values. The function should return the minimum value within the tree.

You may assume that the input tree is non-empty.
"""

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def tree_min_value(node):
    if node is None:
        return 0 

    stack = [node]
    min_value = float("inf")

    while stack:
        current = stack.pop()

        min_value = min(min_value, current.val)

        if current.left is not None:
            stack.append(current.left)
        if current.right is not None:
            stack.append(current.right)

    return min_value

# Driver code 
if __name__ == "__main__":
    # Test case 01
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
    print(tree_min_value(a)) # -> -2 

    # Test case 02
    a = Node(5)
    b = Node(11)
    c = Node(3)
    d = Node(4)
    e = Node(14)
    f = Node(12)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #       5
    #    /    \
    #   11     3
    #  / \      \
    # 4   14     12

    print(tree_min_value(a)) # -> 3

    # Test case 03
    a = Node(-1)
    b = Node(-6)
    c = Node(-5)
    d = Node(-3)
    e = Node(-4)
    f = Node(-13)
    g = Node(-2)
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
    # -3   -4   -13
    #     /       \
    #    -2       -2

    print(tree_min_value(a)) # -> -13

    # Test case 04
    a = Node(42)

    print(tree_min_value(a)) # -> 42