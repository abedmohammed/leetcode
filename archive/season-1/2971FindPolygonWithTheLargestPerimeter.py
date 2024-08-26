class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort()
        total = sum(nums)

        for i in range(len(nums) - 1, -1, -1):
            currNum, otherTotal = nums[i], total - nums[i]

            if currNum < otherTotal:
                return total
            else:
                total = otherTotal

        return -1


answer = Solution()
print(answer.largestPerimeter(nums=[1, 12, 1, 2, 5, 50, 3]))
print(answer.largestPerimeter(nums=[5, 5, 50, 51]))
