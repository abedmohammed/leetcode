class Solution(object):
    def permute(self, nums):
        self.ans = []
        self.backtrackPermutations([], set(nums))

        return self.ans

    def backtrackPermutations(self, curr, integerSet):
        if not integerSet:
            self.ans.append(curr)

        for num in integerSet:
            newSet, newArr = set(integerSet), curr[:]
            newSet.remove(num)
            newArr.append(num)

            self.backtrackPermutations(newArr, newSet)


answer = Solution()
print(answer.permute([1, 2, 3, 4]))
