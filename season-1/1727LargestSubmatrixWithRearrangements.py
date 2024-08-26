class Solution(object):
    def largestSubmatrix(self, matrix):
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    matrix[i][j] = 1 + matrix[i - 1][j]

        res = 0
        for i in range(len(matrix)):
            matrix[i].sort(reverse=True)
            for j in range(len(matrix[0])):
                res = max(res, matrix[i][j] * (j + 1))

        return res


answer = Solution()
print(answer.largestSubmatrix(matrix=[[0, 0, 1], [1, 1, 1], [1, 0, 1]]))
print(answer.largestSubmatrix(matrix=[[1, 0, 1], [0, 1, 0], [1, 0, 1]]))
print(answer.largestSubmatrix(matrix=[[1, 1, 1], [1, 1, 1], [1, 1, 1]]))
print(answer.largestSubmatrix(matrix=[[1, 1, 1]]))
print(answer.largestSubmatrix(matrix=[[1], [1], [1]]))
