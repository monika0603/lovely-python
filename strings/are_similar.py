""" 
Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements 
in one of the arrays.

Given two arrays a and b, check whether they are similar.
"""

def are_similar(a, b):

    count_a = {}
    count_b = {} 

    for a_i in a:
        count_a[a_i] = 1 + count_a.get(a_i, 0)
    
    for b_i in b:
        count_b[b_i] = 1 + count_b.get(b_i, 0) 

    for c in count_a:
        if c not in count_b:
            return False 
        if count_a[c] != count_b[c]:
            return False 

    return True 

if __name__ == "__main__":
    a = [1,2,3]
    b = [1,2,3]
    print(are_similar(a,b))

    # Test case 01
    a = [1,2,3]
    b = [2,1,3]
    print(are_similar(a,b))

    # Test case 02
    a = [1,2,2]
    b = [2,1,1]
    print(are_similar(a,b))

    # Test case 03
    a = [1,2,3]
    b = [1,10,2]
    print(are_similar(a,b))

    # Test case 04
    a = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
    b = [832, 570, 148, 998, 533, 561, 455, 147, 894, 279]
    print(are_similar(a,b))

