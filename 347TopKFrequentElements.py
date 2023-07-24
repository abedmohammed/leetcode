class Solution(object):
    def topKFrequent(self, nums, k):
        ans, count = [], {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for n, c in count.items():
            freq[c].append(n)

        for i in range(len(nums), 0, -1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans

answer = Solution()
print(answer.topKFrequent([1, 1, 2, 2, 2, 3], 2))