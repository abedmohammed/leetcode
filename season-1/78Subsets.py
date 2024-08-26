class Solution(object):
    def subsets(self, nums):
        # sets = [[]]
        # for num in nums:
        #     subset = []
        #     for set in sets:
        #         newSet = set[:]
        #         newSet.append(num)
        #         subset.append(newSet)

        #     for set in subset:
        #         sets.append(set)

        # return sets

        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset[:])
                return
            
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)

        dfs(0)
        return res

answer = Solution()
print(answer.subsets([1, 2, 3, 4]))