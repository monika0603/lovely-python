
# Brute force method
def max_path_sum(grid):
    row, col = 0, 0 
    return _max_path_sum(grid, row, col) 

def _max_path_sum(grid, row, col):

    if row == len(grid) or col == len(grid):
        return 0 

    if row == len(grid)-1 and col == len(grid[0])-1:
        return grid[row][col]

    sum_down = _max_path_sum(grid, row+1, col)
    sum_right = _max_path_sum(grid, row, col+1)

    return grid[row][col] + max(sum_down, sum_right)

# Memoization technique 

def max_path_sum_memo(grid):
    row, col = 0, 0
    return _max_path_sum_memo(grid, row, col, {}) 

def _max_path_sum_memo(grid, row, col, memo):
    pos = (row, col) 
    if pos in memo:
        return memo[pos] 

    if row == len(grid) or col == len(grid[0]):
        return 0 

    if row == len(grid)-1 and col == len(grid[0])-1:
        return grid[row][col] 

    count_down = _max_path_sum_memo(grid, row+1, col, memo)
    count_right = _max_path_sum_memo(grid, row, col+1, memo)

    memo[pos] = grid[row][col] + max(count_down, count_right)

    return memo[pos]

# Driver code 
# Test case 01 
if __name__ == "__main__":

    grid = [
    [1, 3, 12],
    [5, 1, 1],
    [3, 6, 1],
    ]
    print(max_path_sum(grid)) # -> 18

    # Test case 02
    grid = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
    print(max_path_sum_memo(grid)) # -> 27

    # Test case 03 
    grid = [
    [1, 1, 3, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 1, 1, 6, 1, 1, 5, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 5, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [2, 1, 1, 1, 1, 8, 1, 1, 1, 1, 1, 1, 1],
    [2, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 9, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
    print(max_path_sum_memo(grid)) # -> 56