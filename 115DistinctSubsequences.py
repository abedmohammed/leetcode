class Solution(object):
    def numDistinct(self, s, t):
        # res = [0]

        # def dfs(i, curr):
        #     if curr == t:
        #         res[0] += 1
        #         return
        #     if i == len(s):
        #         return

        #     dfs(i + 1, curr + s[i])
        #     dfs(i + 1, curr)

        # dfs(0, "")
        # return res[0]

        # # DP solution

        # dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]

        # for i in range(len(s) + 1):
        #     dp[0][i] = 1

        # for i in range(1, len(t) + 1):
        #     for j in range(1, len(s) + 1):
        #         charS, charT = s[j - 1], t[i - 1]

        #         if charS == charT:
        #             dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
        #         else:
        #             dp[i][j] = dp[i][j - 1]

        # return dp[-1][-1]

        # # DP solution O(len(s)) memory

        dp = [1] * (len(s) + 1)

        for i in range(1, len(t) + 1):
            curr = [0] * (len(s) + 1)
            for j in range(1, len(s) + 1):
                charS, charT = s[j - 1], t[i - 1]
                if charS == charT:
                    curr[j] = dp[j - 1] + curr[j - 1]
                else:
                    curr[j] = curr[j - 1]

            dp = curr

        return dp[-1]


answer = Solution()
print(answer.numDistinct(s="rabbbit", t="rabbit"))
print(answer.numDistinct(s="babgbag", t="bag"))
print(answer.numDistinct(s="ba", t="b"))
