class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def depth_first_values(root):
    return _depth_first_values(root, [])

def _depth_first_values(root, result):
    if root is None:
        return [] 

    result.append(root.val)

    _depth_first_values(root.left, result) 
    _depth_first_values(root.right, result)

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

    print(depth_first_values(a))
    #   -> ['a', 'b', 'd', 'e', 'c', 'f']