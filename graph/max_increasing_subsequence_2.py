""" 
Algorithm:

1. For the first number, the lower limit is float("-inf") and we have a choice of taking/not taking the first number. 
2. We will continue to shorten the input list based on the previous choice. 
3. If we do take the previous number, then the condition we have to meet is that next number must be larger than the 
current number. 

Complexity: 
Time complexity: 2^n where n is the length of the list 
With memoization, we can reduce it to 
"""

# Brute force solution
def max_increasing_subsequence(numbers):
    # 0 represents the index where we want to start in the input list. We want to avoid slicing the list, so 
    # passing the index 
    return _max_increaseing_subsequence(numbers, 0, float("-inf")) 

def _max_increaseing_subsequence(numbers, i, previous):
    # Base case
    if i == len(numbers):
        return 0 

    current = numbers[i]
    options = [] 

    # if you don't take the current number, your previous doesn't change
    dont_take_current = _max_increaseing_subsequence(numbers, i+1, previous) 
    options.append(dont_take_current)

    if current > previous:
        take_current = 1 + _max_increaseing_subsequence(numbers, i+1, current)
        options.append(take_current) 

    return max(options)

# Optimized solution
def max_increasing_subseq(numbers):
    return _max_increasing_subseq(numbers, 0, float("-inf"), {}) 

def _max_increasing_subseq(numbers, i, previous, memo):
    key = (i, previous)
    if key in memo:
        return memo[key] 

    if i == len(numbers):
        return 0 

    current = numbers[i]
    options = [] 

    dont_take_current = _max_increasing_subseq(numbers, i+1, previous, memo)
    options.append(dont_take_current)

    if current > previous:
        take_current = 1 + _max_increasing_subseq(numbers, i+1, current, memo)
        options.append(take_current) 

    memo[key] = max(options)
    return max(options) 

if __name__ == "__main__":
    numbers = [4, 18, 20, 10, 12, 15, 19]
    print(max_increasing_subseq(numbers)) # -> 5

    # Test case 01 
    numbers = [12, 9, 2, 5, 4, 32, 90, 20]
    print(max_increasing_subseq(numbers)) # -> 4

    # Test case 02
    numbers = [42, 50, 51, 60, 55, 70, 4, 5, 70]
    print(max_increasing_subseq(numbers)) # -> 5

    # Test case 03
    numbers = [7, 14, 10, 12]
    print(max_increasing_subseq(numbers)) # -> 3

    # Test case 04
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    print(max_increasing_subseq(numbers)) # -> 21

    # Test case 05
    numbers = [
    1, 2, 3, 4, 5, 12, 6, 30, 7, 8, 9, 10, 11, 12, 13, 10, 18, 14, 15, 16, 17, 18, 19, 20, 21, 100,
    104,
    ]
    print(max_increasing_subseq(numbers)) # -> 23 

    # Test case 06
    numbers = [
    1, 2, 300, 3, 4, 305, 5, 12, 6, 30, 7, 8, 9, 10, 10, 10, 15, 11, 12, 13, 10, 18, 14, 15, 16,
    17, 18, 19, 20, 21, 100,101 ,102, 103, 104, 105
    ]
    print(max_increasing_subseq(numbers)) # -> 27