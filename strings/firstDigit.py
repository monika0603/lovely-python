""" 
Find the leftmost digit that occurs in a given string.

Example

For inputString = "var_1__Int", the output should be
solution(inputString) = '1';
For inputString = "q2q-q", the output should be
solution(inputString) = '2';
For inputString = "0ss", the output should be
solution(inputString) = '0'.
"""

def firstDigit(input):

    for i in input:
        if i.isdigit():
            return i 

if __name__ == "__main__":
    inputString = "var_1__Int"
    print(firstDigit(inputString))

    # Test case 01
    inputString = "q2q-q"
    print(firstDigit(inputString))

    # Test case 02
    inputString = "0ss"
    print(firstDigit(inputString))

