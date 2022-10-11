""" 
Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
solution(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.

# ord returns the number representing the unicode code of a specified character 
"""

def palindrome(s):

    count = [0]*256 

    for i in range(0, len(s)):
        count[ord(s[i])] = 1 + count[ord(s[i])]  

    odd = 0 

    for i in range(0, 256):
        if (count[i] & 1):
            odd += 1 
        
        if odd > 1:
            return False 

    return True 


if __name__ == "__main__":
    s = "aabb"
    print(palindrome(s))

