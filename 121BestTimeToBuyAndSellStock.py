class Solution(object):
    def maxProfit(self, prices):
        maxProfit = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] >= prices[r]:
                l = r
            else:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            r += 1

        return maxProfit


answer = Solution()
print(answer.maxProfit([7,1,5,3,6,4]))
print(answer.maxProfit([7,2,5,3,6,1,8,4]))
print(answer.maxProfit([5,4,3,2,1]))
print(answer.maxProfit([1]))