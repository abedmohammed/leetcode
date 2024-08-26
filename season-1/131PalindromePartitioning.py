class Solution(object):
    def partition(self, s):
        # # man thought he cooked
        # dp = [[0 for i in range(len(s))] for i in range(len(s))]
        # res = []

        # for i in range(len(s)):
        #     dp[i][i] = 1
        #     res.append(s[i : i + 1])

        # for i in range(len(s) - 2, -1, -1):
        #     for j in range(len(s) - 1, i, -1):
        #         if s[i] == s[j] and (len(s[i : j + 1]) < 3 or dp[i + 1][j - 1] == 1):
        #             dp[i][j] = 1
        #             res.append(s[i : j + 1])

        # return res

        res = []
        curPart = []

        def dfs(i):
            if i >= len(s):
                res.append(curPart[:])
                return

            for j in range(i, len(s)):
                substring = s[i : j + 1]
                if substring == substring[::-1]:
                    curPart.append(s[i : j + 1])
                    dfs(j + 1)
                    curPart.pop()

        dfs(0)
        return res


answer = Solution()
print(answer.partition("aab"))
