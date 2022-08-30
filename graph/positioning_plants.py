
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

    # Test case 02
    print(positioning_plants_memo([
    [12, 14, 50, 12, 13],
    [6, 3, 20, 3, 16],
    [24, 12, 7, 2, 74],
    [4, 80, 45, 3, 100],
    [104, 13, 5, 14, 3],
    [38, 19, 7, 6, 24],
    [1, 20, 1, 2, 31],
    [13, 12, 5, 13, 9],
    [60, 32, 20, 3, 2],
    [24, 12, 7, 2, 42],
    [4, 80, 44, 1, 23],
    [104, 13, 5, 14, 28],
    [38, 19, 76, 6, 12],
    [12, 23, 12, 20, 13],
    [1, 3, 1, 1, 50],
    [1, 2, 12, 5, 36],
    [6, 2, 3, 12, 20],
    [4, 6, 4, 11, 15],
    ])) # -> 75

    # Test case 03
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