class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        target_sum = n*(n+1)/2
        actual_sum = 0
        for num in nums:
            actual_sum += num
        return target_sum - actual_sum

answer = Solution()
print(answer.missingNumber([9,6,4,2,3,5,7,0,1]))