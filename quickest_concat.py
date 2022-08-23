""" 
Write a function, quickest_concat, that takes in a string and a list of words as arguments. 
The function should return the minimum number of words needed to build the string by 
concatenating words of the list.

You may use words of the list as many times as needed.
"""

# Brute force solution
def quickest_concat(s, words_list):
    result = _quickest_concat(s, words_list)
    if result == float("inf"):
        return -1 
    else:
        return result 

def _quickest_concat(s, words_list):

    if len(s) == 0:
        return 0 

    min_words = float("inf")
    for word in words_list:
        if s.startswith(word):
            new_s = s[len(word):]
            attempt = 1 + _quickest_concat(new_s, words_list)
            min_words = min(min_words, attempt) 

    
    return min_words

# Optimized solution
def quickest_concat_memo(s, words_list):
    result = _quickest_concat_memo(s, words_list, {})
    if result == float("inf"):
        return -1 
    else:
        return result 

def _quickest_concat_memo(s, words_list, memo):
    if s in memo:
        return memo[s] 

    if len(s) == 0:
        return 0 

    min_words = float("inf")
    for word in words_list:
        if s.startswith(word):
            new_s = s[len(word):]
            attempt = 1 + _quickest_concat_memo(new_s, words_list, memo)
            min_words = min(min_words, attempt) 
    
    memo[s] = min_words 
    return min_words
            



# Driver code 
if __name__ == "__main__":
    # Test case 01
    print(quickest_concat('caution', ['ca', 'ion', 'caut', 'ut'])) # -> 2

    # Test case 02
    print(quickest_concat('caution', ['ion', 'caut', 'caution'])) # -> 1

    # Test case 03
    print(quickest_concat('respondorreact', ['re', 'or', 'spond', 'act', 'respond'])) # -> 4

    # Test case 04
    print(quickest_concat('simchacindy', ['sim', 'simcha', 'acindy', 'ch'])) # -> 3

    # Test case 05
    print(quickest_concat('simchacindy', ['sim', 'simcha', 'acindy'])) # -> -1

    # Test case 06
    print(quickest_concat('uuuuuu', ['u', 'uu', 'uuu', 'uuuu'])) # -> 2

    # Test case 07 
    print(quickest_concat('rongbetty', ['wrong', 'bet'])) # -> -1

    # Test case 08
    print(quickest_concat_memo('uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu', ['u', 'uu', 'uuu', 'uuuu', 'uuuuu'])) # -> 7