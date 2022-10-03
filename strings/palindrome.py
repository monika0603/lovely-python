
def palindrome(s):
    result = _palindrome(s, 0, len(s)-1) 
    if result == len(s):
        return True 
    else:
        return False 

def _palindrome(s, i, j):
    if i == j:
        return 1 
    if i > j:
        return 0 

    if s[i] == s[j]:
        count = 2 + _palindrome(s, i+1, j-1)
    else:
        count = max(_palindrome(s, i+1, j), _palindrome(s, i, j-1)) 

    return count 

if __name__ == "__main__":
    s = 'aabaa'
    print(palindrome(s))

    s = 'abac'
    print(palindrome(s))