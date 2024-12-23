class Solution(object):
    def minCostClimbingStairs(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            if(target - nums[i] in seen):
                return [seen[target-nums[i]], i]
            seen[nums[i]] = i

answer = Solution()
print(answer.minCostClimbingStairs(PARAMS))
