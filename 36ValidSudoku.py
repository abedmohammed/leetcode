class Solution(object):
    def isValidSudoku(self, board):
        for i in range(9):
            seenRow = set()
            seenCol = set()
            for j in range(9):
                numberRow = board[i][j]
                numberCol = board[j][i]
                if numberRow != "." and numberRow in seenRow:
                    return False
                if numberCol != "." and numberCol in seenCol:
                    return False
                if numberRow != ".":
                    seenRow.add(numberRow)
                if numberCol != ".":
                    seenCol.add(numberCol)

        for grid in range(9):
            seen = set()
            gridRow = grid // 3
            gridCol = grid % 3
            for i in range(3):
                for j in range(3):
                    r = i + 3 * gridRow
                    c = j + 3 * gridCol
                    number = board[r][c]
                    if number == ".":
                        continue
                    if number in seen:
                        return False
                    seen.add(number)

        return True
