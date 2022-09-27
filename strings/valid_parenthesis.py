""" 
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""


""" 
Algorithm:
1. Create a dictionary which has open brackets as key and closed brackets as values
2. Create a set with only open brackets
3. Loop over each character in the given string. 
4. Define an empty stack
5. If you encounter the character is in open bracket set, append to the stack.
6. Else, check if the length of the stack is finite and if top of the stack matches with the closing bracket of the dictionary. 
If true, pop the element of the stack
7. Within the current statement, return False imeediately if 6. is not fulfilled. 
8. Outside of the for, check if the length of the stack is still non-zero. If true return False. Otherwise return True 
"""
def valid_parenthesis(s):

    open_to_close = {
        '(' : ')',
        '[' : ']',
        '{' : '}'
    }

    open_set = set(['(', '[', '{'])
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
    s = "()"
    print(valid_parenthesis(s)) 

    # Test case 01
    s = "()[]{}"
    print(valid_parenthesis(s)) 

    # Test case 02
    s = "(]"
    print(valid_parenthesis(s)) 