def moveZeroes(nums):
    lastIndex = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[lastIndex] = nums[i]
            lastIndex += 1
    for i in range(lastIndex, len(nums)):
        nums[i] = 0
    return nums
print(moveZeroes([0, 1, 0, 3, 12]))
