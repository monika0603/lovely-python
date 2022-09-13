""" 
Given an integer array, find the next greater element for every array element. The next greater element of a number x is the first 
greater number to the right of x in the array.

Input:  [2, 7, 3, 5, 4, 6, 8]
Output: [7, 8, 5, 6, 6, 8, -1]

Algorithm: 
1. j > i and A[j] > A[i]
"""
# Brute force solution
def next_greater_element(nums):
    if len(nums) <= 1:
        return nums 

    output = [-1]*len(nums)
    print(output)
    for i in range(len(nums)):
        next = -1 
        for j in range(i+1, len(nums)):
            if nums[j] > nums[i]:
                next = nums[j]
                output.insert(i, next)
                break 
    
    return output
""" 
# Optimized solution
# Rules for pushing to the stack
1. If the stack is empty, push the first element and continue to push additional elements as long as they are smaller than the 
first element pushed. 
2. As soon as we find an element greater than previously pushed elements, we have found the next greater element. So we pop that 
value.  

""" 
from collections import deque 
def findNextGreater(nums):
    if len(nums) <= 1:
        return nums 

    result = [-1]*len(nums)

    s = [] 

    for i in range(len(nums)):

        while s and nums[s[-1]] < nums[i]:
            result[s[-1]] = nums[i]
            s.pop()

        s.append(i)
    return result

if __name__ == "__main__":
    nums = [2, 7, 3, 5, 4, 6, 8]
    #print(next_greater_element(nums))

    print(findNextGreater(nums))