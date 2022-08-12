# Time complexity of O(2^n) where n = len(nums)
# Space complexity: O(n)

# Brute force solution
def non_adjacent_sum(nums):
    return _non_adjacent_sum(nums) 

def _non_adjacent_sum(nums):
    if len(nums) == 0:
        return 0 

    include = nums[0] + _non_adjacent_sum(nums[2:])
    exclude = _non_adjacent_sum(nums[1:])

    return max(include, exclude)

# Brute force solution without slicing the list
def non_adjacent_sum_1(nums):
    return _non_adjacent_sum_1(nums, 0)

def _non_adjacent_sum_1(nums, i):
    if i >= len(nums):
        return 0 

    include = nums[i] + _non_adjacent_sum_1(nums, i + 2)
    exclude = _non_adjacent_sum_1(nums, i + 1)

    return max(include, exclude)

# Optimized solution using memoization 
def non_adjacent_sum_2(nums):
    return _non_adjacent_sum_2(nums, 0, {})

def _non_adjacent_sum_2(nums, i, memo):
    if i >= len(nums):
        return 0 
    if nums[i] in memo:
        return memo[nums[i]] 

    include = nums[i] + _non_adjacent_sum_2(nums, i + 2, memo)
    exclude = _non_adjacent_sum_2(nums, i + 1, memo)

    memo[nums[i]] = max(include, exclude)

    return memo[nums[i]]

# Driver code 
# Test case 01
if __name__ == "__main__":
    nums = [2, 4, 5, 12, 7]
    print(non_adjacent_sum_2(nums)) # -> 16

    # Test case 02
    nums = [7, 5, 5, 12]
    print(non_adjacent_sum_2(nums)) # -> 19

    # Test case 03 
    nums = [7, 5, 5, 12, 17, 29]
    print(non_adjacent_sum_2(nums)) # -> 48

    # Test case 04
    nums = [
    72, 62, 10,  6, 20, 19, 42,
    46, 24, 78, 30, 41, 75, 38,
    23, 28, 66, 55, 12, 17, 9,
    12, 3, 1, 19, 30, 50, 20
    ]
    print(non_adjacent_sum_2(nums)) # -> 488

    # Test case 05
    nums = [
    72, 62, 10,  6, 20, 19, 42, 46, 24, 78,
    30, 41, 75, 38, 23, 28, 66, 55, 12, 17,
    83, 80, 56, 68,  6, 22, 56, 96, 77, 98,
    61, 20,  0, 76, 53, 74,  8, 22, 92, 37,
    30, 41, 75, 38, 23, 28, 66, 55, 12, 17,
    72, 62, 10,  6, 20, 19, 42, 46, 24, 78,
    42
    ]
    print(non_adjacent_sum_2(nums)) # -> 1465

