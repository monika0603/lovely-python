""" 
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
solution(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".
"""

def overlapping_char(s1, s2):

    count_s1 = {} 
    count_s2 = {} 

    for char in s1:
        count_s1[char] = 1 + count_s1.get(char, 0)
    
    for char in s2:
        count_s2[char] = 1 + count_s2.get(char, 0) 

    overlap = [key for key in count_s1 if key in count_s2]

    result = 0
    for char in overlap:
        if count_s1[char] < count_s2[char]:
            result += count_s1[char] 
        else:
            result += count_s2[char]

    return result 

if __name__ == "__main__":
    s1 = 'aabcc'
    s2 = 'adcaa'
    print(overlapping_char(s1, s2))