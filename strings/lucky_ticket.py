""" 
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the 
sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
solution(n) = true;
For n = 239017, the output should be
solution(n) = false.
"""

def lucky_ticket(n):

    n = str(n) 
    half = int(len(n)/2) 
    left = n[:half]
    right = n[half:] 
    
    left_sum = 0 
    right_sum = 0 
    for char in left:
        left_sum += int(char) 
    
    for char in right:
        right_sum += int(char) 

    return left_sum == right_sum

if __name__ == "__main__":
    n = 1230 
    print(lucky_ticket(n))

    # Test case 01
    n = 239017
    print(lucky_ticket(n))
