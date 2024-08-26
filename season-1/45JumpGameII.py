class Solution(object):
    def jump(self, nums):
        # # DP
        # dp = [0 for _ in range(len(nums))]

        # for i in range(len(nums) - 2, -1, -1):
        #     minJumps = float("inf")
        #     for j in range(i + 1, min(i + nums[i] + 1, len(nums))):
        #         minJumps = min(minJumps, dp[j])
        #     dp[i] = minJumps + 1

        # return dp[0]

        # Greedy
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            furthest = 0
            for i in range(l, r + 1):
                furthest = max(furthest, i + nums[i])
            l = r + 1
            r = furthest
            res += 1

        return res


answer = Solution()
print(answer.jump(nums=[2, 3, 1, 1, 4]))
print(answer.jump(nums=[2]))
