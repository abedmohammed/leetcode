from collections import defaultdict


class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        # def dfs(i, arr, step):
        #     if len(arr) > 2 and step != arr[-1] - arr[-2]:
        #         return 0

        #     if i >= len(nums):
        #         return 1 if len(arr) >= 3 else 0

        #     if len(arr) == 2:
        #         step = arr[-1] - arr[-2]

        #     # Take num
        #     res = dfs(i + 1, arr[:] + [nums[i]], step)

        #     # Leave num
        #     res += dfs(i + 1, arr[:], step)

        #     return res

        # return dfs(0, [], None)

        res, n = 0, len(nums)

        dp = [defaultdict(int) for _ in range(n)]

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1 + dp[j][diff]
                res += dp[j][diff]

        return res - (n * (n - 1) // 2)


answer = Solution()
print(answer.numberOfArithmeticSlices(nums=[2, 4, 6, 8, 10]))
