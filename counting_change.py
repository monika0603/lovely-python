""" 
Write a function, counting_change, that takes in an amount and a list of coins. The function 
should return the number of different ways it is possible to make change for the given amount 
using the coins.

You may reuse a coin as many times as necessary.

For example,

counting_change(4, [1,2,3]) -> 4

There are four different ways to make an amount of 4:

1. 1 + 1 + 1 + 1
2. 1 + 1 + 2
3. 1 + 3
4. 2 + 2

However, what we don't want to do here is to count different permutations of 1,1,2 or similarly 1,3. 
So subtracting the coin from the target amount is not going to be the way to solve this problem. Instead
we want to instead count how many of different coins we can take. 

                                                4 
                     coin 1      0*1   / 1*1 / 2*1 \ 3*1 \ 4*1 \ 
                                      4     3      2      1     0 
                    coin 2   0*2/ 1*2| 2*2 \
                              4     2       0  
"""
# Brute force solution using recursion only
def counting_change(amount, coins):
    return _counting_change(amount, coins, 0) 

def _counting_change(amount, coins, i):
    if amount == 0:
        return 1 

    if i == len(coins):
        return 0 

    coin = coins[i] 
    total_ways = 0
    for qty in range(0, (amount//coin) + 1):
        remainder = amount - (qty*coin) 
        total_ways += _counting_change(remainder, coins, i+1)

    return total_ways 

# Optimized solution using memoization
def counting_change_memo(amount, coins):
    return _counting_change_memo(amount, coins, 0, {})

def _counting_change_memo(amount, coins, i, memo):
    key = (amount, i)
    if key in memo:
        return memo[key] 

    if amount == 0:
        return 1 

    if i == len(coins):
        return 0 

    coin = coins[i]
    total_ways = 0
    for qty in range(0, (amount//coin)+1):
        remainder = qty*coin 
        total_ways += _counting_change_memo(amount - remainder, coins, i+1, memo)

    memo[key] = total_ways
    return total_ways


# Driver code 
# Test case 01 
if __name__ == "__main__":
    print(counting_change(4, [1, 2, 3])) # -> 4
    print(counting_change_memo(4, [1, 2, 3])) # -> 4

    # Test case 02
    print(counting_change(8, [1, 2, 3])) # -> 10
    print(counting_change_memo(8, [1, 2, 3])) # -> 10

    # Test case 03
    print(counting_change(24, [5, 7, 3])) # -> 5 
    print(counting_change_memo(24, [5, 7, 3])) # -> 5 

    # Test case 04
    print(counting_change(13, [2, 6, 12, 10])) # -> 0
    print(counting_change_memo(13, [2, 6, 12, 10])) # -> 0

    # Test case 05 
    print(counting_change(512, [1, 5, 10, 25])) # -> 20119
    print(counting_change_memo(512, [1, 5, 10, 25])) # -> 20119

    # Test case 06 
    print(counting_change_memo(1000, [1, 5, 10, 25])) # -> 142511
