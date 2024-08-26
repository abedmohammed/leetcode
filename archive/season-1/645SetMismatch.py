class Solution(object):
    def findErrorNums(self, nums):
        n = len(nums)
        curSum = 0
        seen = set()
        ans = []

        for i in range(len(nums)):
            if nums[i] in seen:
                ans.append(nums[i])
            else:
                seen.add(nums[i])
                curSum += nums[i]

        targetSum = n * (n + 1) / 2
        ans.append(int(targetSum - curSum))

        return ans


answer = Solution()
print(answer.findErrorNums(nums=[1, 2, 2, 4]))
