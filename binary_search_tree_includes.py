
class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 

def binary_search_tree_includes(root, target):
    if root is None:
        return False 

    if root.val == target:
        return True 

    return binary_search_tree_includes(root.left, target) or binary_search_tree_includes(root.right, target) 


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

    print(binary_search_tree_includes(a, 9)) # -> True

    # Test case 02
    print(binary_search_tree_includes(a, 15)) # -> False 

    # Test case 03
    print(binary_search_tree_includes(a, 1)) # -> False

    # Test case 04 
    print(binary_search_tree_includes(a, 12)) # -> True
    