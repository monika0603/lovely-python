
def product(nums):

    max_product = float("-inf")
    for i in range(len(nums)-1):
        product = nums[i]*nums[i+1] 
        max_product = max(max_product, product) 

    return max_product 

if __name__ == "__main__":
    nums = [3, 6, -2, -5, 7, 3]
    print(product(nums))

