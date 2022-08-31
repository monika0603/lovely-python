""" 
Write a function, max_value, that takes in list of numbers as an argument. 
The function should return the largest number in the list.
"""

def largest(nums):
    if len(nums) <= 1:
        return nums 

    max_value = float("-inf")
    for num in nums:
        max_value = max(num, max_value)

    return max_value 

if __name__ == "__main__":
    nums = [4,7,2,8,10,9]
    print(largest(nums))  