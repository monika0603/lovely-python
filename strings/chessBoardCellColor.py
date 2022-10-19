""" 
Given two cells on the standard chess board, determine whether they have the same color or not.

Example

For cell1 = "A1" and cell2 = "C3", the output should be
solution(cell1, cell2) = true.
"""

def chess_board(cell1, cell2):

    rows = 9 
    cols = ['A','B','C','D','E','F','G','H']
    matrix = []

    for i in range(rows):
        a = []
        for j,n in enumerate(cols):
            if (i%2 == 0) and (j%2 != 0):
                a.append(str(n)+str(i))
            else:
                a.append('B')
        matrix.append(a)
   
    return matrix

def chess_board1(cell1, cell2):

    cell1_0 = ord(cell1[0])
    cell1_1 = int(cell1[1]) 

    cell2_0 = ord(cell2[0])
    cell2_1 = int(cell2[1])

    return (cell1_0 + cell1_1 + cell2_0 + cell2_1)%2 == 0

if __name__ == "__main__":
    print(chess_board1('A1','C3'))
            
