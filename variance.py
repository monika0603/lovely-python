""" 
Calculate variance for a list of dictionaries 

variance = sum(x - mean)**2/(n-1)
"""

import math
def variance(input):

    for i in range(len(input)):
        for key, values in input[i].items():
            if isinstance(values, list):
                mean = sum(values)/len(values)
                n = len(values)
                variance = 0
                for value in values:
                    variance += round((value - mean)**2/(n-1), 2)

        print('mean, variance = ', mean, variance)



if __name__ == "__main__":

    input = [
    {
        'key': 'list1',
        'values': [4,5,2,3,4,5,2,3],
    },
    {
        'key': 'list2',
        'values': [1,1,34,12,40,3,9,7],
    }
]

print(variance(input))