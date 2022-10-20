""" 
Given some integer, find the maximal number you can obtain by deleting exactly 
one digit of the given number.

Example

For n = 152, the output should be
solution(n) = 52;
For n = 1001, the output should be
solution(n) = 101.
"""

def deleteDigit(n):
    n = list(str(n))
    return _deleteDigit(n)

def _deleteDigit(n):
    if len(n) == 0:
        return [[]] 

    first = n[0] 
    full_permutations = []
    for perm in _deleteDigit(n[1:]):
        for i in range(len(perm)+1):
            full_permutations.append(perm[:i] + [first] + perm[i:]) 

    return full_permutations



if __name__ == "__main__":
    n = ['1','5','2']
    n = 152
    print(deleteDigit(n)) 