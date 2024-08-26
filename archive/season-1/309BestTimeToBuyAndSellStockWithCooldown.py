class Solution(object):
    def maxProfit(self, prices):
        dp = {}

        def dfs(i, buy):
            if i >= len(prices):
                return 0
            if (i, buy) in dp:
                return dp[(i, buy)]

            if buy:
                dp[(i, buy)] = max(
                    dfs(i + 1, False) - prices[i],
                    dfs(i + 1, True),
                )
            else:
                dp[(i, buy)] = max(
                    dfs(i + 2, True) + prices[i],
                    dfs(i + 1, False),
                )

            return dp[(i, buy)]

        return dfs(0, True)


answer = Solution()
print(answer.maxProfit([1, 2, 3, 0, 2]))
print(answer.maxProfit([2, 1, 4]))
