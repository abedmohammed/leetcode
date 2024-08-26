from collections import deque


class Solution(object):
    def rearrangeArray(self, nums):
        # pos, neg = deque(), deque()

        # for num in nums:
        #     if num > 0:
        #         pos.append(num)
        #     else:
        #         neg.append(num)

        # for i in range(len(nums)):
        #     if i % 2 == 0:
        #         nums[i] = pos.popleft()
        #     else:
        #         nums[i] = neg.popleft()

        # return nums

        res = [0] * len(nums)
        pos, neg = 0, 1

        for i in range(len(nums)):
            if nums[i] > 0:
                res[pos] = nums[i]
                pos += 2
            else:
                res[neg] = nums[i]
                neg += 2

        return res


answer = Solution()
print(answer.rearrangeArray(nums=[3, 1, -2, -5, 2, -4]))
