""" 
Problem: Given a list of coordinates, write a function to find the k closest points 
(measure by Euclidean 
distance) to the origin. For example if k = 3, and the points are 
[[2, -1], [3,2], [4,1], [-1, -1], [-2, 2]] then return [[-1,-1],[2,-1],[-2,2]] 

A brute force way will be to iterate over all the coordinates and calculate the Euclidean distance. 
Compute the distance from each coordinate to the origin, sort them and find the k-closest to the origin. 
This will 
result in O(nlogn) because of sorting algorithm. 
A more optimized way will be to utilize a min-heap whereby we add coordinates based on the 
Euclidean distance. 
Then at the end, just take the first k elements which will already be the smallest due to min heap.
"""
import heapq 

def euclidean_distance(x,y):
    return x**2 + y**2

def closest(points, k):

    minHeap = []
    for point in points:
        x, y = point 
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
