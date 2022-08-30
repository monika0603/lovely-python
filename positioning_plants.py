""" 
You've been hired to plant flowers in a garden with n different positions. There are m different 
flower types. The prices of flowers types vary depending on which position they are planted. Your 
bosses are picky, they tell you to never plant two of the same flower type right next to each other. 
What is the minimum cost we need to plant a flower in each position of the garden?

Write a function, positioningPlants, that takes in a 2D list with dimensions n * m. Each row of 
the list represents the costs of the flower types at that position. This means that costs[i][j] 
represents the cost of planting flower type j at position i.

    plant 
   0  1  2
0  4  3  7
1  6  1  9
2  2  5  3  

                                  pos, last_plant 
                                  0, null (in the beginning position is zero and plant type is null)
                         4/           |3           \ 7
                        (1,0)        (1,1)          (1,2)
                     1/     9\
                (2,1)        (1,2)     

Brute force complexity: n = # of positions
                        m = # of plant types
                Time: O(m^n)
               Space: O(n)
Memoization: Time: O(mn)
"""

# Brute force solution only using recursion
def positioning_plants(costs, pos=0, last_plant=None):
    if pos == len(costs):
        return 0 

    min_cost = float("inf")
    for plant_type, plant_cost in enumerate(costs[pos]):
        if plant_type != last_plant:
            candidate = plant_cost + positioning_plants(costs, pos+1, plant_type)
            min_cost = min(candidate, min_cost)

    return min_cost

# Optimized solution using memoization
def positioning_plants_memo(costs, pos=0, last_plant=None):
    return _positioning_plants_memo(costs, pos, last_plant, {})

def _positioning_plants_memo(costs, pos, last_plant, memo):
    key = (pos, last_plant)
    if key in memo:
        return memo[key]

    if pos == len(costs):
        return 0 

    min_cost = float("inf")
    for plant_type, plant_cost in enumerate(costs[pos]):
        if plant_type != last_plant:
            candidate = plant_cost + _positioning_plants_memo(costs, pos+1, plant_type, memo)
            min_cost = min(min_cost, candidate)
            memo[key] = min_cost
 
    return min_cost

# Driver code 
if __name__ == "__main__":
    print(positioning_plants([
    [4, 3, 7],
    [6, 1, 9],
    [2, 5, 3]
    ])) # -> 7, by doing 4 + 1 + 2.

    # Test case 02
    print(positioning_plants([
    [12, 14, 5],
    [6, 3, 2]
    ])) # -> 8

    # Test case 03
    print(positioning_plants([
    [12, 14, 5],
    [6, 3, 2],
    [4, 2, 7],
    [4, 8, 4],
    [1, 13, 5],
    [8, 6, 7],
    ])) # -> 23

    # Test case 04
    print(positioning_plants([
    [12, 14, 5, 13],
    [6, 3, 20, 3],
    [24, 12, 7, 2],
    [4, 80, 45, 3],
    [104, 13, 5, 14],
    [38, 19, 7, 6],
    [12, 2, 1, 2],
    ])) # -> 26

    # Test case 05
    print(positioning_plants_memo([
    [12, 14, 50, 12],
    [6, 3, 20, 3],
    [24, 12, 7, 2],
    [4, 80, 45, 3],
    [104, 13, 5, 14],
    [38, 19, 7, 6],
    [1, 20, 1, 2],
    [13, 12, 5, 13],
    [60, 32, 20, 3],
    [24, 12, 7, 2],
    [4, 80, 44, 1],
    [104, 13, 5, 14],
    [38, 19, 76, 6],
    [12, 23, 12, 20],
    [1, 3, 1, 1],
    [1, 2, 12, 5],
    ])) # -> 74