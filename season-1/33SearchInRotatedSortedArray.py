class Solution(object):
    def search(self, nums, target):
        length = len(nums)
        l, r = 0, length - 1

        while l <= r:
            mid = (l + r)//2

            if target == nums[mid]: return mid

            # IN LEFT PORTION OF ROTATION
            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # IN RIGHT PORTION OF ROTATION
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1
          

answer = Solution()
print(answer.search([9, 0, 1, 2, 3, 4, 5], 1))