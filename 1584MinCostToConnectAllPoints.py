import heapq


class Solution(object):
    def minCostConnectPoints(self, points):
        N = len(points)

        # Create adjacency list
        adj = {i: [] for i in range(N)}

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # Prim's Algorithm
        res = 0
        visit = set()
        minHeap = [[0, 0]]
        while len(visit) < N:
            cost, i = heapq.heappop(minHeap)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minHeap, [neiCost, nei])

        return res


answer = Solution()
print(answer.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
