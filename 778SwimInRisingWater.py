import heapq


class Solution(object):
    def swimInWater(self, grid):
        minHeap = [(grid[0][0], 0, 0)]
        visited = set([grid[0][0]])
        cost, i, j = 0, 0, 0
        N = len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while minHeap:
            cost, i, j = heapq.heappop(minHeap)

            if i == N - 1 and j == N - 1:
                return cost

            for dr, dc in directions:
                di, dj = i + dr, j + dc

                if di < 0 or di >= N or dj < 0 or dj >= N or grid[di][dj] in visited:
                    continue
                visited.add(grid[di][dj])
                heapq.heappush(minHeap, (max(grid[di][dj], cost), di, dj))

        return cost


answer = Solution()
print(
    answer.swimInWater(
        [
            [0, 1, 2, 3, 4],
            [24, 23, 22, 21, 5],
            [12, 13, 14, 15, 16],
            [11, 17, 18, 19, 20],
            [10, 9, 8, 7, 6],
        ]
    )
)
print(answer.swimInWater([[7, 2], [1, 3]]))
