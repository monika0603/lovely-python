""" 
Write a function, summing_squares, that takes a target number as an argument. The function 
should return the minimum number of perfect squares that sum to the target. A perfect square 
is a number of the form (i*i) where i >= 1.

For example: 1, 4, 9, 16 are perfect squares, but 8 is not perfect square.

Given 12:

summing_squares(12) -> 3

The minimum squares required for 12 is three, by doing 4 + 4 + 4.

Another way to make 12 is 9 + 1 + 1 + 1, but that requires four perfect squares.
"""

# Brute force solution of using recursion
import math 
def summing_squares(n):

    if n == 0:
        return 0 

    min_squares = float("inf")
    for i in range(1, math.floor(math.sqrt(n))+1):
        square = i*i
        attempt = 1 + summing_squares(n - square) 
        min_squares = min(attempt, min_squares)

    return min_squares

# Optimized solution using memoization
def summing_squares_memo(n):
    return _summing_squares_memo(n, {})

def _summing_squares_memo(n, memo):
    if n in memo:
        return memo[n] 

    if n == 0:
        return 0 

    min_squares = float("inf")

    for i in range(1, math.floor(math.sqrt(n))+1):
        square = i*i 
        attempt = 1 + _summing_squares_memo(n-square, memo)
        min_squares = min(min_squares, attempt) 

    memo[n] = min_squares
    return min_squares

# Driver code 
# Test case 01 
if __name__ == "__main__":
    print(summing_squares(12)) # -> 3
    print(summing_squares_memo(12))

    # Test case 02 
    print(summing_squares(8)) # -> 2
    print(summing_squares_memo(8))

    # Test case 03
    print(summing_squares(9)) # -> 1
    print(summing_squares_memo(9))

    # Test case 04
    print(summing_squares(31)) # -> 4
    print(summing_squares_memo(31))

    # Test case 05
    print(summing_squares(50)) # -> 2
    print(summing_squares_memo(50))