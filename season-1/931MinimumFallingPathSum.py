class Solution(object):
    def minFallingPathSum(self, matrix):
        n = len(matrix)

        dp = [[0] * n for _ in range(n)]

        for j in range(n):
            dp[-1][j] = matrix[-1][j]

        for i in range(n - 2, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = matrix[i][j]
                if j == 0:
                    dp[i][j] += min(dp[i + 1][j], dp[i + 1][j + 1])
                elif j == n - 1:
                    dp[i][j] += min(dp[i + 1][j], dp[i + 1][j - 1])
                else:
                    dp[i][j] += min(dp[i + 1][j], dp[i + 1][j + 1], dp[i + 1][j - 1])

        for row in dp:
            print(row)

        return min(dp[0])


answer = Solution()
print(
    answer.minFallingPathSum(
        matrix=[
            [100, -42, -46, -41],
            [31, 97, 10, -10],
            [-58, -51, 82, 89],
            [51, 81, 69, -51],
        ]
    )
)
print(answer.minFallingPathSum(matrix=[[-19, 57], [-40, -5]]))
print(answer.minFallingPathSum(matrix=[[-19]]))
