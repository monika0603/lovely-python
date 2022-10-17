""" 
Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the
 distance between any two neighboring numbers is equal (note that 0 and n - 1 are neighboring, too).
"""

def circl_of_numbers(n, firstNum):

    return (firstNum + n/2) % n 
    
if __name__ == "__main__":
    n = 10
    firstNum = 2
    print(circl_of_numbers(n, firstNum))