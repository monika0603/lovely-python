""" 
You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make 
jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.

Example

For inputArray = [5, 3, 6, 7, 9], the output should be
solution(inputArray) = 4.

Algorithm:
1. Create two variable position = 0 and step = 1 
2. Loop over as long as position <= max value in the input
3. if pos in the input, increment the step and initialize position back to zero 
4. else increment position with step 
5. return step at the end 
"""

def avoid_obstacles(nums):

    pos = 0 
    step = 1 

    while pos <= max(nums):
        print(pos, step)
        if pos in nums:
            step += 1
            pos = 0 
        else:
            pos += step 

    return step 

if __name__ == "__main__":
    nums = [5, 3, 6, 7, 9]
    print(avoid_obstacles(nums))