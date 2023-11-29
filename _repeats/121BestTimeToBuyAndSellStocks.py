class Solution(object):
    def maxProfit(self, prices):
        curProfit, curMaxPrice = 0, prices[-1]

        for i in range(len(prices) - 2, -1, -1):
            if prices[i] > curMaxPrice:
                curMaxPrice = prices[i]
            else:
                curProfit = max(curProfit, curMaxPrice - prices[i])

        return curProfit


answer = Solution()
print(answer.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
