class Solution(object):
    def rotate(self, matrix):
        left, right = 0, len(matrix) - 1

        while left < right:
            top, bottom = left, right
            for i in range(right - left):
                temp = matrix[top][left + i]

                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top + i][right] = temp

            left += 1
            right -= 1

        return matrix


answer = Solution()
print(answer.rotate(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(
    answer.rotate(
        matrix=[[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    )
)
