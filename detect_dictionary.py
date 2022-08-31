""" 
Write a function, detectDictionary, that takes in a dictionary of words and an alphabet string. 
The function should return a boolean indicating whether or not all words of the dictionary are 
lexically-ordered according to the alphabet.

You can assume that all characters are lowercase a-z.

You can assume that the alphabet contains all 26 letters.

Algorithm: 

1. Loop over the dictionary of words, and fetch two words 
2. For each of the two words selected, check if the order of the alphabets is correct according to 
the alphabet list provided.
3. Find any differing character and check their order in the alphabet. 
"""

def detect_dictionary(dictionary, alphabet):

    for i in range(len(dictionary)-1):
        word_1, word_2 = dictionary[i], dictionary[i+1]

        if not lexical_order(word_1, word_2, alphabet):
            return False 

    return True 

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
    dictionary = ["zoo", "tick", "tack", "door"]
    alphabet = "ghzstijbacdopnfklmeqrxyuvw"
    print(detect_dictionary(dictionary, alphabet)) # -> True

    # Test case 02
    dictionary = ["zoo", "tack", "tick", "door"]
    alphabet = "ghzstijbacdopnfklmeqrxyuvw"
    print(detect_dictionary(dictionary, alphabet)) # -> False

    # Test case 03
    dictionary = ["zoos", "zoo", "tick", "tack", "door"]
    alphabet = "ghzstijbacdopnfklmeqrxyuvw"
    print(detect_dictionary(dictionary, alphabet)) # -> False

    # Test case 04
    dictionary = ["miles", "milestone", "proper", "process", "goal"]
    alphabet = "mnoijpqrshkltabcdefguvwzxy"
    print(detect_dictionary(dictionary, alphabet)) # -> True 

    # Test case 05
    dictionary = ["miles", "milestone", "pint", "proper", "process", "goal"];
    alphabet = "mnoijpqrshkltabcdefguvwzxy"
    print(detect_dictionary(dictionary, alphabet)) # -> True 

    # Test case 06
    dictionary = ["miles", "milestone", "pint", "proper", "process","goal", "apple"];
    alphabet = "mnoijpqrshkltabcdefguvwzxy"
    print(detect_dictionary(dictionary, alphabet)) # -> False