class Solution(object):
    def findDuplicate(self, nums):
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        catchUp = 0

        while catchUp != slow:
            catchUp = nums[catchUp]
            slow = nums[slow]

        return catchUp


answer = Solution()
print(answer.findDuplicate([1, 3, 4, 2, 2]))
print(answer.findDuplicate([4, 3, 1, 4, 2]))
print(answer.findDuplicate([2, 2, 2, 2, 2, 2]))
