""" 
Given a string, return its encoding defined as follows:

First, the string is divided into the least possible number of disjoint substrings 
consisting of identical characters
for example, "aabbbc" is divided into ["aa", "bbb", "c"]
Next, each substring with length greater than one is replaced with a concatenation 
of its length and the repeating character
for example, substring "bbb" is replaced by "3b"
Finally, all the new strings are concatenated together in the same order and a new 
string is returned.
Example

For s = "aabbbc", the output should be
solution(s) = "2a3bc".
"""

def compress(s):

    i = 0
    j = 1 
    count = 1 
    result = [] 

    while j < len(s):
        if s[i] == s[j]:
            count += 1
            i += 1  
            j += 1
        else:
            if count > 1:
                result.append(str(count))
            result.append(s[i]) 
            i += 1
            j += 1
            count = 1 

    if count > 1:
        result.append(str(count))
    result.append(s[i])
    
    return "".join(result) 

if __name__ == "__main__":
    s = "aabbbc"
    print(compress(s))