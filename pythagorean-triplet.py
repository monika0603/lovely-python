""" 
Given an array of integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a2 + b2 = c2.
Input: arr[] = {3, 1, 4, 6, 5} 
Output: True 
There is a Pythagorean triplet (3, 4, 5).

Input: arr[] = {10, 4, 6, 12, 5} 
Output: False 
There is no Pythagorean triplet. 
"""

def triplet(numbers):

    numbers = sorted(numbers)
    print(numbers)

    for i in range(len(numbers)-2):
        a = numbers[i]
        b = numbers[i+1]
        c = numbers[i+2]

        if a*a + b*b == c*c:
            return True 

    return False 


if __name__ == "__main__":
    nums = [3,1,4,6,5]
    print(triplet(nums))

    # Test case 01
    nums = [10, 4, 6, 12, 5]
    print(triplet(nums))