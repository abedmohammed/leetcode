class Solution(object):
    def rotate(self, matrix):
        left, right = 0, len(matrix) - 1

        while left > right:
            for i in range(right - left):
                top, bottom = left, right


answer = Solution()
print(answer.rotate(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(
    answer.rotate(
        matrix=[[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    )
)
