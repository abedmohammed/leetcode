class Solution(object):
    def longestIncreasingPath(self, matrix):
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[float("-inf")] * COLS for _ in range(ROWS)]
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def dfs(i, j, prev):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or matrix[i][j] <= prev:
                return 0

            if dp[i][j] != float("-inf"):
                return dp[i][j]

            currMax = 0
            for di, dj in directions:
                r, c = i + di, j + dj
                currMax = max(currMax, dfs(r, c, matrix[i][j]))

            dp[i][j] = currMax + 1

            return dp[i][j]

        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                res = max(res, dfs(i, j, matrix[i][j] - 1))

        return res


answer = Solution()
print(answer.longestIncreasingPath(matrix=[[9, 9, 4], [6, 6, 8], [2, 1, 1]]))
print(answer.longestIncreasingPath(matrix=[[3, 4, 5], [3, 2, 6], [2, 2, 1]]))
print(answer.longestIncreasingPath(matrix=[[3]]))
