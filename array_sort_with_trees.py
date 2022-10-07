""" 
Some people are standing in a row in a park. There are trees between them which cannot be moved. Your 
task is to rearrange the people by their heights in a non-descending order without moving the trees. 
People can be very tall!

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
solution(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
"""

def array_sort(nums):

    input = []
    for num in nums:
        if num != -1:
            input.append(num) 

    input = sorted(input) 
    j = 0
    for i in range(len(nums)):
        if nums[i] == -1:
            pass 
        else:
            nums[i] = input[j]
            j += 1
        
    return nums 

if __name__ == "__main__":
    nums = [-1, 150, 190, 170, -1, -1, 160, 180] 
    print(array_sort(nums))
