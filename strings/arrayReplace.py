""" 
Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.

Example

For inputArray = [1, 2, 1], elemToReplace = 1, and substitutionElem = 3, the output should be
solution(inputArray, elemToReplace, substitutionElem) = [3, 2, 3].
"""

def array_replace(nums, elemToReplace, substitutionElem):

    output = []

    for num in nums:
        if num == elemToReplace:
            output.append(substitutionElem)
        else:
            output.append(num)

    return output 

if __name__ == "__main__":
    nums = [1,2,1]
    elemToReplace = 1
    substitutionElem = 3 
    print(array_replace(nums, elemToReplace, substitutionElem))

