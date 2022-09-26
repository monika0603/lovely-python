""" 
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

def common_prefix(strs):

    result = ""
    # Takes the first word and iterates over the length of the first word
    for i in range(len(strs[0])):
        # Loops over each word in the list
        for s in strs:
            if i==len(s) or s[i] != strs[0][i]:
                return result
        result +=strs[0][i]
    return result


if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    print(common_prefix(strs)) 

    # Test case 02
    strs = ["dog","racecar","car"]
    print(common_prefix(strs))

    # Test case 03
    strs = ['dig', 'dog']
    print(common_prefix(strs))