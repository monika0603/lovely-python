""" 
You are given an array of integers. On each move you are allowed to increase exactly one of its 
element by one. Find the minimal number of moves required to obtain a strictly increasing sequence 
from the input.

Example

For inputArray = [1, 1, 1], the output should be
solution(inputArray) = 3.

Algorithm:

1. If current <= previous 
2. Store current; x = current 
3. Update current += (previous - current) + 1 
4. Update count += current - x 
"""

def array_change(nums):

    first = nums[0]
    count = 0

    nums = sorted(nums)

    for i in range(1,len(nums)):
        if nums[i] <= nums[i-1]:
            x = nums[i] 
            nums[i] += (nums[i-1] - nums[i]) + 1 
            count += nums[i] - x 

    return count 

    

if __name__ == "__main__":
    nums = [1, 1, 1]
    print(array_change(nums))

