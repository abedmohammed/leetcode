class Solution(object):
    def countSubstrings(self, s):
        # DP APPROACH
        dp = [[0] * len(s) for _ in range(len(s))]
        res = len(s)

        for i in range(len(s)):
            dp[i][i] = 1

        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                charI, charJ = s[i], s[j]

                if charI == charJ:
                    if j - i < 2 or dp[i + 1][j - 1] == 1:
                        dp[i][j] = 1
                        res += 1

        return res


answer = Solution()
print(answer.countSubstrings(s="aaa"))
