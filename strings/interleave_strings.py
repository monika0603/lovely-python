""" 
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m non-empty substrings respectively, 
such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

 

Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.

Algorithm:

1. Check if the length of s1 + s2 = s3, otherwise return False 
2. Create three pointers, and initialize them to zero
3. Create a boolean variable that is going to store False to begin with 
4. First: if i1 < len(s1) and s3[i3] == s1[i1] then update found if the recursive call returns True when pointers are incremented. 
5. Second, if i2 < len(s2) and s3[i3] == s2[i2] then update found if the recursive call returns True when pointers are incremented
"""


def interleaving(s1, s2, s3):

    if len(s1) + len(s2) != len(s3):
        return False 

    return _interleaving(s1, s2, s3, 0, 0, 0)

def _interleaving(s1, s2, s3, i1, i2, i3):
    if i3 == len(s3):
        return True 

    found = False 
    if i1 < len(s1) and s3[i3] == s1[i1]:
        found = found or _interleaving(s1, s2, s3, i1+1, i2, i3+1)
    if i2 < len(s2) and s3[i3] == s2[i2]:
        found = found or _interleaving(s1, s2, s3, i1, i2+1, i3+1)

    return found 

if __name__ == "__main__":

    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(interleaving(s1,s2,s3))

    # Test case 01 
    s1 = "" 
    s2 = "" 
    s3 = ""
    print(interleaving(s1,s2,s3))
