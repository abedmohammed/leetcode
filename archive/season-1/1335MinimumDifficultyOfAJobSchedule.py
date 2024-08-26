class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        if len(jobDifficulty) < d:
            return -1

        dp = {}

        def dfs(i, currD, currMax):
            if i == len(jobDifficulty):
                return 0 if currD == d else float("inf")
            elif currD >= d:
                return float("inf")
            elif (i, currD, currMax) in dp:
                return dp[(i, currD, currMax)]

            currMax = max(jobDifficulty[i], currMax)

            res = min(dfs(i + 1, currD, currMax), currMax + dfs(i + 1, currD + 1, 0))

            dp[(i, currD, currMax)] = res

            return res

        return dfs(0, 0, 0)


answer = Solution()
print(answer.minDifficulty(jobDifficulty=[6, 5, 4, 3, 2, 1], d=2))
print(answer.minDifficulty(jobDifficulty=[9, 9, 9], d=2))
print(answer.minDifficulty(jobDifficulty=[1, 1, 1], d=3))
