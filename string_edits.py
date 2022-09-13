""" 
Given two strings str1 and str2 and below operations that can be performed on str1. Find minimum number of edits (operations) 
required to convert ‘str1’ into ‘str2’.  

Insert
Remove
Replace
All of the above operations are of equal cost. 

Input:   str1 = “geek”, str2 = “gesek”
Output:  1
Explanation: We can convert str1 into str2 by inserting a ‘s’.

Algorithms: 

1. Instead of string slicing, use variables that help to check if the characters are equal or not 
2. Count the number of overlaping characters 
3. Take difference between overlaping count and len(str1). 
"""

def overlap_subsequence(s1, s2):
    result = _overlap_subsequence(s1, s2, 0, 0)

    max_length = max(len(s1), len(s2))

    return max_length - result

def _overlap_subsequence(s1, s2, i, j):

    if i == len(s1) or j == len(s2):
        return 0 

    if s1[i] == s2[j]:
        return 1 + _overlap_subsequence(s1, s2, i+1, j+1)
    else:
        return max(_overlap_subsequence(s1, s2, i+1, j), _overlap_subsequence(s1, s2, i, j+1))

if __name__ == "__main__":
    str1 = 'geek'
    str2 = 'gesek'
    print(overlap_subsequence(str1, str2))

    # Test case 01 
    str1 = 'cat'
    str2 = 'cut'
    print(overlap_subsequence(str1, str2))

    # Test case 02 
    str1 = "sunday"
    str2 = "saturday"
    print(overlap_subsequence(str1, str2))

    