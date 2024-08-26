class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            if(target - nums[i] in seen):
                return [seen[target-nums[i]], i]
            seen[nums[i]] = i

answer = Solution()
print(answer.twoSum([3, 2, 4], 6))