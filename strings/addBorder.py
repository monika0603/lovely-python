""" 
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example: picture = ["abc",
           "ded"]

solution(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
"""

def add_border(input):

    output = []
    border = "" 
    for i in range(0, len(picture[0])+2):
        border += "*"
    output.append(border) 

    for i in range(0, len(picture)):
        output.append("*"+picture[i]+"*")

    output.append(border)
    
    return output


if __name__ == "__main__":
    picture = ["abc",
               "ded"]

    print(add_border(picture))