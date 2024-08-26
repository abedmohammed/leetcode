class Solution(object):
    def minDistance(self, word1, word2):
        dp = [[0 for _ in range(len(word1) + 1)] for _ in range(len(word2) + 1)]

        for i in range(len(word1) + 1):
            dp[-1][i] = len(word1) - i

        for j in range(len(word2) + 1):
            dp[j][-1] = len(word2) - j

        for i in range(len(word2) - 1, -1, -1):
            for j in range(len(word1) - 1, -1, -1):
                char1, char2 = word1[j], word2[i]
                if char1 == char2:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j + 1], dp[i + 1][j], dp[i + 1][j + 1])

        return dp[0][0]


answer = Solution()
print(answer.minDistance(word1="horse", word2="ros"))
print(answer.minDistance(word1="intention", word2="execution"))
