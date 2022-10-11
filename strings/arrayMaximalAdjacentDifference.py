""" 
Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

Example

For inputArray = [2, 4, 1, 0], the output should be
solution(inputArray) = 3.
"""

def difference(nums):

    max_diff = float("-inf")
    
    for i in range(len(nums)-1):
        diff = abs(nums[i] - nums[i+1])
        max_diff = max(max_diff, diff) 

    return max_diff 

if __name__ == "__main__":
    nums = [2,4,1,0]
    print(difference(nums))
