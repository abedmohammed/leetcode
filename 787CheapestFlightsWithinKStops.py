class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        # adjList = [[] for i in range(n)]
        # for fr, to, cost in flights:
        #     adjList[fr].append((to, cost))

        # minHeap = [[0, src, 0]]  # 0 cost, src start, 0 stops

        # while minHeap:
        #     cost, node, stops = heapq.heappop(minHeap)
        #     if node == dst:
        #         return cost

        #     for adjacentNode in adjList[node]:
        #         if stops + 1 > k and adjacentNode[0] != dst:
        #             continue
        #         heapq.heappush(
        #             minHeap, [cost + adjacentNode[1], adjacentNode[0], stops + 1]
        #         )

        # return -1

        prices = [float("inf") for i in range(n)]
        prices[src] = 0

        for i in range(k + 1):
            tempPrices = prices[:]

            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tempPrices[d]:
                    tempPrices[d] = prices[s] + p

            prices = tempPrices

        return prices[dst] if prices[dst] != float("inf") else -1


answer = Solution()
print(
    answer.findCheapestPrice(
        4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1
    )
)
print(answer.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1))
