from math import sqrt

class Solution(object):
    def climbStairs(self, n):
        return int((((1+sqrt(5))**(n+1))-((1-sqrt(5)))**(n+1))//(2**(n+1)*sqrt(5)))

answer = Solution()
print(answer.climbStairs(5))