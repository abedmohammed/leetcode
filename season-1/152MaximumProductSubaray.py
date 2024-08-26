class Solution(object):
    def maxProduct(self, nums):
        ans = max(nums)
        currentMax, currentMin = 1, 1

        for num in nums:
            if num == 0:
                currentMax, currentMin = 1, 1
            
            temp = currentMax
            currentMax = max(num * currentMax, num * currentMin, num)
            currentMin = min(num * temp, num * currentMin, num)

            ans = max(ans, currentMax)

        return ans

            
                

answer = Solution()
print(answer.maxProduct([2,3,-2,4]))
print(answer.maxProduct([0,2]))