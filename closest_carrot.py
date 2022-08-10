
from collections import deque
def closest_carrot(grid, row, col):

    queue = deque([(row, col, 0)])
    visited = set() 
    visited.add((row,col))

    while queue:
        r, c, distance = queue.popleft()

        if grid[r][c] == 'C':
            return distance 

        deltas = [(-1,0),(1,0),(0,-1),(0,1)]
        for delta in deltas:
            dx, dy = delta 
            neighbor_row = r+dx 
            neighbor_col = c+dy 
            pos = (neighbor_row, neighbor_col)

            if check_bounds(grid, neighbor_row, neighbor_col):
                if pos not in visited and grid[neighbor_row][neighbor_col] != 'X':
                    visited.add(pos) 
                    queue.append((neighbor_row, neighbor_col, distance+1)) 

    return -1 

def check_bounds(grid, r, c):
    row_inbounds = 0 <= r < len(grid)
    col_inbounds = 0 <= c < len(grid[0])

    if row_inbounds and col_inbounds:
        return True 

    return False 

# Driver code 

if __name__ == "__main__":
    # Test case 01
    grid = [
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'X', 'O', 'O', 'O'],
    ['O', 'X', 'X', 'O', 'O'],
    ['O', 'X', 'C', 'O', 'O'],
    ['O', 'X', 'X', 'O', 'O'],
    ['C', 'O', 'O', 'O', 'O'],
    ]

    print(closest_carrot(grid, 1, 2)) # -> 4

    # Test case 02 
    grid = [
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'X', 'O', 'O', 'O'],
    ['O', 'X', 'X', 'O', 'O'],
    ['O', 'X', 'C', 'O', 'O'],
    ['O', 'X', 'X', 'O', 'O'],
    ['C', 'O', 'O', 'O', 'O'],
    ]

    print(closest_carrot(grid, 0, 0)) # -> 5

    # Test case 03
    grid = [
    ['O', 'O', 'X', 'X', 'X'],
    ['O', 'X', 'X', 'X', 'C'],
    ['O', 'X', 'O', 'X', 'X'],
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'X', 'X', 'X', 'X'],
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'C', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O'],
    ]

    print(closest_carrot(grid, 3, 4)) # -> 9 

    # Test case 04
    grid = [
    ['O', 'O', 'X', 'O', 'O'],
    ['O', 'X', 'X', 'X', 'O'],
    ['O', 'X', 'C', 'C', 'O'],
    ]

    print(closest_carrot(grid, 1, 4)) # -> 2

    # Test case 05
    grid = [
    ['O', 'O', 'X', 'O', 'O'],
    ['O', 'X', 'X', 'X', 'O'],
    ['O', 'X', 'C', 'C', 'O'],
    ]

    print(closest_carrot(grid, 2, 0)) # -> -1

    # Test case 06
    grid = [
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'C'],
    ]

    print(closest_carrot(grid, 0, 0)) # -> -1