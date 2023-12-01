class Solution(object):
    def twoSum(self, nums, target):
        needed = {}

        for i, num in enumerate(nums):
            if target - num in needed:
                return [i, needed[target - num]]

            needed[num] = i


answer = Solution()
print(answer.twoSum(nums=[2, 7, 11, 15], target=9))
