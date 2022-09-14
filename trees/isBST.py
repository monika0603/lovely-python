class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 

def is_binary_search_tree(root):
    return isBST(root, float("-inf"), float("inf"))

def isBST(root, left, right):
    if root is None:
        return True 

    if not root.val < right and root.val > left:
        return False 

    return isBST(root.left, left, root.val) and isBST(root.right, root.val, right)



if __name__ == "__main__":
    a = Node(12)
    b = Node(5)
    c = Node(18)
    d = Node(3)
    e = Node(9)
    f = Node(19)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      12
    #    /   \
    #   5     18
    #  / \     \
    # 3   9     19

    print(is_binary_search_tree(a)) # -> True

    # Test case 01
    a = Node(12)
    b = Node(5)
    c = Node(18)
    d = Node(3)
    e = Node(15)
    f = Node(19)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      12
    #    /   \
    #   5     18
    #  / \     \
    # 3   15     19

    print(is_binary_search_tree(a)) # -> False 
