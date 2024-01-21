class Solution(object):
    def rob(self, nums):
        twoAway = 0
        oneAway = 0

        for i in range(len(nums) - 1, -1, -1):
            currRob = max(oneAway, nums[i] + twoAway)

            twoAway = oneAway
            oneAway = currRob

        return oneAway


answer = Solution()

print(answer.sumSubarrayMins(nums=[1, 2, 3, 1]))
