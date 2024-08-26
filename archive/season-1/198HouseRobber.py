class Solution(object):
    def rob(self, nums):
        robFirst, robSecond = 0, 0

        for n in nums:
            maximumHarvest = max(robSecond, robFirst + n)
            robFirst = robSecond
            robSecond = maximumHarvest

        return max(robFirst, robSecond)

        

answer = Solution()
print(answer.rob([1,2,3,1]))
print(answer.rob([2,7,9,3,1]))