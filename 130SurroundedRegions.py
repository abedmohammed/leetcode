class Solution(object):
    def solve(self, board):
        def dfs(i, j):
            if (
                i < 0
                or i >= len(board)
                or j < 0
                or j >= len(board[0])
                or board[i][j] != "O"
            ):
                return

            board[i][j] = "S"

            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i + 1, j)
            dfs(i, j - 1)

        # horizontal
        for col in range(len(board[0])):
            dfs(0, col)
            dfs(len(board) - 1, col)

        # vertical
        for row in range(len(board)):
            dfs(row, 0)
            dfs(row, len(board[0]) - 1)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "S":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"

        return board


answer = Solution()
print(
    answer.solve(
        [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"],
        ]
    )
)
