""" 
Problem: Given a list of coordinates, write a function to find the k closest points (measure by Euclidean 
distance) to the origin. For example if k = 3, and the points are 
[[2, -1], [3,2], [4,1], [-1, -1], [-2, 2]] then return [[-1,-1],[2,-1],[-2,2]] 

Algorithm: 

1. Brute force solution is to calculate the Euclidean distance (x**2 + y**2) and sort the distances. 
This will result in O(nlogn) because of the sorting algorithm. 

2. Optimized way is to use DS called heapq, and use min heap function of it to get the smallest distances 
upto the desired values of k.
"""

import heapq 

def euclidean_distance(x,y):
    return x**2 + y**2 

def closest(points, k):

    minHeap = []
    for point in points:
        x,y = point 
        distance = euclidean_distance(x,y) 
        minHeap.append([distance, x, y])

    heapq.heapify(minHeap)

    output = []
    while k >= 0:
        distance, x, y = heapq.heappop(minHeap)
        output.append([x,y])    
        k -= 1 

    return output 

if __name__ == "__main__":
    points = [[2, -1], [3,2], [4,1], [-1, -1], [-2, 2]]
    k = 2
    print(closest(points, k))
