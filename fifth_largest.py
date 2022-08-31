
from collections import deque
def fifth_largest(numlists):

    input = []
    for list in numlists:
        list = merge_sort(list)
        input.append(list)

    print(input)

    output = [] 
    for list in input:
        output.append(list[-5])

    return output

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


numlists = [ [1,2,3,4,5], [3,1,2,5,4], [1,2,3,4,5,6,7], 
[99, 320, 400, 100.25, 55.2, 0.1] ]
print(fifth_largest(numlists))