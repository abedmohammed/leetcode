class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda a: a[0])

        res, currentInterval = [], intervals[0]

        for i in range(1, len(intervals)):
            if currentInterval[1] < intervals[i][0]:
                res.append(currentInterval)
                currentInterval = intervals[i]
            else:
                currentInterval = [min(currentInterval[0], intervals[i][0]), max(currentInterval[1], intervals[i][1])]

        res.append(currentInterval)
        return res

answer = Solution()
print(answer.merge([[1,3],[2,6],[8,10],[15,18]]))
print(answer.merge([[1,3]]))
