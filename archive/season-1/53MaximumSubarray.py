class Solution(object):
    def maxSubArray(self, nums):
        ans = nums[0]
        curSum = 0

        for num in nums:
            if curSum < 0:
                curSum = 0

            curSum += num
            ans = max(ans, curSum)

        return ans

answer = Solution()
print(answer.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
