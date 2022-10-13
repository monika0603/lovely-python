""" 
Correct variable names consist only of English letters, digits and underscores and they can't start 
with a digit.

Check if the given string is a correct variable name.

Example

For name = "var_1__Int", the output should be
solution(name) = true;
For name = "qq-q", the output should be
solution(name) = false;
For name = "2w2", the output should be
solution(name) = false.

"""

def variableName(input):

    for i, s in enumerate(input):
        if i == 0 and s.isdigit():
            return False 
        if (s == '-') or (s == '[') or (s == ' '):
            return False 

    return True 

if __name__ == "__main__":
    input = "2w2"
    print(variableName(input))

    # Test case 01
    input = "qq-q"
    print(variableName(input))

    # Test case 02
    input = "var_1__Int"
    print(variableName(input))
