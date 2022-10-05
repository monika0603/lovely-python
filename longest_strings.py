""" 
Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
solution(inputArray) = ["aba", "vcd", "aba"].
"""

def longest_string(input):

    string_length = set()
    for string in input:
        string_length.add(len(string)) 

    max_length = max(string_length)
    output = [] 
    for string in input:
        if len(string) == max_length:
            output.append(string) 

    return output 

if __name__ == "__main__":
    input = ["aba", "aa", "ad", "vcd", "aba"]
    print(longest_string(input))