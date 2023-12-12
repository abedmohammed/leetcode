class Solution(object):
    def transpose(self, matrix):
        ROWS, COLS = len(matrix), len(matrix[0])
        ans = []
        for j in range(COLS):
            row = []
            for i in range(ROWS):
                row.append(matrix[i][j])
            ans.append(row)
            row = []
            

        return ans


answer = Solution()
print(answer.transpose(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
