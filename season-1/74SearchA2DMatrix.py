class Solution(object):
    def searchMatrix(self, matrix, target):
        rows, columns = len(matrix), len(matrix[0])
        l = 0
        r = rows * columns - 1
        while l <= r:
            mid = (l + r) // 2
            num = matrix[mid // columns][mid % columns]

            if num == target:
                return True
            elif num > target:
                r = mid - 1
            else:
                l = mid + 1

        return False


answer = Solution()
print(answer.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 16))
print(answer.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 7))
