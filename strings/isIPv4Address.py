""" 
An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a 
computer network that uses the Internet Protocol for communication. There are two versions of the 
Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.

Given a string, find out if it satisfies the IPv4 address naming rules.

Example

For inputString = "172.16.254.1", the output should be
solution(inputString) = true;

For inputString = "172.316.254.1", the output should be
solution(inputString) = false.

316 is not in range [0, 255].

For inputString = ".254.255.0", the output should be
solution(inputString) = false.

There is no first number.
"""

def solution(s):

    s = s.split('.')
    length_s = [] 
    letters = 'abcdefghijklmnopqrstuvwxyz'

    for str in s:
        length_s.append(len(str)) 

    min_length = min(length_s)
    if min_length == 0:
        return False 

    for i in range(len(s)):
        if not s[i].isdigit():
            return False 
        if i == 1:
            if (int(s[i]) > 255) or (int(s[i]) < 0):
                return False 

    return True 

if __name__ == "__main__":
    s = "172.16.254.1" 
    print(solution(s)) # True

    # Test case 01
    s = "172.316.254.1"
    print(solution(s)) # False 

    # Test case 02
    s = ".254.255.0"
    print(solution(s)) # False 

    # Test case 03
    s = "1.1.1.1a"
    print(solution(s)) # False 