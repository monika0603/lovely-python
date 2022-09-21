""" 
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

def longest_substring(s):
    charSet = set() 
    l = 0
    result = 0 

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1 
        charSet.add(s[r])
        result = max(result, r-l+1) 

    return result 

if __name__ == "__main__":
    s = "abcabcbb"
    print(longest_substring(s))

    # Test case 02
    s = "bbbbb"
    print(longest_substring(s))

    # Test case 03
    s = "pwwkew"
    print(longest_substring(s))
