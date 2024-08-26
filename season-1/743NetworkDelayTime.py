import heapq


class Solution(object):
    def networkDelayTime(self, times, n, k):
        adjMap = [[] for i in range(n + 1)]
        for u, v, w in times:
            adjMap[u].append((v, w))

        minHeap = [(0, k)]
        visited = set([k])
        cost = 0
        while minHeap and len(visited) != n:
            cost, currNode = heapq.heappop(minHeap)
            visited.add(currNode)
            for v, w in adjMap[currNode]:
                if v in visited:
                    continue
                heapq.heappush(minHeap, (cost + w, v))

        return cost if len(visited) == n else -1


answer = Solution()
print(answer.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
print(answer.networkDelayTime([[1, 2, 1]], 2, 2))
print(answer.networkDelayTime([[1, 2, 1], [2, 3, 2], [1, 3, 4]], 3, 1))
print(answer.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1], [3, 5, 2]], 5, 2))
