class Solution(object):
    def sumSubarrayMins(self, arr):
        MOD = 10**9 + 7
        # dp = {}

        # def dfs(i, minNum):
        #     if i == len(arr):
        #         return 0
        #     minNum = min(minNum, arr[i])
        #     if (i, minNum) in dp:
        #         return dp[(i, minNum)]

        #     dp[(i, minNum)] = dfs(i + 1, minNum) + minNum
        #     return dp[(i, minNum)]

        # res = 0
        # for i in range(len(arr)):
        #     res += dfs(i, float("inf"))

        # return res % MOD


answer = Solution()

print(answer.sumSubarrayMins(arr=[3, 1, 2, 4]))
# print(answer.sumSubarrayMins(arr=[11, 81, 94, 43, 3]))
