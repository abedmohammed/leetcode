class Solution(object):
    def minCostClimbingStairs(self, cost):
        costTwoStep, costOneStep = 0, 0

        cur = 2

        while cur < len(cost):
            temp = costOneStep

            costOneStep = min(costOneStep + cost[cur - 1], costTwoStep + cost[cur - 2])
            costTwoStep = temp

            cur += 1

        return min(costOneStep + cost[cur - 1], costTwoStep + cost[cur - 2])
