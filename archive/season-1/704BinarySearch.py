class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1


answer = Solution()
print(answer.search([-1, 0, 3, 5, 9, 12, 16], 16))
print(answer.search([-1, 0, 3, 5, 9, 12, 16], 2))
