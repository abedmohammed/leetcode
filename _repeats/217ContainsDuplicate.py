class Solution(object):
    def containsDuplicate(self, nums):
        # numsSeen = set()

        # for num in nums:
        #     if num in numsSeen:
        #         return True

        #     numsSeen.add(num)

        # return False

        nums.sort()

        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                return True

        return False


answer = Solution()
print(answer.containsDuplicate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
