""" 
Call two arms equally strong if the heaviest weights they each are able to lift are equal.

Call two people equally strong if their strongest arms are equally strong (the strongest arm can be 
both the right and the left), and so are their weakest arms.

Given your and your friend's arms' lifting capabilities find out if you two are equally strong.

Example

For yourLeft = 10, yourRight = 15, friendsLeft = 15, and friendsRight = 10, the output should be
solution(yourLeft, yourRight, friendsLeft, friendsRight) = true;
For yourLeft = 15, yourRight = 10, friendsLeft = 15, and friendsRight = 10, the output should be
solution(yourLeft, yourRight, friendsLeft, friendsRight) = true;
For yourLeft = 15, yourRight = 10, friendsLeft = 15, and friendsRight = 9, the output should be
solution(yourLeft, yourRight, friendsLeft, friendsRight) = false.
"""

def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):

    your_sum = yourLeft + yourRight 
    friends_sum = friendsLeft + friendsRight 

    your_max = max(yourLeft, yourRight)
    friends_max = max(friendsLeft, friendsRight) 

    return your_sum == friends_sum and your_max == friends_max 

if __name__ == "__main__":
    yourLeft = 10
    yourRight = 15
    friendsLeft = 15
    friendsRight = 10 
    print(areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight)) 

    # Test case 01
    yourLeft = 15
    yourRight = 10
    friendsLeft = 15
    friendsRight = 10 
    print(areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight)) 

    # Test case 02
    yourLeft = 15
    yourRight = 10
    friendsLeft = 15
    friendsRight = 9 
    print(areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight)) 

    # Test case 03
    yourLeft = 10
    yourRight = 15
    friendsLeft = 5
    friendsRight = 20 
    print(areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight)) 
