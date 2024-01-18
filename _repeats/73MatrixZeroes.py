class Solution(object):
    def setZeroes(self, matrix):
        ROW, COL = len(matrix), len(matrix[0])

        def setCrossX(i, j):
            for r in range(ROW):
                if matrix[r][j] != 0:
                    matrix[r][j] = "x"

            for c in range(COL):
                if matrix[i][c] != 0:
                    matrix[i][c] = "x"

        for i in range(ROW):
            for j in range(COL):
                if matrix[i][j] == 0:
                    setCrossX(i, j)

        for i in range(ROW):
            for j in range(COL):
                if matrix[i][j] == "x":
                    matrix[i][j] = 0


answer = Solution()
print(answer.setZeroes(matrix=[[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
print(answer.setZeroes(matrix=[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
