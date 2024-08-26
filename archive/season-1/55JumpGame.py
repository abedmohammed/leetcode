class Solution(object):
    def canJump(self, nums):
        dp = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= dp - i:
                dp = i
        
        return dp == 0
    
answer = Solution()
print(answer.canJump([2,3,1,1,4]))
print(answer.canJump([3,2,1,0,4]))
print(answer.canJump([2, 0]))
