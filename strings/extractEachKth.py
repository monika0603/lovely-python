""" 
Given array of integers, remove each kth element from it.

Example

For inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and k = 3, the output should be
solution(inputArray, k) = [1, 2, 4, 5, 7, 8, 10].

"""

def extract(nums, k):

    sum = 0 
    remove = []
    output = []
    
    while sum+k <= max(nums):
        sum += k
        remove.append(sum-1)

    for i in range(len(nums)):
        if i in remove:
            pass 
        else:
            output.append(nums[i])

    return output 

def extract1(nums, k):

    for i in range(len(nums)-1, -1, -1):
        print(i, k, i%k, k-1)
        if i%k == k-1:
            del nums[i]
    return nums 

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 3 
    print(extract1(nums, k))

    # Test case 01
    nums = [1, 2, 1, 2, 1, 2, 1, 2]
    print(extract1(nums, k))

