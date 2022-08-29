""" 
Write a function, flip_tree, that takes in the root of a binary tree. The function should flip 
the binary tree, turning left subtrees into right subtrees and vice-versa. This flipping 
should occur in-place by modifying the original tree. The function should return the root of the tree.
"""

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def flip_tree(root):
    if root is None:
        return None 

    left = flip_tree(root.left)
    right = flip_tree(root.right) 
    root.left = right 
    root.right = left 

    return root 

# Driver code 
if __name__ == "__main__":
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
    e.right = h

    #      a
    #    /    \
    #   b      c
    #  / \      \
    # d   e      f
    #    / \
    #    g  h

    print(flip_tree(a)) 