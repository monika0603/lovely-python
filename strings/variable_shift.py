""" 
Given a string, your task is to replace each of its characters by the next one in the English alphabet; 
i.e. replace a with b, replace b with c, etc (z would be replaced by a).

Example

For inputString = "crazy", the output should be solution(inputString) = "dsbaz".
"""

def variable_shift(input):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    output = ''
    for i in range(len(input)):
        value = alphabet.index(input[i])
        if value == len(alphabet)-1:
            value = alphabet.index('a')
            output += alphabet[value]
        else:
            output += alphabet[value+1]
        
    return output 

if __name__ == "__main__":
    input = 'crazy'
    print(variable_shift(input))


