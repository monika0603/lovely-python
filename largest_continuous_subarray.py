""" 
Problem: Given an integer array, find the sum of the largest continuous subarray within the array. 
For example if the input is [-1, 3, 5, -4, 3, -6, 9, 2], then return 11 (because of [9, 2]). Note 
that is all the elements are negative, you should return 0.
"""

def largest_sum(nums):

    if len(nums) <= 1:
        return nums 

    max_sum = 0 
    current_sum = 0 

    for num in nums:
        current_sum += num 
        max_sum = max(current_sum, max_sum)

    return max_sum 

if __name__ == "__main__":
    nums = [-1, 3, 5, -4, 3, -6, 9, 2]
    print(largest_sum(nums))

    # Test case 01
    nums = [-1, -2, -3, -4, -5, -6]
    print(largest_sum(nums))