class Solution(object):
    def rotate(self, matrix):
        # for i in range(len(matrix)//2):
        #     for j in range(i, len(matrix) - i - 1):
        #         save = matrix[i][j]
        #         for k in range(4):
        #             if k == 0:
        #                 temp = matrix[j][len(matrix) - 1 - i]
        #                 matrix[j][len(matrix) - 1 - i] = save
        #                 save = temp
        #             if k == 1:
        #                 temp = matrix[len(matrix) - 1 - i][len(matrix) - 1 - j]
        #                 matrix[len(matrix) - 1 - i][len(matrix) - 1 - j] = save
        #                 save = temp
        #             if k == 2:
        #                 temp = matrix[len(matrix) - 1 - j][i]
        #                 matrix[len(matrix) - 1 - j][i] = save
        #                 save = temp
        #             if k == 3:
        #                 temp = matrix[i][j]
        #                 matrix[i][j] = save
        #                 save = temp
        # for row in matrix:
        #     print(row)

        # return matrix
                
        l, r = 0, len(matrix) - 1

        while l < r:
            top, bottom = l, r
            for i in range(r - l):
                topLeft = matrix[top][l+i]

                matrix[top][l+i] = matrix[bottom-i][l]
                matrix[bottom-i][l] = matrix[bottom][r - i]
                matrix[bottom][r - i] = matrix[top + i][r]
                matrix[top + i][r] = topLeft

            l += 1
            r -= 1

        return matrix
                
                
answer = Solution()
print(answer.rotate([[1,2,3],[4,5,6],[7,8,9]]))
# print(answer.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
