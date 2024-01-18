class Solution(object):
    def climbStairs(self, n):
        twoStep = 0
        oneStep = 1

        for i in range(n):
            temp = oneStep + twoStep
            twoStep = oneStep
            oneStep = temp

        return oneStep
