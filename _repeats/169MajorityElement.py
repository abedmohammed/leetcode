class Solution(object):
    def majorityElement(self, nums):
        # res = nums[0]
        # seen = {}

        # for num in nums:
        #     seen[num] = seen.get(num, 0) + 1
        #     res = max(seen[num], res)

        # return res

        curNum, curCount = nums[0], 1

        for num in nums:
            if curNum == num:
                curCount += 1
            else:
                curCount -= 1

            if curCount == 0:
                curNum = num

        return curNum


answer = Solution()
print(answer.majorityElement(nums=[3, 2, 3]))
