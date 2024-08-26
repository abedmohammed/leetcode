class Solution(object):
    def isValidSudoku(self, board):
        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]
        grids = [[{} for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                character = board[i][j]
                if character != ".":
                    if character in rows[i]:
                        return False
                    rows[i][character] = 1

                    if character in cols[j]:
                        return False
                    cols[j][character] = 1

                    if character in grids[i // 3][j // 3]:
                        return False
                    grids[i // 3][j // 3][character] = 1

        return True


                    
answer = Solution()
print(answer.isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))