class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        # dp = {}

        # def dfs(i, j):
        #     if i < 0 or i >= ROWS or j < 0 or j >= COLS or obstacleGrid[i][j] == 1:
        #         return 0
        #     if i == ROWS - 1 and j == COLS - 1:
        #         return 1
        #     if (i, j) in dp:
        #         return dp[(i, j)]

        #     dp[(i, j)] = res = dfs(i + 1, j) + dfs(i, j + 1)
        #     return res

        # return dfs(0, 0)

        dp = [[0 for _ in range(COLS + 1)] for _ in range(ROWS + 1)]

        dp[-2][-2] = 1

        for i in range(len(dp) - 2, -1, -1):
            for j in range(len(dp[0]) - 2, -1, -1):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] += dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]


answer = Solution()
print(answer.uniquePathsWithObstacles(obstacleGrid=[[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(answer.uniquePathsWithObstacles(obstacleGrid=[[0]]))
