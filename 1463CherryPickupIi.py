class Solution(object):
    def cherryPickup(self, grid):
        ROWS, COLS = len(grid), len(grid[0])

        cache = {}

        def doubleDfs(i, j1, j2):
            if j1 < 0 or j2 < 0 or j1 >= COLS or j2 >= COLS:
                return float("-inf")
            elif i >= ROWS:
                return 0
            elif (i, j1, j2) in cache:
                return cache[(i, j1, j2)]

            maxPath = 0
            for dir1 in [-1, 0, 1]:
                for dir2 in [-1, 0, 1]:
                    maxPath = max(maxPath, doubleDfs(i + 1, j1 + dir1, j2 + dir2))

            maxPath += grid[i][j1]

            if j1 != j2:
                maxPath += grid[i][j2]

            cache[(i, j1, j2)] = maxPath

            return maxPath

        return doubleDfs(0, 0, COLS - 1)


# 26 minutes
answer = Solution()
print(answer.cherryPickup(grid=[[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]))
print(
    answer.cherryPickup(
        grid=[
            [1, 0, 0, 0, 0, 0, 1],
            [2, 0, 0, 0, 0, 3, 0],
            [2, 0, 9, 0, 0, 0, 0],
            [0, 3, 0, 5, 4, 0, 0],
            [1, 0, 2, 3, 0, 0, 6],
        ]
    )
)
