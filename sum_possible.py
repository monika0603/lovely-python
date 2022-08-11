
def sum_possible(num, list_num):
    return _sum_possible(num, list_num, {}) 

def _sum_possible(target, list_num, memo):
    if target in memo:
        return memo[target]

    if target < 0:
        return False 

    if target == 0:
        return True 

    for number in list_num:
        if _sum_possible(target-number, list_num, memo) == True:
            memo[target] = True 
            return memo[target] 

    memo[target] = False
    return memo[target] 

# Driver code 
# Test case 01 
if __name__ == "__main__":
    print(sum_possible(8, [5, 12, 4])) # -> True, 4 + 4

    # Test case 02
    print(sum_possible(15, [6, 2, 10, 19])) # -> False

    # Test case 03
    print(sum_possible(13, [6, 2, 1])) # -> True

    # Test case 04
    print(sum_possible(103, [6, 20, 1])) # -> True

    # Test case 05
    print(sum_possible(12, [])) # -> False

    # Test case 06
    print(sum_possible(271, [10, 8, 265, 24])) # -> False