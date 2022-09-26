""" 
Write a function, uncompress, that takes in a string as an argument. The input string will be formatted into multiple groups 
according to the following pattern:

<number><char>

for example, '2c' or '3a'.
The function should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times 
consecutively. You may assume that the input string is well-formed according to the previously mentioned pattern.
"""

def uncompress(s):

    result = ''
    i = j = 0 
    numbers = '0123456789'

    while j < len(s):
        if s[j] in numbers:
            j += 1 
        else:
            num = int(s[i:j]) 
            result += s[j]*num 
            j += 1 
            i = j 
    return result 


if __name__ == "__main__":
    print(uncompress("2c3a1t")) # -> 'ccaaat'

    # Test case 01
    print(uncompress("4s2b")) # -> 'ssssbb'