class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        if len(points) <= 1:
            return 0

        totalTime = 0

        for i in range(1, len(points)):
            x1, y1 = points[i - 1]
            x2, y2 = points[i]

            horizontal = abs(x1 - x2)
            vertical = abs(y1 - y2)

            # diagonalMoves = min(horizontal, vertical)
            # singularMoves = max(horizontal, vertical) - diagonalMoves
            # totalTime += diagonalMoves + singularMoves
            # totalTime += min(horizontal, vertical) + max(horizontal, vertical) - min(horizontal, vertical) = max(horizontal, vertical)

            totalTime += max(horizontal, vertical)

        return totalTime


answer = Solution()
print(answer.minTimeToVisitAllPoints(points=[[1, 1], [3, 4], [-1, 0]]))
print(answer.minTimeToVisitAllPoints(points=[[3, 2], [-2, 2]]))
