class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        res = []
        subset = []

        def backtrack(i):
            if i == len(nums):
                res.append(subset[:])
                return

            subset.append(nums[i])
            backtrack(i + 1)

            subset.pop()
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)

        backtrack(0)
        return res


answer = Solution()
print(answer.subsetsWithDup([1, 2, 2]))
