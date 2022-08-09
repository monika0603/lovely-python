
def minimum_island(grid):

    min_island = float("inf") 
    visited = set() 
    output = []

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'L':
                size = dfs(grid, row, col, visited)
                if size > 0:
                    output.append(size)
                    min_island = min(size, min_island) 

    return min_island, output

def dfs(grid, row, col, visited):

    row_inbounds = 0 <= row < len(grid)
    col_inbounds = 0 <= col < len(grid[0]) 

    if not row_inbounds or not col_inbounds or grid[row][col] == 'W':
        return 0 

    pos = (row, col)
    if pos in visited:
        return 0 

    visited.add(pos) 

    size = 1 
    size += dfs(grid, row+1, col, visited)
    size += dfs(grid, row-1, col, visited)
    size += dfs(grid, row, col+1, visited)
    size += dfs(grid, row, col-1, visited)

    return size 

# Drive code 
if __name__ == "__main__":
    # Test case 01
    grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
    ]

    print(minimum_island(grid)) # -> 2

    # Test case 02
    grid = [
    ['L', 'W', 'W', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['W', 'L', 'W', 'L', 'W'],
    ['W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'L', 'L', 'L'],
    ]

    print(minimum_island(grid)) # -> 1

    # Test case 03 
    grid = [
    ['L', 'L', 'L'],
    ['L', 'L', 'L'],
    ['L', 'L', 'L'],
    ]

    print(minimum_island(grid)) # -> 9

    # Test case 04 
    grid = [
    ['W', 'W'],
    ['L', 'L'],
    ['W', 'W'],
    ['W', 'L']
    ]

    print(minimum_island(grid)) # -> 1