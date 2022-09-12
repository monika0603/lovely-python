""" 
Write an efficient program for printing k largest elements in an array. Elements in an array can be in any order.
For example: if the given array is [1, 23, 12, 9, 30, 2, 50] and you are asked for the largest 3 elements i.e., k = 3 
then your program should print 50, 30, and 23.
"""
from collections import deque 
def k_largest(nums):
    if len(nums) <= 1:
        return nums 

    mid = len(nums)//2 
    left_sorted = k_largest(nums[:mid])
    right_sorted = k_largest(nums[mid:])

    return merge_sort(left_sorted, right_sorted)
    
def merge_sort(left, right):
    left_1 = deque(left)
    right_1 = deque(right)

    merged = [] 

    while left_1 and right_1:
        if left_1[0] < right_1[0]:
            merged.append(left_1.popleft())
        else:
            merged.append(right_1.popleft())

    merged += left_1 
    merged += right_1 

    return merged 

if __name__ == "__main__":
    nums = [1, 23, 12, 9, 30, 2, 50]
    output = k_largest(nums)
    print(output[-3:])