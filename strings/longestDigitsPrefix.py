""" 
Given a string, output its longest prefix which contains only digits.

Example

For inputString = "123aa1", the output should be
solution(inputString) = "123".
"""

def digitPrefix(input):

    output = ''

    for i in input:
        if i.isdigit():
            output += i 
        else:
            output += '-'

    output = output.split('-')

    length = []
    for i, n in enumerate(output):
        length.append(len(n))

    max_length = max(length)

    for i in output:
        if max_length == len(i):
            return "".join(i) 

    


if __name__ == "__main__":
    input = "123aa1"
    print(digitPrefix(input))