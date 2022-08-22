""" 
Write a function, can_concat, that takes in a string and a list of words as arguments. The function 
should return boolean indicating whether or not it is possible to concatenate words of the list 
together to form the string.

You may reuse words of the list as many times as needed.
"""

# Brute force method
def can_concat(s, word_list):
    if len(s) == 0:
        return True 

    for word in word_list:
        if s.startswith(word):
            new_s = s[len(word):]
            if can_concat(new_s, word_list) == True:
                return True 

    return False 

# Optimized method using memoization
def can_concat_memo(s, word_list):
    return _can_concat_memo(s, word_list, {})

def _can_concat_memo(s, word_list, memo):
    if s in memo:
        return memo[s] 

    if len(s) == 0:
        return True 

    for word in word_list:
        if s.startswith(word):
            new_s = s[len(word):]
            if _can_concat_memo(new_s, word_list, memo) == True:
                memo[s] = True 
                return True 

    memo[s] = False 
    return False 

# Driver code
if __name__ == "__main__":
    # Test case 01
    print(can_concat("oneisnone", ["one", "none", "is"])) #  -> True

    # Test case 02
    print(can_concat("oneisnone", ["on", "e", "is"])) #  -> False

    # Test case 03 
    print(can_concat("oneisnone", ["on", "e", "is", "n"])) #  -> True

    # Test case 04 
    print(can_concat("foodisgood", ["is", "g", "ood", "f"])) #  -> True

    # Test case 05 
    print(can_concat("santahat", ["santah", "hat"])) #  -> False

    # Test case 06
    print(can_concat("santahat", ["santah", "san", "hat", "tahat"])) #  -> True

    # Test case 07
    print(can_concat_memo("rrrrrrrrrrrrrrrrrrrrrrrrrrx", ["r", "rr", "rrr", "rrrr", "rrrrr", "rrrrrr"])) #  -> False