

def pairSum(nums, target):
    start = 0
    end = len(nums) - 1 
    while end > start:
        if nums[start] + nums[end] == target:
            return True
        if nums[start] + nums[end] < target:
            start += 1
        else:
            end -= 1
    return False