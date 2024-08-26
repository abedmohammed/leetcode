class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        # dp = [[0 for _ in range(len(text1) + 1)] for _ in range(len(text2) + 1)]

        # for i in range(1, len(text2) + 1):
        #     for j in range(1, len(text1) + 1):
        #         if text2[i - 1] == text1[j - 1]:
        #             dp[i][j] = dp[i - 1][j - 1] + 1
        #         else:
        #             dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # for r in dp:
        #     print(r)

        # return dp[-1][-1]

        dp = [0 for _ in range(len(text1) + 1)]

        for i in range(1, len(text2) + 1):
            newDP = [0 for _ in range(len(text1) + 1)]
            for j in range(1, len(text1) + 1):
                if text2[i - 1] == text1[j - 1]:
                    newDP[j] = dp[j - 1] + 1
                else:
                    newDP[j] = max(dp[j], newDP[j - 1])
            dp = newDP

        return dp[-1]


answer = Solution()
print(answer.longestCommonSubsequence(text1="abcde", text2="ace"))
