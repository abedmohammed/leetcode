from collections import Counter


class Solution(object):
    def minOperations(self, nums):
        occurences = Counter(nums)
        res = 0
        for occ in occurences.values():
            rem = occ % 3
            res += occ // 3

            if rem != 0:
                res += occ // 3 + 1
            if occ == 1:
                return -1

        return res

        # occurences = Counter(nums)
        # res = 0
        # for occ in occurences.values():
        #     if occ == 1:
        #         return -1
        #     res += -(-occ // 3)

        # return res


answer = Solution()
print(answer.minOperations(nums=[2, 3, 3, 2, 2, 4, 2, 3, 4]))
print(answer.minOperations(nums=[2, 1, 2, 2, 3, 3]))
print(
    answer.minOperations(
        [14, 12, 14, 14, 12, 14, 14, 12, 12, 12, 12, 14, 14, 12, 14, 14, 14, 12, 12]
    )
)
