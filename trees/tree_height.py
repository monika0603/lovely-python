from collections import deque 

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def how_high(root):
    if root is None:
        return -1 

    queue = deque([(root, 0)])

    while queue:
        current, level = queue.popleft()

        if current.left is not None:
            queue.append((current.left, level+1))
        if current.right is not None:
            queue.append((current.right, level+1))

    return level 

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

    print(how_high(a)) # -> 2 

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

    print(how_high(a)) # -> 3
    
    # Test case 03
    a = Node('a')
    c = Node('c')
    a.right = c
    #      a
    #       \
    #        c
    print(how_high(a)) # -> 1

    # Test case 04
    print(how_high(None)) # -> -1