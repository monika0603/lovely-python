""" 
Given array of integers, find the maximal possible sum of some of its k 
consecutive elements.

Example

For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
solution(inputArray, k) = 8.
All possible sums of 2 consecutive elements are:

2 + 3 = 5;
3 + 5 = 8;
5 + 1 = 6;
1 + 6 = 7.
Thus, the answer is 8.

Algorithm: 
1. Take the sum of k elements 
2. Add the last element to the sum and remove the first 
3. Check for max

"""

def consecutive_Sum(nums, k):
    n = len(nums)

    # compute the sum of first window of size k 
    res = 0 
    for i in range(k):
        res += nums[i] 

    # Compute sums of remaining windows by removing 
    # first element of previous window and adding last 
    # element of current window. 
    curr_sum = res 
    for i in range(k, n):
        curr_sum += nums[i] - nums[i-k]
        res = max(res, curr_sum)

    return res 


if __name__ == "__main__":
    nums = [2,3,5,1,6]
    print(consecutive_Sum(nums, 2))

    # Test case 01
    nums = [1,3,2,4]
    print(consecutive_Sum(nums, 3))