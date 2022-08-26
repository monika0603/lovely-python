
from collections import deque 
class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def bottom_right_value(root):
    if root is None:
        return [] 

    queue = deque([root])
    result = [] 

    while queue:
        current = queue.popleft()

        if current.left is None and current.right is None:
            result.append(current.val)

        if current.left is not None:
            queue.append(current.left) 
        if current.right is not None:
            queue.append(current.right)

    return result[0]

if __name__ == "__main__":
    a = Node(3)
    b = Node(11)
    c = Node(10)
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
    #   11     10
    #  / \      \
    # 4   -2     1

    print(bottom_right_value(a)) # -> 1

    # Test case 02
    a = Node(-1)
    b = Node(-6)
    c = Node(-5)
    d = Node(-3)
    e = Node(-4)
    f = Node(-13)
    g = Node(-2)
    h = Node(6)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    e.right = h

    #        -1
    #      /   \
    #    -6    -5
    #   /  \     \
    # -3   -4   -13
    #     / \       
    #    -2  6

    print(bottom_right_value(a)) # -> 6 

    # Test case 03
    a = Node(-1)
    b = Node(-6)
    c = Node(-5)
    d = Node(-3)
    e = Node(-4)
    f = Node(-13)
    g = Node(-2)
    h = Node(6)
    i = Node(7)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    e.right = h
    f.left = i

    #        -1
    #      /   \
    #    -6    -5
    #   /  \     \
    # -3   -4   -13
    #     / \    /   
    #    -2  6  7 

    print(bottom_right_value(a)) # -> 7 

    # Test case 04
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')

    a.left = b
    a.right = c
    b.right = d
    d.left = e
    e.right = f

    #      a
    #    /   \ 
    #   b     c
    #    \
    #     d
    #    /
    #   e
    #  /
    # f
            
    print(bottom_right_value(a)) # -> 'f'