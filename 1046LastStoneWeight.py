import heapq


class Solution(object):
    def lastStoneWeight(self, stones):
        maxHeap = [-stones[i] for i in range(len(stones))]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            rock1 = heapq.heappop(maxHeap)
            rock2 = heapq.heappop(maxHeap)

            if rock1 == rock2:
                continue

            heapq.heappush(maxHeap, rock1 - rock2)

        return -heapq.heappop(maxHeap) if len(maxHeap) == 1 else 0
