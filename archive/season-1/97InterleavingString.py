class Solution(object):
    def isInterleave(self, s1, s2, s3):
        # # Memoization
        # dp = {}
        # if len(s3) != len(s1) + len(s2):
        #     return False

        # def dfs(i, j, curr):
        #     if i == len(s1):
        #         return True if curr + s2[j:] == s3 else False
        #     if j == len(s2):
        #         return True if curr + s1[i:] == s3 else False
        #     if curr != s3[: i + j]:
        #         return False
        #     if (i, j) in dp:
        #         return dp[(i, j)]

        #     dp[(i, j)] = dfs(i + 1, j, curr + s1[i]) or dfs(i, j + 1, curr + s2[j])

        #     return dp[(i, j)]

        # return dfs(0, 0, "")

        # 2D DP
        if len(s3) != len(s1) + len(s2):
            return False

        dp = [[False for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]

        dp[-1][-1] = True

        for i in range(len(s1) - 1, -1, -1):
            if s1[i] == s3[i + len(s2)] and dp[i + 1][-1]:
                dp[i][-1] = True

        for i in range(len(s2) - 1, -1, -1):
            if s2[i] == s3[i + len(s1)] and dp[-1][i + 1]:
                dp[-1][i] = True

        for i in range(len(s1) - 1, -1, -1):
            for j in range(len(s2) - 1, -1, -1):
                if (s1[i] == s3[i + j] and dp[i + 1][j]) or (
                    s2[j] == s3[i + j] and dp[i][j + 1]
                ):
                    dp[i][j] = True

        for row in dp:
            print(row)

        return dp[0][0]


answer = Solution()
print(answer.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))
# print(answer.isInterleave("ac", "dc", "adcc"))
# print(answer.isInterleave("", "", ""))
# print(answer.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc"))
