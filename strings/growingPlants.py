""" 
Caring for a plant can be hard work, but since you tend to it regularly, you have 
a plant that grows consistently. Each day, its height increases by a fixed amount 
represented by the integer upSpeed. But due to lack of sunlight, the plant decreases 
in height every night, by an amount represented by downSpeed.

Since you grew the plant from a seed, it started at height 0 initially. Given an 
integer desiredHeight, your task is to find how many days it'll take for the plant 
to reach this height.

Example
For upSpeed = 100, downSpeed = 10, and desiredHeight = 910, the output should be
solution(upSpeed, downSpeed, desiredHeight) = 10.
"""

def growingPlants(upSpeed, downSpeed, desiredHeight):
    
    first = upSpeed
    count = 1
    while upSpeed < desiredHeight:
        upSpeed = (upSpeed - downSpeed)
        upSpeed += first 
        count += 1 

    return count 

if __name__ == "__main__":
    upSpeed = 100
    downSpeed = 10 
    desiredHeight = 910 
    print(growingPlants(upSpeed, downSpeed, desiredHeight))
