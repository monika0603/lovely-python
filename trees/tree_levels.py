
from collections import deque 

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def tree_levels(root):
    if root is None:
        return []

    queue = deque([(root, 0)])
    result = [] 

    while queue:
        current, level = queue.popleft() 

        if level == len(result):
            result.append([current.val])
        else:
            result[level].append(current.val) 

        if current.left is not None:
            queue.append((current.left, level+1))
        if current.right is not None:
            queue.append((current.right, level+1))

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

    print(tree_levels(a)) # ->
    # [
    #   ['a'],
    #   ['b', 'c'],
    #   ['d', 'e', 'f']
    # ]

    # Test case 02
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    h = Node('h')
    i = Node('i')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    e.right = h
    f.left = i

    #         a
    #      /    \
    #     b      c
    #   /  \      \
    #  d    e      f
    #      / \    /
    #     g  h   i

    print(tree_levels(a)) # ->
    # [
    #   ['a'],
    #   ['b', 'c'],
    #   ['d', 'e', 'f'],
    #   ['g', 'h', 'i']
    # ]

    # Test case 03
    q = Node('q')
    r = Node('r')
    s = Node('s')
    t = Node('t')
    u = Node('u')
    v = Node('v')

    q.left = r
    q.right = s
    r.right = t
    t.left = u
    u.right = v

    #      q
    #    /   \
    #   r     s
    #    \
    #     t
    #    /
    #   u
    #  /
    # v

    print(tree_levels(q)) # ->
    # [
    #   ['q'],
    #   ['r', 's'],
    #   ['t'],
    #   ['u'],
    #   ['v']
    # ]

    # Test case 04
    print(tree_levels(None)) # -> []