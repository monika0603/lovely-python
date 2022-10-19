""" 
Let's define digit degree of some positive integer as the number of times we 
need to replace this number with the sum of its digits until we get to a one 
digit number.

Given an integer, find its digit degree.
"""
def findSum(n):
    
    n = str(n)
    sum = 0  
    for d in n:
        sum += int(d) 

    return sum 

def digitDegree(n):

    sum = findSum(n)
    count = 1 

    if sum == 1:
        return count 
    elif n < 10:
        return 0
    else:
        while sum > 9:
            sum = findSum(sum) 
            count += 1 

    return count 

if __name__ == "__main__":
    n = 100 
    print(digitDegree(n))

    # Test case 01
    n = 5 
    print(digitDegree(n))

    # Test case 02
    n = 91 
    print(digitDegree(n))