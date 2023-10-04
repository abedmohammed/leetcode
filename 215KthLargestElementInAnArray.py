import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]


answer = Solution()
print(answer.findKthLargest([3, 2, 1, 5, 6, 4], 2))
print(answer.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
