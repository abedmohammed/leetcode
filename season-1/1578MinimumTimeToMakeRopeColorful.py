class Solution(object):
    def minCost(self, colours, neededTime):
        curCost, maxIterCost = 0, neededTime[0]

        for i in range(1, len(colours)):
            if colours[i] == colours[i - 1]:
                curCost += min(maxIterCost, neededTime[i])
                maxIterCost = max(maxIterCost, neededTime[i])
            else:
                maxIterCost = neededTime[i]

        return curCost


answer = Solution()
print(answer.minCost(colours="abaac", neededTime=[1, 2, 3, 4, 5]))
print(answer.minCost(colours="aabaa", neededTime=[1, 2, 3, 4, 1]))
print(answer.minCost(colours="abaaa", neededTime=[1, 2, 3, 4, 5]))
print(answer.minCost(colours="a", neededTime=[1]))
