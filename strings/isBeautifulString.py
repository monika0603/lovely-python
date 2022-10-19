""" 
A string is said to be beautiful if each letter in the string appears at most as 
many times as the previous letter in the alphabet within the string; ie: b occurs 
no more times than a; c occurs no more times than b; etc. Note that letter a has 
no previous letter.

Given a string, check whether it is beautiful.
"""

from ssl import ALERT_DESCRIPTION_HANDSHAKE_FAILURE


def isBeautifulString1(input):

    count = {}
    letters = 'abcdefghijklmnopqrstuvwxyz'

    for i in range(len(input)):
        count[input[i]] = 1 + count.get(input[i], 0) 

    count = dict(sorted(count.items(), key=lambda x: x[0]))
    keys = list(count.keys())
    values = list(count.values())
    
    for key in keys:
        value = letters.index(key)
        print(value)

    output = True 
    for i in range(len(values)-1):
        if values[i+1] > values[i]: 
            output = False 

    return output    

def isBeautifulString(input):

    temp_dict = dict()
    letters = 'abcdefghijklmnopqrstuvwxyz' 

    for char in letters:
        temp_dict[char] = 0 
    
    for char in input:
        temp_dict[char] = 1 + temp_dict.get(char, 0) 
    
    previous = temp_dict['a'] 
    for char in letters:
        if temp_dict[char] > previous:
            return False 
        previous = temp_dict[char]

    return True 


if __name__ == "__main__":
    input = "bbbaacdafe"
    print(isBeautifulString(input)) 

    # Test case 01
    input = "aabbb"
    print(isBeautifulString(input)) 

    # Test case 02
    input = "bbc"
    print(isBeautifulString(input)) 

    # Test case 03
    input = "zaa"
    print(isBeautifulString(input)) 

    # Test case 04
    input = "bbbaacdafe"
    print(isBeautifulString(input)) 



