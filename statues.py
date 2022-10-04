""" 
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having 
an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest 
to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional 
statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

Example

For statues = [6, 2, 3, 8], the output should be
solution(statues) = 3.

Ratiorg needs statues of sizes 4, 5 and 7.
"""

def statues(nums):

    max_num = max(nums)
    min_num = min(nums) 

    actual = []
    for i in range(min_num, max_num+1):
        actual.append(i) 

    missing = [j for j in actual if j not in nums]
    return len(missing) 


if __name__ == "__main__":
    nums = [6, 2, 3, 8]
    print(statues(nums))