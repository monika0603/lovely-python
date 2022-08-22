""" 
Write a function, max_palin_subsequence, that takes in a string as an argument. The function should 
return the length of the longest subsequence of the string that is also a palindrome.

A subsequence of a string can be created by deleting any characters of the string, while 
maintaining the relative order of characters.
"""

def max_palin_subsequence(s):
    return _max_palin_subsequence(s, 0, len(s)-1)

def _max_palin_subsequence(s, i, j):
    if i == j:
        return 1 

    if i > j:
        return 0 

    if s[i] == s[j]:
        return 2 + _max_palin_subsequence(s, i+1, j-1)
    else:
        return max(_max_palin_subsequence(s, i, j-1), _max_palin_subsequence(s, i+1, j))

# Optimized code using memoization
def max_palin_subsequence_memo(s):
    return _max_palin_subsequence_memo(s, 0, len(s)-1, {})

def _max_palin_subsequence_memo(s, i, j, memo):
    key = (i, j)
    if key in memo:
        return memo[key] 

    if i == j:
        return 1
    if i > j:
        return 0 

    if s[i] == s[j]:
        memo[key] = 2 + _max_palin_subsequence_memo(s, i+1, j-1, memo)
        return 2 + _max_palin_subsequence_memo(s, i+1, j-1, memo)
    else:
        memo[key] = max(_max_palin_subsequence_memo(s, i+1, j, memo), _max_palin_subsequence_memo(s, i, j-1, memo))
        return max(_max_palin_subsequence_memo(s, i+1, j, memo), _max_palin_subsequence_memo(s, i, j-1, memo))

# Driver code 
if __name__ == "__main__":
    # Test case 01
    print(max_palin_subsequence("luwxult")) # -> 5

    # Test case 02
    print(max_palin_subsequence("xyzaxxzy")) # -> 6

    # Test case 03 
    print(max_palin_subsequence("lol")) # -> 3

    # Test case 04
    print(max_palin_subsequence("boabcdefop")) # -> 3

    # Test case 05
    print(max_palin_subsequence("z")) # -> 1

    # Test case 06
    print(max_palin_subsequence_memo("chartreusepugvicefree")) # -> 7

    # Test case 07
    print(max_palin_subsequence_memo("qwueoiuahsdjnweuueueunasdnmnqweuzqwerty")) # -> 15

    # Test case 08
    print(max_palin_subsequence_memo("enamelpinportlandtildecoldpressedironyflannelsemioticsedisonbulbfashionaxe")) # -> 31