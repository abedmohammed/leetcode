class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            find = target - num
            if find in seen:
                return seen[find], i
            seen[num] = i
