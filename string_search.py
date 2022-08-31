""" 
Write a function, string_search, that takes in a grid of letters and a string as arguments. 
The function should return a boolean indicating whether or not the string can be found in the 
grid as a path by connecting horizontal or vertical positions. The path can begin at any position, 
but you cannot reuse a position more than once in the path.

You can assume that all letters are lowercase and alphabetic.
"""

def string_search(grid, s):

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if dfs(grid, row, col, s, set()) == True:
                return True 

    return False 

def dfs(grid, r, c, s, visited):

    if s == '':
        return True  

    row_inbounds = 0 <= r < len(grid)
    col_inbounds = 0 <= c < len(grid[0])

    pos = (r,c)
    if pos in visited:
        return False 

    visited.add(pos)

    if not row_inbounds or not col_inbounds:
        return False 

    if grid[r][c] != s[0]:
        return False 

    suffix = s[1:]
    return dfs(grid, r+1, c, suffix, set(visited)) or dfs(grid, r-1, c, suffix, set(visited)) or dfs(grid, r, c+1, suffix, set(visited)) or dfs(grid, r, c-1, suffix, set(visited))


if __name__ == "__main__":
    grid = [
    ['e', 'y', 'h', 'i', 'j'],
    ['q', 'x', 'e', 'r', 'p'],
    ['r', 'o', 'l', 'l', 'n'],
    ['p', 'r', 'x', 'o', 'h'],
    ['a', 'a', 'm', 'c', 'm']
    ]
    print(string_search(grid, 'hello')) # -> True

    # Test case 01
    grid = [
    ['e', 'y', 'h', 'i', 'j'],
    ['q', 'x', 'e', 'r', 'p'],
    ['r', 'o', 'l', 'l', 'n'],
    ['p', 'r', 'x', 'o', 'h'],
    ['a', 'a', 'm', 'c', 'm']
    ]
    print(string_search(grid, 'proxy')) # -> True

    # Test case 02
    grid = [
    ['e', 'y', 'h', 'i', 'j'],
    ['q', 'x', 'e', 'r', 'p'],
    ['r', 'o', 'l', 'l', 'n'],
    ['p', 'r', 'x', 'o', 'h'],
    ['a', 'a', 'm', 'c', 'm']
    ]
    print(string_search(grid, 'rolling')) # -> False