""" 
Write a function, is_binary_search_tree, that takes in the root of a binary tree. The function 
should return a boolean indicating whether or not the tree satisfies the binary search tree property.

A Binary Search Tree is a binary tree where all values within a node's left subtree are smaller 
than the node's value and all values in a node's right subtree are greater than or equal to the node's 
value.
"""

class Node:

    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def is_binary_search_tree(root):
    return _is_binary_search_tree(root, float("-inf"), float("inf")) 

def _is_binary_search_tree(root, left, right):
    if root is None:
        return True 

    if not root.val < right and root.val > left:
        return False  

    return _is_binary_search_tree(root.left, left, root.val) and _is_binary_search_tree(root.right, root.val, right)

if __name__ == "__main__":
    a = Node(12)
    b = Node(5)
    c = Node(18)
    d = Node(3)
    e = Node(9)
    f = Node(19)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      12
    #    /   \
    #   5     18
    #  / \     \
    # 3   9     19

    print(is_binary_search_tree(a)) # -> True

    # Test case 02
    a = Node(12)
    b = Node(5)
    c = Node(18)
    d = Node(3)
    e = Node(15)
    f = Node(19)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      12
    #    /   \
    #   5     18
    #  / \     \
    # 3   15     19

    print(is_binary_search_tree(a)) # -> False 

    # Test case 03
    a = Node(12)
    b = Node(5)
    c = Node(19)
    d = Node(3)
    e = Node(9)
    f = Node(19)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      12
    #    /   \
    #   5     19
    #  / \     \
    # 3   9     19

    print(is_binary_search_tree(a)) # -> True 

    # Test case 04
    a = Node(12)
    b = Node(5)
    c = Node(10)
    d = Node(3)
    e = Node(9)
    f = Node(19)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      12
    #    /   \
    #   5     10
    #  / \     \
    # 3   9     19

    print(is_binary_search_tree(a)) # -> False