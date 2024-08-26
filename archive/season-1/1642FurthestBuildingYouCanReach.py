import heapq


class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        # cache = {}

        # def dfs(i, bricks, ladders):
        #     if bricks < 0 or ladders < 0:
        #         return -1
        #     if i == len(heights) - 1:
        #         return i
        #     if (i, bricks, ladders) in cache:
        #         return cache[(i, bricks, ladders)]

        #     gap = heights[i + 1] - heights[i]

        #     res = i

        #     if gap <= 0:
        #         res = dfs(i + 1, bricks, ladders)
        #     else:
        #         res = max(
        #             dfs(i + 1, bricks - gap, ladders),
        #             dfs(i + 1, bricks, ladders - 1),
        #             res,
        #         )

        #     cache[(i, bricks, ladders)] = res
        #     return res

        # return dfs(0, bricks, ladders)

        heap = []
        brickSum = 0

        for i in range(len(heights) - 1):
            gap = heights[i + 1] - heights[i]

            if gap <= 0:
                continue
            else:
                heapq.heappush(heap, gap)

            if len(heap) > ladders:
                brickSum += heapq.heappop(heap)

                if brickSum > bricks:
                    return i

        return len(heights) - 1


answer = Solution()
print(answer.furthestBuilding(heights=[4, 2, 7, 6, 9, 14, 12], bricks=5, ladders=1))
print(
    answer.furthestBuilding(
        heights=[4, 12, 2, 7, 3, 18, 20, 3, 19], bricks=100, ladders=2
    )
)
