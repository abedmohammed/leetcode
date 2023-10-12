from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        # # DFS ALGORITHM
        # # DFS -> set in time grid how long it takes for orange to become infected (how many steps from original)
        # # override time if it is quicker than what is already there
        # # after each call stack finishes, empty the visited set
        # # go through entire grid and find biggest number

        # timeGrid = [
        #     [float("inf") for i in range(len(grid[0]))] for i in range(len(grid))
        # ]
        # visited = set()

        # def dfs(i, j, currTime):
        #     if (
        #         i < 0
        #         or i >= len(grid)
        #         or j < 0
        #         or j >= len(grid[0])
        #         or ((i, j) in visited and timeGrid[i][j] < currTime)
        #         or grid[i][j] != 1
        #     ):
        #         return

        #     visited.add((i, j))
        #     timeGrid[i][j] = min(timeGrid[i][j], currTime)

        #     currTime += 1
        #     dfs(i - 1, j, currTime)
        #     dfs(i, j + 1, currTime)
        #     dfs(i + 1, j, currTime)
        #     dfs(i, j - 1, currTime)

        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == 2:
        #             dfs(i - 1, j, 1)
        #             dfs(i, j + 1, 1)
        #             dfs(i + 1, j, 1)
        #             dfs(i, j - 1, 1)
        #             visited = set()
        # ans = 0

        # print(timeGrid)

        # for i in range(len(timeGrid)):
        #     for j in range(len(timeGrid[0])):
        #         if timeGrid[i][j] == float("inf") and grid[i][j] == 1:
        #             return -1
        #         elif timeGrid[i][j] != float("inf"):
        #             ans = max(ans, timeGrid[i][j])

        # return ans

        # # BFS METHOD

        queue = deque()
        time, fresh = 0, 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1

        while queue and fresh > 0:
            for _ in range(len(queue)):
                i, j = queue.popleft()

                for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    r, c = i + dr, j + dc
                    if (
                        r < 0
                        or r >= len(grid)
                        or c < 0
                        or c >= len(grid[0])
                        or grid[r][c] != 1
                    ):
                        continue
                    grid[r][c] = 2
                    queue.append((r, c))
                    fresh -= 1

            time += 1

        return time if fresh == 0 else -1


answer = Solution()
print(answer.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(answer.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
print(answer.orangesRotting([[0]]))
