from collections import deque 

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 


def breadth_first_values(root):
    if root is None:
        return [] 

    queue = deque([root])
    result = [] 

    while queue:
        current = queue.popleft() 

        result.append(current.val)

        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)

    return result 

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

    print(breadth_first_values(a))
    #    -> ['a', 'b', 'c', 'd', 'e', 'f']

    # Test case 02
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
    f.right = h

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f
    #    /       \
    #   g         h

    print(breadth_first_values(a))
    #   -> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    # Test case 03
    a = Node('a')
    #      a
    print(breadth_first_values(a))
    #    -> ['a']

    # Test case 04
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    x = Node('x')

    a.right = b
    b.left = c
    c.left = x
    c.right = d
    d.right = e

    #      a
    #       \
    #        b
    #       /
    #      c
    #    /  \
    #   x    d
    #         \
    #          e

    print(breadth_first_values(a)) 
    #    -> ['a', 'b', 'c', 'x', 'd', 'e']

    # Test case 05
    print(breadth_first_values(None))
    #    -> []