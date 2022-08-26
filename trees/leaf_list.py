class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def leaf_list(root):
    result = [] 
    return _leaf_list(root, result)

def _leaf_list(root, result):
    if root is None:
        return [] 

    if root.left is None and root.right is None:
        result.append(root.val)

    _leaf_list(root.left, result)
    _leaf_list(root.right, result) 

    return result

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

    print(leaf_list(a)) # -> [ 'd', 'e', 'f' ] 

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

    print(leaf_list(a)) # -> [ 'd', 'g', 'h' ] 

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

    print(leaf_list(a)) # -> [ 20, 1, 3, 54 ]

    # Test case 04
    x = Node('x')
    #      x
    print(leaf_list(x)) # -> [ 'x' ]

    # Test case 05
    print(leaf_list(None)) # -> []