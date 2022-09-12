""" 
Application of Lowest Common Ancestor(LCA):
To determine the distance between pairs of nodes in a tree: the distance from n1 to n2 can be computed as the distance 
from the root to n1, plus the distance from the root to n2, minus twice the distance from the root to their lowest common 
ancestor.
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 

def lowest_common_ancestor(root, target_a, target_b):
    path_a = path_target(root, target_a)
    path_b = path_target(root, target_b)

    result = [x for x in path_a if x in path_b]
    return result[-1]

def path_target(root, target):
    if root is None:
        return 

    if root.val == target:
        return root.val 

    left_path = path_target(root.left, target)
    if left_path is not None:
        return [root.val, *left_path] 

    right_path = path_target(root.right, target)
    if right_path is not None:
        return [root.val, *right_path] 

if __name__ == "__main__":
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    h = Node('h')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    e.right = h

    #      a
    #    /    \
    #   b      c
    #  / \      \
    # d   e      f
    #    / \
    #    g  h

    print(lowest_common_ancestor(a, 'd', 'h'))

    # Test case 01
    print(lowest_common_ancestor(a, 'd', 'g')) # b

    # Test case 03
    print(lowest_common_ancestor(a, 'g', 'c')) # a

    # Test case 04
    print(lowest_common_ancestor(a, 'b', 'g')) # b
