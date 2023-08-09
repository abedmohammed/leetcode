class Solution(object):
    def lengthOfLIS(self, nums):
        # n*2^n
        # self.maximum = 1

        # def dfs(i, total, current):
        #     if i >= len(nums):
        #         self.maximum = max(total, self.maximum)
        #         return


        #     if nums[i] > current:
        #         dfs(i + 1, total + 1, nums[i])
        #     dfs(i + 1, total, current)

        # for i in range(len(nums)):
        #     dfs(i, 1, nums[i])

        # return self.maximum
        
        # n^2
        dp = {float("inf"): 0}
        ans = float("-inf")

        for i in range(len(nums) - 1, -1, -1):
            maximum = 0
            for number in dp:
                if number > nums[i]:
                    maximum = max(maximum, dp[number])
            dp[nums[i]] = maximum + 1
            ans = max(maximum+1, ans)

        return ans
    



            

answer = Solution()
print(answer.lengthOfLIS([10,9,2,5,3,7,101,18]))
print(answer.lengthOfLIS([0,1,0,3,2,3]))
print(answer.lengthOfLIS([7,7,7,7,7,7,7]))
print(answer.lengthOfLIS([7]))