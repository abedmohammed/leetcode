class Solution(object):
    def canPartition(self, nums):
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return True if target in dp else False


answer = Solution()
print(answer.canPartition([1, 5, 11, 5]))
print(answer.canPartition([1, 2, 3, 5]))
