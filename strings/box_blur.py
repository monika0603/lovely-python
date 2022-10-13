""" 
Last night you partied a little too hard. Now there's a black and white photo of you that's about to go 
viral! You can't let this ruin your reputation, so you want to apply the box blur algorithm to the photo 
to hide its content.

The pixels in the input image are represented as integers. The algorithm distorts the input image in the 
following way: Every pixel x in the output image has a value equal to the average value of the pixel values 
from the 3 × 3 square that has its center at x, including x itself. All the pixels on the border of x are 
then removed.

Return the blurred image as an integer, with the fractions rounded down.

Example

For

image = [[1, 1, 1], 
         [1, 7, 1], 
         [1, 1, 1]]
the output should be solution(image) = [[1]].

To get the value of the middle pixel in the input 3 × 3 square: (1 + 1 + 1 + 1 + 7 + 1 + 1 + 1 + 1) = 15 / 9 = 1.66666 = 1. 
The border pixels are cropped from the final result.
"""
def matrix(input, i, j):

    sum = 0 
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            sum += input[x][y]

    return sum//9 

def box_blur(image):

    sol = [] 
    for i in range(1,len(image)-1):
        temp = [] 
        for j in range(1,len(image[0])-1):
            temp.append(matrix(image, i, j))
        sol.append(temp)

    return sol 

if __name__ == "__main__":
    image = [[1, 1, 1], 
            [1, 7, 1], 
            [1, 1, 1]] 

    print(box_blur(image))

    # Test case 01
    image = [[7, 4, 0, 1], 
            [5, 6, 2, 2], 
            [6, 10, 7, 8], 
            [1, 4, 2, 0]] 

    print(box_blur(image))
