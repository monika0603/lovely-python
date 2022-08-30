""" 
Write a function, breaking_boundaries, that takes in 5 arguments: a number of rows (m), 
a number of columns (n), a number of moves (k), a starting row (r), and a starting column (c). 
Say you were situated in a grid with dimensions m * n. If you had to start at position (r,c), 
in how many different ways could you move out of bounds if you could take at most k moves. 
A single move is moving one space up, down, left, or right. During a path you may revisit a 
position.

Given m, n, k, r, c:

3, 4, 2, 0, 0

   0      1     2    3
0 (0,0) (0,1) (0,2) (0,3)
1
2

In this example given that we have k=2 moves, there are 4 ways we can be out of bounds
1. up
2. left
3. right-up
4. down-left
"""

def breaking_boundaries(m, n, k, r, c):
    return _breaking_boundaries(m, n, k, r, c)


def _breaking_boundaries(m, n, k, r, c):

    row_inbounds = 0 <= r < m 
    col_inbounds = 0 <= c < n 

    if not row_inbounds or not col_inbounds:
        return 1 

    if k == 0:
        return 0 

    count = 0 
    deltas = [(-1,0), (1,0), (0,-1), (0,1)]
    for delta in deltas:
        dx, dy = delta 
        count += _breaking_boundaries(m, n, k-1, r+dy, c+dx)

    return count 

def breaking_boundaries_memo(m, n, k, r, c):
    return _breaking_boundaries_memo(m, n, k, r, c, {})

def _breaking_boundaries_memo(m, n, k, r, c, memo):
    key = (k, r, c)
    if key in memo:
        return memo[key] 

    row_inbounds = 0 <= r < m 
    col_inbounds = 0 <= c < n 

    if not row_inbounds or not col_inbounds:
        return 1 

    if k == 0:
        return 0 

    count = 0
    deltas = [(-1,0), (1,0), (0,-1), (0,1)]
    for delta in deltas:
        dx, dy = delta 
        count += _breaking_boundaries_memo(m, n, k-1, r+dy, c+dx, memo) 
        memo[key] = count 

    return count 



if __name__ == "__main__":
    print(breaking_boundaries(3, 4, 2, 0, 0)) # -> 4

    # Test case 01
    print(breaking_boundaries(2, 2, 2, 1, 1)) # -> 6

    #Test case 02
    print(breaking_boundaries(3, 4, 3, 0, 0)) # -> 11

    # Test case 03
    print(breaking_boundaries(4, 4, 5, 2, 1)) # -> 160

    # Test case 04
    print(breaking_boundaries(5, 6, 9, 2, 5)) # -> 11635

    # Test case 05
    print(breaking_boundaries_memo(6, 6, 12, 3, 4)) # -> 871065

    # Test case 06
    print(breaking_boundaries_memo(6, 6, 15, 3, 4)) # -> 40787896

    # Test case 07
    print(breaking_boundaries_memo(6, 8, 16, 2, 1)) # -> 137495089
    
        


