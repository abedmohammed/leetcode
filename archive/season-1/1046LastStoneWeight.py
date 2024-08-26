import heapq


class Solution(object):
    def lastStoneWeight(self, stones):
        stones = [-x for x in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)

            if y - x != 0:
                heapq.heappush(stones, -(y - x))

        return -heapq.heappop(stones) if stones else 0


answer = Solution()
print(answer.lastStoneWeight([3, 2, 1, 5, 6, 4]))
print(answer.lastStoneWeight([8, 8, 8, 7, 6]))
print(answer.lastStoneWeight([3, 2, 1, 5, 6, 4]))
print(answer.lastStoneWeight([3, 2, 1, 5, 6, 4]))
