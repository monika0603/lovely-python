""" 
Write a function, lefty_nodes, that takes in the root of a binary tree. The function should return a 
list containing the left-most value on every level of the tree. The list must be ordered in a 
top-down fashion where the root is the first item.

Note that the left-most node on a level may not necessarily be a left child.
"""

from collections import deque 
class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

# Using depth-first-search
def lefty_nodes(root):
    values = [] 
    traverse(root, 0, values)
    return values 

def traverse(root, level, values):
    if root is None:
        return 

    if level == len(values):
        values.append(root.val) 

    traverse(root.left, level+1, values)
    traverse(root.right, level+1, values)

# Using DFS iteratively
def lefty_nodes_dfs(root):
    if root is None:
        return 

    stack = [(root, 0)]
    result = [] 

    while stack:
        current, level = stack.pop()

        if level == len(result):
            result.append(current.val)

        if current.right is not None:
            stack.append((current.right, level+1))
        if current.left is not None:
            stack.append((current.left, level+1))
        
    return result 

# Printing righty nodes using iterative DFS 
def righty_nodes_dfs(root):
    if root is None:
        return 

    stack = [(root, 0)]
    result = [] 

    while stack:
        current, level = stack.pop()

        if level == len(result):
            result.append(current.val) 

        if current.left is not None:
            stack.append((current.left, level+1))
        if current.right is not None:
            stack.append((current.right, level+1)) 

    return result 

# Driver code 
# Test case 01
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

    print(lefty_nodes(a)) # [ 'a', 'b', 'd', 'g' ]
    print(lefty_nodes_dfs(a)) # [ 'a', 'b', 'd', 'g' ]
    print(righty_nodes_dfs(a))
