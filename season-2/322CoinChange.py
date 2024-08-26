class Solution(object):
    def coinChange(self, coins, amount):
        dp = [float("inf")] * (amount + 1)

        dp[0] = 0

        for i in range(amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if not float("inf") else -1


answer = Solution()
print(answer.coinChange([2], 3))
# print(answer.coinChange([1, 2, 5], 11))
# print(answer.coinChange([186, 419, 83, 408], 6249))
