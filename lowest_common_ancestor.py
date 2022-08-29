""" 
Write a function, lowest_common_ancestor, that takes in the root of a binary tree and two values. 
The function should return the value of the lowest common ancestor of the two values in the tree.

You may assume that the tree values are unique and the tree is non-empty.

Note that a node may be considered an ancestor of itself.


"""
class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 


def lowest_common_ancestor(root, target1, target2):
    result_1 = _path_target(root, target1)
    result_2 = _path_target(root, target2)
    
    output = []
    for i in result_1:
        if i in result_2:
            output.append(i)

    return output[-1]

def _path_target(root, target):
    if root is None:
        return None 

    if root.val == target:
        return root.val

    left_path = _path_target(root.left, target)
    if left_path is not None:
        return [root.val, *left_path] 

    right_path = _path_target(root.right, target)
    if right_path is not None:
        return [root.val, *right_path]


#Driver code 
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

    print(lowest_common_ancestor(a, 'd', 'h'))

    # Test case 02
    print(lowest_common_ancestor(a, 'd', 'g')) # b

    # Test case 03
    print(lowest_common_ancestor(a, 'g', 'c')) # a

    # Test case 04
    print(lowest_common_ancestor(a, 'b', 'g')) # b

    # Test case 05
    print(lowest_common_ancestor(a, 'f', 'c')) # c

    # Test case 06
    l = Node('l')
    m = Node('m')
    n = Node('n')
    o = Node('o')
    p = Node('p')
    q = Node('q')
    r = Node('r')
    s = Node('s')
    t = Node('t')

    l.left = m
    l.right = n
    n.left = o
    n.right = p
    o.left = q
    o.right = r
    p.left = s
    p.right = t

    #        l
    #     /     \
    #    m       n
    #         /    \
    #         o     p
    #        / \   / \
    #       q   r s   t

    print(lowest_common_ancestor(l, 'r', 'p')) # n 

    # Test case 07
    print(lowest_common_ancestor(l, 'm', 'o')) # l

    # Test case 08
    print(lowest_common_ancestor(l, 't', 'q')) # n

    # Test case 09
    print(lowest_common_ancestor(l, 's', 'p')) # p