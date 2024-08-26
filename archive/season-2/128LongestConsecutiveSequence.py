class Solution(object):
    def longestConsecutive(self, nums):
        nums = set(nums)

        res = 0
        for num in nums:
            if num - 1 not in nums:
                length = 1
                while num + length in nums:
                    length += 1
                res = max(res, length)

        return res


answer = Solution()
print(answer.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print(answer.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
print(answer.longestConsecutive(nums=[5, 4, 3, 2, 1, 0]))
print(
    answer.longestConsecutive(
        nums=[1, 1, 1, 5, 4, 3, 2, 1, 0, 8, 10, 9, 15, 14, 13, 12, 11]
    )
)
