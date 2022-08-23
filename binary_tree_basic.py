""" 
Write a function, depth_first_values, that takes in the root of a binary tree. The function 
should return a list containing all values of the tree in depth-first order.
"""

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

# Recursive method for depth-first-search
def depth_first_values(node):
    if node is None:
        return []

    left_values = depth_first_values(node.left)
    right_values = depth_first_values(node.right)
    return [node.val, *left_values, *right_values]


# Driver code 
# Test case 01 
if __name__ == "__main__":
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')        
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

    print(depth_first_values(a)) #   -> ['a', 'b', 'd', 'e', 'c', 'f']

    # Test case 02
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f
    #    /
    #   g

    print(depth_first_values(a))
    #   -> ['a', 'b', 'd', 'e', 'g', 'c', 'f']

    # Test case 03
    a = Node('a')
    #     a
    print(depth_first_values(a))
    #   -> ['a']

    # Test case 04
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    a.right = b;
    b.left = c;
    c.right = d;
    d.right = e;

    #      a
    #       \
    #        b
    #       /
    #      c
    #       \
    #        d
    #         \
    #          e

    print(depth_first_values(a))
    #   -> ['a', 'b', 'c', 'd', 'e']

    # Test case 05
    print(depth_first_values(None))
    #   -> []