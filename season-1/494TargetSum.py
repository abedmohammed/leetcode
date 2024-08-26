class Solution(object):
    def findTargetSumWays(self, nums, target):
        dp = {}

        def topdown(i, current):
            if i < 0:
                if current == 0:
                    return 1
                return 0
            if (i, current) in dp:
                return dp[(i, current)]

            dp[(i, current)] = topdown(i - 1, current + nums[i]) + topdown(
                i - 1, current - nums[i]
            )

            return dp[(i, current)]

        return topdown(len(nums) - 1, target)


answer = Solution()
print(answer.findTargetSumWays([1, 1, 1, 1, 1], 3))
