class Solution(object):
    def uniquePaths(self, m, n):
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        dp[-1][-2] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]


answer = Solution()
print(answer.uniquePaths(m=3, n=7))
