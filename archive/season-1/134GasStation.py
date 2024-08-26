class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) - sum(cost) < 0:
            return -1

        total = 0
        start = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                start = i + 1

        return start


answer = Solution()
print(answer.canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))
print(answer.canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]))
