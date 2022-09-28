""" 
Write a function, befitting_brackets, that takes in a string as an argument. The function should return a 
boolean indicating whether or not the string contains correctly matched brackets.

You may assume the string contains only characters: ( ) [ ] { }
"""

def befitting_brackets(s):

    open_to_close = { 
        '(':')',
        '{':'}',
        '[':']'
    }

    open_set = set(['(', '{', '['])

    stack = [] 
    for character in s:
        if character in open_set:
            stack.append(character)
        else:
            if len(stack) and open_to_close[stack[-1]] == character:
                stack.pop() 
            else:
                return False 

    if len(stack):
        return False 
    return True 

if __name__ == "__main__":
    print(befitting_brackets('(){}[](())')) # -> True

    # Test case 02
    print(befitting_brackets('({[]})')) # -> True 

    # Test case 03
    print(befitting_brackets('[][}')) # -> False

    # Test case 04
    print(befitting_brackets('{[]}({}')) # -> False

    # Test case 05
    print(befitting_brackets('[]{}(}[]')) # -> False 

    # Test case 06
    print(befitting_brackets('[]{}()[]')) # -> True


                

