from collections import deque


class Solution(object):
    def wallsAndGates(self, rooms):
        queue = deque()
        time = 0

        ROWS, COLUMNS = len(rooms), len(rooms[0])

        for i in range(ROWS):
            for j in range(COLUMNS):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        while queue:
            time += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()

                for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    r, c = i + dr, j + dc
                    if (
                        r >= 0
                        and r < ROWS
                        and c >= 0
                        and c < COLUMNS
                        and rooms[r][c] > time
                    ):
                        queue.append((r, c))
                        rooms[r][c] = time

        return rooms


answer = Solution()
print(
    answer.wallsAndGates(
        [
            [2147483647, -1, 0, 2147483647],
            [2147483647, 2147483647, 2147483647, -1],
            [2147483647, -1, 2147483647, -1],
            [0, -1, 2147483647, 2147483647],
        ]
    )
)
