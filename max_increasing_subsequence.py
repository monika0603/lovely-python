""" 
Write a function, max_increasing_subseq, that takes in a list of numbers as an argument. The 
function should return the length of the longest subsequence of strictly increasing numbers.

A subsequence of a list can be created by deleting any items of the list, while maintaining 
the relative order of items.

Algorithm: The logic will be built on whether to take the first number in the sequence or not. 
 
                         6,9,7,8
         (don't take) /            \ (take)
              9,7,8               6| 9,7,8
                        don't take 9  / \ take 9 
                                7,8       9 |7,8 

"""
# Brute force solution without memoization
def max_increasing_subseq(numbers):
    return _max_increasing_subseq(numbers, 0, float("-inf"))

def _max_increasing_subseq(numbers, i, previous):
    if i == len(numbers):
        return 0 

    current = numbers[i]
    order = []
    dont_take_current = _max_increasing_subseq(numbers, i+1, previous) 
    order.append(dont_take_current)

    if current > previous:
        take_current = 1 + _max_increasing_subseq(numbers, i+1, current)
        order.append(take_current)

    return max(order)

# Optimized solution with memoization
def max_increasing_subseq_memo(numbers):
    return _max_increasing_subseq_memo(numbers, 0, float("-inf"), {})


def _max_increasing_subseq_memo(numbers, i, previous, memo):
    key = (i, previous)
    if key in memo:
        return memo[key] 

    if i == len(numbers):
        return 0 

    current = numbers[i] 
    order = []
    dont_take_current = _max_increasing_subseq_memo(numbers, i+1, previous, memo) 
    order.append(dont_take_current)

    if current > previous:
        take_current = 1 + _max_increasing_subseq_memo(numbers, i+1, current, memo)
        order.append(take_current)

    memo[key] = max(order)
    return max(order)

# Driver code 
if __name__ == "__main__":
    # Test case 01
    numbers = [4, 18, 20, 10, 12, 15, 19]
    print(max_increasing_subseq_memo(numbers))

    # Test case 02
    numbers = [12, 9, 2, 5, 4, 32, 90, 20]
    print(max_increasing_subseq_memo(numbers)) # -> 4    

    # Test case 03
    numbers = [42, 50, 51, 60, 55, 70, 4, 5, 70]
    print(max_increasing_subseq_memo(numbers)) # -> 5   

    # Test case 04
    numbers = [7, 14, 10, 12]
    print(max_increasing_subseq_memo(numbers)) # -> 3

    # Test case 05
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    print(max_increasing_subseq_memo(numbers)) # -> 21

    # Test case 06
    numbers = [
    1, 2, 3, 4, 5, 12, 6, 30, 7, 8, 9, 10, 11, 12, 13, 10, 18, 14, 15, 16, 17, 18, 19, 20, 21, 100,
    104,
    ]
    print(max_increasing_subseq_memo(numbers)) # -> 23

    # Test case 07
    numbers = [
    1, 2, 300, 3, 4, 305, 5, 12, 6, 30, 7, 8, 9, 10, 10, 10, 15, 11, 12, 13, 10, 18, 14, 15, 16,
    17, 18, 19, 20, 21, 100,101 ,102, 103, 104, 105
    ]
    print(max_increasing_subseq_memo(numbers)) # -> 27
