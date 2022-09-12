""" 
Algorithm:
1. I need to pass along the position, and plant_type. Initial plant_type selection will determine my next choice of cost and plant_type. 
2. position will help me slice the input grid, and create a base case if I have reached the length of the grid. 
3. Minimum selection logic where I keep adding the plant_cost
"""

# Brute force solution
def positioning_plants(costs, pos=0, last_plant=None):
    return _positioning_plants(costs, pos, last_plant)

def _positioning_plants(costs, pos, last_plant):
    if pos == len(costs):
        return 0 

    min_cost = float("inf")
    for plant_type, plant_cost in enumerate(costs[pos]):
        if plant_type != last_plant:
            candidate = plant_cost + _positioning_plants(costs, pos+1, plant_type) 
            min_cost = min(min_cost, candidate) 

    return min_cost

# Optimized solution
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


if __name__ == "__main__":
    print(positioning_plants([
    [4, 3, 7],
    [6, 1, 9],
    [2, 5, 3]
    ])) # -> 7, by doing 4 + 1 + 2.

    # Test case 01
    print(positioning_plants_memo([
    [12, 14, 5],
    [6, 3, 2]
    ])) # -> 8

    # Test case 02
    print(positioning_plants([
    [12, 14, 5],
    [6, 3, 2],
    [4, 2, 7],
    [4, 8, 4],
    [1, 13, 5],
    [8, 6, 7],
    ])) # -> 23

    # Test case 03
    print(positioning_plants([
    [12, 14, 5, 13],
    [6, 3, 20, 3],
    [24, 12, 7, 2],
    [4, 80, 45, 3],
    [104, 13, 5, 14],
    [38, 19, 7, 6],
    [12, 2, 1, 2],
    ])) # -> 26 

    # Test case 04
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