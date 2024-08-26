from collections import defaultdict


class Solution(object):
    def findMatrix(self, nums):
        mem = defaultdict(int)
        ans = [[]]
        for num in nums:
            index = mem[num]

            if index >= len(ans):
                ans.append([])

            ans[index].append(num)

            mem[num] += 1
        return ans


answer = Solution()
print(answer.findMatrix(nums=[1, 3, 4, 1, 2, 3, 1]))
print(answer.findMatrix(nums=[1, 2, 3, 4]))
