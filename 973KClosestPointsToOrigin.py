import heapq
import math


class Solution(object):
    def kClosest(self, points, k):
        heap = []

        for coords in points:
            distance = coords[0] ** 2 + coords[1] ** 2
            heap.append((distance, coords))

        ans = []
        heapq.heapify(heap)
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans


answer = Solution()
print(answer.kClosest([[1, 3], [-2, 2]], 1))
