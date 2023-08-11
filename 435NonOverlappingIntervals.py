class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda a: a[0])
        currentEnd = intervals[0][1]
        ans = 0

        for start, end in intervals[1:]:
            if start >= currentEnd:
                currentEnd = end
            else:
                currentEnd = min(end, currentEnd)
                ans += 1
        return ans



answer = Solution()
print(answer.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(answer.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(answer.eraseOverlapIntervals([[1,3]]))
print(answer.eraseOverlapIntervals([[1,3], [2,4], [3,6], [4,7], [1,10], [9,10]]))
print(answer.eraseOverlapIntervals([[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]))


