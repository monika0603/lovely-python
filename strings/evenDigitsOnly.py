""" 
Check if all digits of the given integer are even.

Example

For n = 248622, the output should be
solution(n) = true;
For n = 642386, the output should be
solution(n) = false.
"""

def evenDigitsOnly(n):

    n = str(n)

    for i in n:
        if int(i)%2 != 0:
            return False 

    return True 

if __name__ == "__main__":
    n = 248622
    print(evenDigitsOnly(n))

    # Test case 02
    n = 642386
    print(evenDigitsOnly(n))