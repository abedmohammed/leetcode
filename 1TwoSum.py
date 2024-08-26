class Solution(object):
    def twoSum(self, nums, target):
        seenNums = {}
        for i in range(len(nums)):
            find = target - nums[i]
            if find in seenNums:
                return [i, seenNums[find]]

            seenNums[nums[i]] = i


"""
# Code
for i, n in enumerate(nums)

i -> indexes
n -> values
"""
