class Solution(object):
    def maxProfit(self, prices):
        res = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                res = max(res, prices[r] - prices[l])
            r += 1

        return res
