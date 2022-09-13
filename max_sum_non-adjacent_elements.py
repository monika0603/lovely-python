""" 
Given an array arr[] of positive numbers, the task is to find the maximum sum of a subsequence with the constraint that no 2 
numbers in the sequence should be adjacent in the array.

nput: arr[] = {5, 5, 10, 100, 10, 5}
Output: 110
Explanation: Pick the subsequence {5, 100, 5}.
The sum is 110 and no two elements are adjacent. This is the highest possible sum.

Algorithm: 
1. Loop over the length of numbers and initialize a sum 
1. Create a pointer that increases by 2, 
"""

def max_sum(numbers):
    return _max_sum(numbers, 0, previous=float("-inf"))

def _max_sum(numbers, i, previous):
    if i == len(numbers):
        return 0 

    # recur by excluding the current element
    excl = _max_sum(numbers, i+1, previous) 

    incl = 0 
    if previous + 1 != i:
        print((previous+1), i)
        incl = _max_sum(numbers, i+1, i) + numbers[i] 

    return max(excl, incl) 

if __name__ == "__main__":
    nums = [1, 2, 9, 4, 5, 0, 4, 11, 6]
    print(max_sum(nums))

    # Test case 01
    nums = [5, 5, 10, 100, 10, 5]
    print(max_sum(nums))