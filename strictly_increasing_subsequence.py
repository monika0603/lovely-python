""" 
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing 
sequence by removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence 
containing only one element is also considered to be strictly increasing.

Example

For sequence = [1, 3, 2, 1], the output should be
solution(sequence) = false.

There is no one element in this array that can be removed in order to get a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be
solution(sequence) = true.

You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can 
remove 2 to get the strictly increasing sequence [1, 3].

Algorithm:
                            6,9,7,8
           don't take 6  /            \ take 6    
                    9,7,8              9,7,8
      don't take 9 /     \ take 9     don't take 9 
                7,8      7,8          7,8
                                     /   \ take 7
                                         8 
      None of the moves on the left are valid because 7 or 8 smaller than 9   

1.  Use dynamic programming to solve this problem. 
2. I need an index to start from the beginning of the list, also a negative number to keep track of 
the previous I had
         
"""

def max_increasing_subsequence(numbers):
     result = _max_increasing_subsequence(numbers, 0, float("-inf"), {}) 
     return result == len(numbers)-1
        

def _max_increasing_subsequence(numbers, i, prev, memo):
    key = (i, prev)
    if key in memo:
        return memo[key]

    if i == len(numbers):
        return 0 

    current = numbers[i]
    options = []
    # If you don't take current number, then the previous doesn't change
    dont_take_current = _max_increasing_subsequence(numbers, i+1, prev, memo)
    options.append(dont_take_current)

    if current > prev:
        take_current = 1 + _max_increasing_subsequence(numbers, i+1, current, memo)
        options.append(take_current) 

    memo[key] = max(options)
    return max(options)

if __name__ == "__main__":

    numbers = [
    1, 2, 300, 3, 4, 305, 5, 12, 6, 30, 7, 8, 9, 10, 10, 10, 15, 11, 12, 13, 10, 18, 14, 15, 16,
    17, 18, 19, 20, 21, 100,101 ,102, 103, 104, 105
    ]
    print(max_increasing_subsequence(numbers)) # -> 27

    # Test case 01
    numbers = [1,3,2,1]
    print(max_increasing_subsequence(numbers))

    # Test case 02 
    numbers = [1,3,2]
    print(max_increasing_subsequence(numbers))

    
