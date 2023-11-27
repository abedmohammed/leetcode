class Solution(object):
    def knightDialer(self, n):
        MOD = 10**9 + 7
        MOVES = {
            0: [4, 6],
            1: [8, 6],
            2: [7, 9],
            3: [4, 8],
            4: [9, 3, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
        }

        dp = [[0] * 10 for _ in range(n)]

        for i in range(10):
            dp[0][i] = 1

        for i in range(1, len(dp)):
            for j in range(10):
                for move in MOVES[j]:
                    dp[i][j] += dp[i - 1][move] % MOD

        return sum(dp[n - 1]) % MOD


answer = Solution()
print(answer.knightDialer(n=3))
