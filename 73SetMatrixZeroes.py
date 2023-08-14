class Solution(object):
    def setZeroes(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    self.setColsAndRows(matrix, i, j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "x":
                      matrix[i][j] = 0


        return matrix

    def setColsAndRows(self, matrix, row, col):
        matrix[row][col] = "x"
        # Set row to symbol
        for i in range(len(matrix[0])):
            if matrix[row][i] != 0:
                matrix[row][i] = "x"

        # Set column to symbol
        for i in range(len(matrix)):
            if matrix[i][col] != 0:
                matrix[i][col] = "x"

        return matrix
answer = Solution()
print(answer.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
print(answer.setZeroes([[1],[0],[1]]))
print(answer.setZeroes([[1, 0, 1]]))
print(answer.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))