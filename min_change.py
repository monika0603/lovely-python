
def min_change(target, num_list):
    result = _min_change(target, num_list, {}) 
    if result == float("inf"):
        return -1 
    else:
        return result 

def _min_change(target, num_list, memo):
    if target in memo:
        return memo[target]

    if target < 0:
        return float("inf")

    if target == 0:
        return 0

    min_change = float("inf")
    for num in num_list:
        attempt = 1 + _min_change(target-num, num_list, memo)
        min_change = min(min_change, attempt) 

    memo[target] = min_change 
    return memo[target]

# Driver code
# Test case 01
if __name__ == "__main__":
    print(min_change(8, [1, 5, 4, 12])) # -> 2

    # Test case 02 
    print(min_change(13, [1, 9, 5, 14, 30])) # -> 5

    # Test case 03 
    print(min_change(23, [2, 5, 7])) # -> 4 

    # Test case 04
    print(min_change(102, [1, 5, 10, 25])) # -> 6

    # Test case 05
    print(min_change(200, [1, 5, 10, 25])) # -> 8

    # Test case 06 
    print(min_change(2017, [4, 2, 10])) # -> -1

    # Test case 07
    print(min_change(271, [10, 8, 265, 24])) # -> -1