class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        res = []
        currInterval = intervals[0]

        for start, end in intervals[1:]:
            curStart, curEnd = currInterval

            if start <= curEnd:
                currInterval = [curStart, max(end, curEnd)]
            else:
                res.append(currInterval)
                currInterval = [start, end]

        res.append(currInterval)

        return res


answer = Solution()
print(answer.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
