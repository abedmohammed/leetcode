class Solution(object):
    def minCostClimbingStairs(self, cost):
        first, second = 0, 0

        for i in range(2, len(cost)):
            temp = second
            second = min(first + cost[i - 2], second + cost[i - 1])
            first = temp

        return min(first + cost[-2], second + cost[-1])


answer = Solution()
print(answer.minCostClimbingStairs([10, 15, 20]))
