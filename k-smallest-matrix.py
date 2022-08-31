""" 
Problem: Say you have an nxn matrix of elements that are sorted in ascending order both in the 
column and rows of the matrix. Return the kth smallest element of the matrix. For example, 
consider the matrix below:
[1 4 7]
[3 5 9]
[6 8 11]
"""

import heapq 

def smallest(grid, k):

    minHeap = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            minHeap.append(grid[row][col])

    heapq.heapify(minHeap)

    return minHeap[k]

if __name__ == "__main__":

    grid = [ 
        [1, 4, 7],
        [3, 5, 9],
        [6, 8, 11]
    ]
    print(smallest(grid, 7))