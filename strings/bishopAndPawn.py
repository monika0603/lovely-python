""" 
Given the positions of a white bishop and a black pawn on the standard chess 
board, determine whether the bishop can capture the pawn in one move.

The bishop has no restrictions in distance for each move, but is limited to 
diagonal movement. Check out the example below to see how it can move:
"""

def bishopPawan(bishop, pawn):

    return abs(int(bishop[1]) - int(pawn[1])) == abs(ord(bishop[0]) - ord(pawn[0]))

if __name__ == "__main__":
    bishop = 'a1'
    pawn = 'c3'
    print(bishopPawan(bishop, pawn))

    # Test case 01
    bishop = 'h1'
    pawn = 'h3'
    print(bishopPawan(bishop, pawn))
