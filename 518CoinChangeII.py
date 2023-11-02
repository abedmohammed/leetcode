class Solution(object):
    def change(self, amount, coins):
        # # Recursive + memoization
        # dp = {}

        # def dfs(i, curVal):
        #     if curVal > amount:
        #         return 0
        #     if (i, curVal) in dp:
        #         return dp[(i, curVal)]
        #     if curVal == amount:
        #         return 1

        #     total = 0
        #     for j in range(i, len(coins)):
        #         dp[(j, curVal + coins[j])] = dfs(j, curVal + coins[j])
        #         total += dp[(j, curVal + coins[j])]

        #     return total

        # return dfs(0, 0)

        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for val in range(1, amount + 1):
                if val - coin >= 0:
                    dp[val] += dp[val - coin]
        return dp[-1]


answer = Solution()
print(answer.change(5, [1, 2, 5]))
