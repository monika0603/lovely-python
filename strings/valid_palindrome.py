""" 
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric 
characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

    

def valid_palindrome(s):

    s = s.lower()
    a = set('abcdefghijklmnopqrstuvwxyz0123456789')
    left = 0
    right = len(s)-1 

    while left<right:
        if s[left] not in a:
            left += 1 
            continue 
        if s[right] not in a:
            right -= 1
            continue 
        if s[left] != s[right]:
            return False 
        left += 1
        right -= 1

    return True 
        

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(valid_palindrome(s))

    # Test case 01
    s = "race a car"
    print(valid_palindrome(s))

    # Test case 02
    s = ""
    print(valid_palindrome(s))