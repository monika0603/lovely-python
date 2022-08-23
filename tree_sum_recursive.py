""" 
Write a function, tree_sum, that takes in the root of a binary tree that contains number values. 
The function should return the total sum of all values in the tree.
"""

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def tree_sum(node):
    if node is None:
        return 0 

    return node.val + tree_sum(node.left) + tree_sum(node.right)


# Driver code 
# Test case 01 
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

    print(tree_sum(a)) # -> 21

    # Test case 02 
    a = Node(1)
    b = Node(6)
    c = Node(0)
    d = Node(3)
    e = Node(-6)
    f = Node(2)
    g = Node(2)
    h = Node(2)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h

    #      1
    #    /   \
    #   6     0
    #  / \     \
    # 3   -6    2
    #    /       \
    #   2         2

    print(tree_sum(a)) # -> 10

    # Test case 03
    print(tree_sum(None)) # -> 0