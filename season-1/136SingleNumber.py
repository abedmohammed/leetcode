class Solution(object):
    def singleNumber(self, nums):
        xor = 0

        for num in nums:
            xor ^= num

        return xor

answer = Solution()
print(answer.singleNumber([2, 2, 1]))

