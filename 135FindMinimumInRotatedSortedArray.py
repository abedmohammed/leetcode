class Solution(object):
    def findMin(self, nums):
        length = len(nums)
        l, r = 0, length - 1

        while l < r:
            if nums[l] < nums[r]: return nums[l]

            mid = (l + r)//2
            if nums[mid] < nums[l]:
                r = mid
            else:
                l = mid + 1
            
        return nums[r]

answer = Solution()
print(answer.findMin([16, 42, -7, -3, 8]))