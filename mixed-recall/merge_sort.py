
from collections import deque 
def merge_sort(nums):
    if len(nums) <= 1:
        return nums 

    mid = len(nums)//2 
    left_sorted = merge_sort(nums[:mid])
    right_sorted = merge_sort(nums[mid:])

    return merge(left_sorted, right_sorted)

def merge(left, right):

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
    numbers = [10, 4, 42, 5, 8, 100, 5, 6, 12, 40]
    print(merge_sort(numbers))
    # -> [ 4, 5, 5, 6, 8, 10, 12, 40, 42, 100 ] 

    # Test case 01
    numbers = [7] * 120000
    print(merge_sort(numbers))
    # -> [7, 7, 7, 7, 7, ...]

    # Test case 02
    numbers = [7] * 95000
    print(merge_sort(numbers))
    # -> [7, 7, 7, 7, 7, ...]