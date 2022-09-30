""" 
Write a function, decompress_braces, that takes in a compressed string as an argument. The function 
should return the string decompressed.

The compression format of the input string is 'n{sub_string}', where the sub_string within braces 
should be repeated n times.

You may assume that every number n is guaranteed to be an integer between 1 through 9.

You may assume that the input is valid and the decompressed string will only contain alphabetic characters.
"""

def decompress_braces(string):
    
    number_chars = '123456789'
    stack = [] 
    for char in string:
        if char in number_chars:
            stack.append(int(char)) 
        else:
            if char == '}':
                segment = ''
                while not isinstance(stack[-1], int):
                    popped = stack.pop()
                    segment = popped + segment
                num = stack.pop()
                stack.append(segment*num)
                
            elif char != '{':
                stack.append(char)

    return "".join(stack)
    
if __name__ == "__main__":
    print(decompress_braces("2{q}3{tu}v")) # -> qqtututuv 

    # Test case 01
    print(decompress_braces("ch3{ao}")) # -> chaoaoao 

    # Test case 02
    print(decompress_braces("2{y3{o}}s"))
    # -> yoooyooos
      