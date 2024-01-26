class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        # cache = {}
        # MOD = 10**9 + 7

        # def backtrack(i, j, movesLeft):
        #     if i < 0 or i >= m or j < 0 or j >= n:
        #         return 1
        #     if movesLeft <= 0:
        #         return 0
        #     if (i, j, movesLeft) in cache:
        #         return cache[(i, j, movesLeft)]

        #     res = (
        #         backtrack(i, j + 1, movesLeft - 1)
        #         + backtrack(i + 1, j, movesLeft - 1)
        #         + backtrack(i, j - 1, movesLeft - 1)
        #         + backtrack(i - 1, j, movesLeft - 1)
        #     ) % MOD

        #     cache[(i, j, movesLeft)] = res
        #     return res % MOD

        # return backtrack(startRow, startColumn, maxMove)

        dp = [[0 for _ in range(n)] for _ in range(m)]

        for move in range(1, maxMove + 1):
            curDP = [[0 for _ in range(n)] for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    curDP[i][j] += 1 if i - 1 < 0 else dp[i - 1][j]
                    curDP[i][j] += 1 if i + 1 >= m else dp[i + 1][j]
                    curDP[i][j] += 1 if j + 1 >= n else dp[i][j + 1]
                    curDP[i][j] += 1 if j - 1 < 0 else dp[i][j - 1]

            dp = curDP

        return dp[startRow][startColumn]


answer = Solution()
print(answer.findPaths(m=2, n=2, maxMove=2, startRow=0, startColumn=0))
print(answer.findPaths(m=1, n=3, maxMove=3, startRow=0, startColumn=1))
