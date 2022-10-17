""" 
Given a string, find the number of different characters in it.

Example

For s = "cabca", the output should be
solution(s) = 3.

There are 3 different characters a, b and c.
"""

def differentSymbolsNaive(s):

    count_s = {}

    for i in range(len(s)):
        count_s[s[i]] = 1 + count_s.get(i, 0) 

    return len(count_s)
     
if __name__ == "__main__":
    s = "cabca"
    print(differentSymbolsNaive(s))
