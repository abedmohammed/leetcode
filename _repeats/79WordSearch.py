class Solution(object):
    def exist(self, board, word):
        ROWS, COLS = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def backtrack(i, j, word):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS:
                return False
            if board[i][j] == "#":
                return False
            if board[i][j] != word[0]:
                return False
            if len(word) == 1:
                return True

            temp = board[i][j]
            board[i][j] = "#"

            for di, dj in directions:
                r, c = i + di, j + dj

                if backtrack(r, c, word[1:]):
                    return True

            board[i][j] = temp

            return False

        for i in range(ROWS):
            for j in range(COLS):
                if backtrack(i, j, word):
                    return True

        return False


answer = Solution()
print(
    answer.exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="ABCCED",
    )
)
print(
    answer.exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="ABCB",
    )
)
print(
    answer.exist(
        board=[["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]],
        word="ABCEFSADEESE",
    )
)
