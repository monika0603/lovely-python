
def count_paths(grid):
    return _count_paths(grid, 0, 0, {}) 

def _count_paths(grid, row, col, memo):

    pos = (row, col)
    if pos in memo:
        return memo[pos]

    if row == len(grid) or col == len(grid[0]) or grid[row][col] == 'X':
        return 0 

    if row == len(grid)-1 and col == len(grid[0])-1:
        return 1 

    count_down = _count_paths(grid, row+1, col, memo)
    count_right = _count_paths(grid, row, col+1, memo)

    memo[pos] = count_down + count_right
    return memo[pos] 

# Driver code 
# Test case 01 
if __name__ == "__main__":
    grid = [
    ["O", "O"],
    ["O", "O"],
    ]
    print(count_paths(grid)) # -> 2

    # Test case 02 
    grid = [
    ["O", "O", "X"],
    ["O", "O", "O"],
    ["O", "O", "O"],
    ]
    print(count_paths(grid)) # -> 5 

    # Test case 03 
    grid = [
    ["O", "O", "O"],
    ["O", "O", "X"],
    ["O", "O", "O"],
    ]
    print(count_paths(grid)) # -> 3

    # Test case 04
    grid = [
    ["O", "O", "O"],
    ["O", "X", "X"],
    ["O", "O", "O"],
    ]
    print(count_paths(grid)) # -> 1 

    # Test case 05 
    grid = [
    ["O", "O", "X", "O", "O", "O"],
    ["O", "O", "X", "O", "O", "O"],
    ["X", "O", "X", "O", "O", "O"],
    ["X", "X", "X", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "O"],
    ]
    print(count_paths(grid)) # -> 0

    # Test case 06
    grid = [
    ["O", "O", "X", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "X"],
    ["X", "O", "O", "O", "O", "O"],
    ["X", "X", "X", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "O"],
    ]
    print(count_paths(grid)) # -> 42