""" 
Problem: Write a function, best_bridge, that takes in a grid as an argument. The grid contains 
water (W) and land (L). There are exactly two islands in the grid. An island is a vertically 
or horizontally connected region of land. Return the minimum length bridge needed to connect the two islands. A bridge does not need to form a straight line.

Algorithm: 

1. Find the first island
2. BFS toward the second island
3. Count the distance 
4. return distance which is the shortest distance 
"""

from collections import deque  
def best_bridge(grid):

    main_island = None
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            potential_island = dfs(grid, row, col, set())
            if len(potential_island) > 0:
                main_island = potential_island
                break 

    visited = set(main_island) 
    queue = deque([])
    for pos in main_island:
        r,c = pos 
        queue.append((r,c,0)) 

    while queue:
        r, c, distance = queue.popleft()

        if grid[r][c] == 'L' and (r,c) not in main_island:
            return distance-1 

        deltas = [(-1,0), (1,0), (0,1), (0,-1)]
        for delta in deltas:
            dx, dy = delta 
            neighbor_row = r+dy 
            neighbor_col = c+dx 

            position = (neighbor_row, neighbor_col)
            if is_inbounds(grid, neighbor_row, neighbor_col) and position not in visited:
                visited.add(position)
                queue.append((neighbor_row, neighbor_col, distance+1))

    return -1 


def is_inbounds(grid, row, col):
    row_inbounds = 0 <= row < len(grid)
    col_inbounds = 0 <= col < len(grid[0]) 

    return row_inbounds and col_inbounds 

def dfs(grid, row, col, visited):

    if not is_inbounds(grid, row, col) or grid[row][col] == 'W':
        return visited 

    pos = (row, col)
    if pos in visited:
        return visited 

    visited.add(pos)

    dfs(grid, row+1, col, visited)
    dfs(grid, row-1, col, visited)
    dfs(grid, row, col+1, visited)
    dfs(grid, row, col-1, visited)

    return visited


# Driver code 
if __name__ == "__main__":
    # Test case 01
    grid = [
    ["W", "W", "W", "L", "L"],
    ["L", "L", "W", "W", "L"],
    ["L", "L", "L", "W", "L"],
    ["W", "L", "W", "W", "W"],
    ["W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W"],
    ]
    print(best_bridge(grid)) # -> 1 

    # Test case 02 
    grid = [
    ["W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W"],
    ["L", "L", "W", "W", "L"],
    ["W", "L", "W", "W", "L"],
    ["W", "W", "W", "L", "L"],
    ["W", "W", "W", "W", "W"],
    ]
    print(best_bridge(grid)) # -> 2

    # Test case 03 
    grid = [
    ["W", "W", "W", "W", "W"],
    ["W", "W", "W", "L", "W"],
    ["L", "W", "W", "W", "W"],
    ]
    print(best_bridge(grid)) # -> 3

    # Test case 04
    grid = [
    ["W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W", "L", "W", "W"],
    ["W", "W", "W", "W", "L", "L", "W", "W"],
    ["W", "W", "W", "W", "L", "L", "L", "W"],
    ["W", "W", "W", "W", "W", "L", "L", "L"],
    ["L", "W", "W", "W", "W", "L", "L", "L"],
    ["L", "L", "L", "W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W"],
    ]
    print(best_bridge(grid)) # -> 3

    # Test case 05
    grid = [
    ["L", "L", "L", "L", "L", "L", "L", "L"],
    ["L", "W", "W", "W", "W", "W", "W", "L"],
    ["L", "W", "W", "W", "W", "W", "W", "L"],
    ["L", "W", "W", "W", "W", "W", "W", "L"],
    ["L", "W", "W", "W", "W", "W", "W", "L"],
    ["L", "W", "W", "W", "W", "W", "W", "L"],
    ["L", "W", "W", "L", "W", "W", "W", "L"],
    ["L", "W", "W", "W", "W", "W", "W", "L"],
    ["L", "W", "W", "W", "W", "W", "W", "L"],
    ["L", "W", "W", "W", "W", "W", "W", "L"],
    ["L", "W", "W", "W", "W", "W", "W", "L"],
    ["L", "L", "L", "L", "L", "L", "L", "L"],
    ]
    print(best_bridge(grid)) # -> 2

    # Test case 06
    grid = [
    ["W", "L", "W", "W", "W", "W", "W", "W"],
    ["W", "L", "W", "W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W", "W", "L", "W"],
    ["W", "W", "W", "W", "W", "W", "L", "L"],
    ["W", "W", "W", "W", "W", "W", "W", "L"],
    ]
    print(best_bridge(grid)) # -> 8