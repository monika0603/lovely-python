""" 
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is 
not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""

def index_occurence(s1, s2):

    if not s1 or not s2:
        return -1 

    if s2 in s1:
        return s1.index(s2)

    else:
        return -1 

if __name__ == "__main__":
    s1 = "sadbutsad"
    s2 = "sad"
    print(index_occurence(s1, s2))

    # Test case 02
    s1 = "leetcode"
    s2 = "leeto"
    print(index_occurence(s1,s2))