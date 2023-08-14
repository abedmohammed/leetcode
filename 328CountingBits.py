class Solution(object):
    def countBits(self, n):
        dp = [0] * (n+1)
        offset = 1

        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]

        return dp

answer = Solution()
print(answer.countBits([2]))
print(answer.countBits([5]))