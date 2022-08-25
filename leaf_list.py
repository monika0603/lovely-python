""" 
Write a function, leaf_list, that takes in the root of a binary tree and returns a list 
containing the values of all leaf nodes in left-to-right order.
"""

from collections import deque 
class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def leaf_list_recursive(root):
    result = []
    return _leaf_list_recursive(root, result)

def _leaf_list_recursive(root, result):
    if root is None:
        return [] 

    if root.left is None and root.right is None:
        result.append(root.val) 

    _leaf_list_recursive(root.left, result)
    _leaf_list_recursive(root.right, result)

    return result 

def leaf_list(root):
    if root is None:
        return []

    stack = [root]
    result = []

    while stack:
        current = stack.pop() 

        if current.left is None and current.right is None:
            result.append(current.val)

        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)
        

    return result 

# Driver code 
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

    print(leaf_list_recursive(a)) # -> [ 'd', 'e', 'f' ] 

    # Test case 02
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

    print(leaf_list_recursive(a)) # -> [ 'd', 'g', 'h' ]

    # Test case 03
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

    print(leaf_list_recursive(a)) # -> [ 20, 1, 3, 54 ]

    # Test case 04 
    x = Node('x')
    #      x
    print(leaf_list(x)) # -> [ 'x' ]

    # Test case 05
    print(leaf_list(None)) # -> [ ]