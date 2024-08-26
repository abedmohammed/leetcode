class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        subset = []

        def backtrack(i, curSum):
            if curSum == target:
                res.append(subset[:])
                return
            if i >= len(candidates) or curSum > target:
                return

            subset.append(candidates[i])
            backtrack(i + 1, curSum + candidates[i])

            subset.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, curSum)

        backtrack(0, 0)
        return res


answer = Solution()
print(answer.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
print(answer.combinationSum2([2, 5, 2, 1, 2], 5))
