""" 
Write a function, decompress_braces, that takes in a compressed string as an argument. The function 
should return the string decompressed.

The compression format of the input string is 'n{sub_string}', where the sub_string within braces 
should be repeated n times.

You may assume that every number n is guaranteed to be an integer between 1 through 9.

You may assume that the input is valid and the decompressed string will only contain alphabetic characters.
"""

def decompress_braces(string):
  
    num = 0
    output = []
    open_set = set(['{'])
    close_set = set(['}'])
    letters = 'abcdefghijklmnopqrstuvwxyz'
  
    s = ''
    s1 = ''
    for i in range(len(string)):
        if string[i] in letters:
            s1 += string[i]
        if string[i] in open_set:
            left = 0
            right = 0 
            num = int(string[i-1])
        if string[i] in letters:
            s += string[i]
            right += 1 
        if string[i] in close_set:
            output.append(s[0:right+1]*num)
            s = ''
    print(string.index(s1))         
    return "".join(output) 

print(decompress_braces("2{q}3{tu}v"))
      