nums = [2,7,11,15]
target = 9

for i in range(len(nums)):
    num = target - nums[i]
    if num in nums:
        x = nums.index(num)
        print([i,x]) 
        if i != x: 
            break