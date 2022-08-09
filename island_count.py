
def island_count(grid):

    count = 0
    visited = set()

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'L':
                if dfs(grid, row, col, visited) == True:
                    count += 1 

    return count 

def dfs(grid, row, col, visited):

    row_inbounds = 0 <= row < len(grid)
    col_inbounds = 0 <= col < len(grid[0])

    if not row_inbounds or not col_inbounds or grid[row][col] == 'W':
        return False 

    pos = (row, col)
    if pos in visited:
        return False 

    visited.add(pos) 

    dfs(grid, row+1, col, visited)
    dfs(grid, row-1, col, visited)
    dfs(grid, row, col+1, visited)
    dfs(grid, row, col-1, visited) 

    return True 

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

    print(island_count(grid)) # -> 3

    # Test case 02 
    grid = [
    ['L', 'W', 'W', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['W', 'L', 'W', 'L', 'W'],
    ['W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'L', 'L', 'L'],
    ]

    print(island_count(grid)) # -> 4

    grid = [
    ['L', 'L', 'L'],
    ['L', 'L', 'L'],
    ['L', 'L', 'L'],
    ]

    print(island_count(grid)) # -> 1

    grid = [
    ['W', 'W'],
    ['W', 'W'],
    ['W', 'W'],
    ]

    print(island_count(grid)) # -> 0