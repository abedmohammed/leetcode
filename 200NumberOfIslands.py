from collections import deque

class Solution(object):
    def numIslands(self, grid):
        if not grid: return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            coords = deque([[r,c]])

            while coords:
                for i in range(len(coords)):
                    r, c = coords.popleft()

                    if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                        continue

                    grid[r][c] = "0"

                    coords.append([r-1, c])
                    coords.append([r, c+1])
                    coords.append([r+1, c])
                    coords.append([r, c-1])


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands

answer = Solution()
print(answer.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","1"]
]))
print(answer.numIslands([
  ["1","1"],
  ["0","0"]
]))