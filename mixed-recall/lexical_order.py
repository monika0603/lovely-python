""" 
Write a function, lexical_order, that takes in 2 words and an alphabet string as an argument. The 
function should return True if the first word should appear before the second word if 
lexically-ordered according to the given alphabet order. If the second word should appear first, 
then return False.

Note that the alphabet string may be any arbitrary string.

Intuitively, Lexical Order is like "dictionary" order:

You can assume that all characters are lowercase a-z.

You can assume that the alphabet contains all 26 letters.

Algorithm: 
1. Find the character with max length and loop over the max length.
2. Look for each differing character and find their order in the dictionary provided. 
3. If the first word's character comes after in the second word's character in the 
dictionary then return False. 
4. If the opposite happens then return True. 
5. Edge case, if both words are the same then return True outside of the for loop. 
"""

def lexical_order(word_1, word_2, alphabet):
    max_length = max(len(word_1), len(word_2)) 

    for i in range(0, max_length):

        value_1 = alphabet.index(word_1[i]) if i < len(word_1) else float("-inf") 
        value_2 = alphabet.index(word_2[i]) if i < len(word_2) else float("-inf") 

        if value_1 < value_2:
            return True 
        elif value_2 < value_1:
            return False 

    return True 

if __name__ == "__main__":
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    print(lexical_order("apple", "dock", alphabet)) # -> True 

    # Test case 02
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    print(lexical_order("apple", "ample", alphabet)) # -> False

    # Test case 03
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    print(lexical_order("app", "application", alphabet)) # -> True

    # Test case 04
    alphabet = "ghzstijbacdopnfklmeqrxyuvw"
    print(lexical_order("semper", "semper", alphabet)) # -> True