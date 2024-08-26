class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        points.sort(key=lambda a: a[0])

        maxWidth = 0
        for i in range(1, len(points)):
            maxWidth = max(maxWidth, points[i][0] - points[i - 1][0])

        return maxWidth


answer = Solution()
print(answer.maxWidthOfVerticalArea([[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]))
