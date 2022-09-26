""" 
Write a function, compress, that takes in a string as an argument. The function should return a compressed version of the 
string where consecutive occurrences of the same characters are compressed into the number of occurrences followed by the 
character. Single character occurrences should not be changed.

'aaa' compresses to '3a'
'cc' compresses to '2c'
't' should remain as 't'
"""

def compress(s):
    s += '!'
    result = ''
    i = j = 0 

    while j < len(s):
        if s[i] == s[j]:
            # I am on a streak of consecutive letters
            j += 1 
        else:
            num = j-i 
            if num == 1:
                result += s[i]
            else:
                result += str(num) + s[i]
            i = j 

    return result

if __name__ == "__main__":
    print(compress('ccaaatsss'))

    # Test case 01
    print(compress('ssssbbz')) # -> '4s2bz'

    # Test case 02
    print(compress('ppoppppp')) # -> '2po5p'

    # Test case 03
    print(compress('nnneeeeeeeeeeeezz')) # -> '3n12e2z' 

    # Test case 04
    print(compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')) 
    # -> '127y'