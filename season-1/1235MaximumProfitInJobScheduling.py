import bisect


class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        intervals = sorted(zip(startTime, endTime, profit))

        cache = {}

        def dfs(i):
            if i == len(intervals):
                return 0
            if i in cache:
                return cache[i]

            res = dfs(i + 1)

            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            cache[i] = res = max(res, intervals[i][2] + dfs(j))
            return res

        return dfs(0)


answer = Solution()
print(
    answer.jobScheduling(
        startTime=[1, 2, 3, 3], endTime=[3, 4, 5, 6], profit=[50, 10, 40, 70]
    )
)

print(
    answer.jobScheduling(
        startTime=[1, 2, 3, 4, 6],
        endTime=[3, 5, 10, 6, 9],
        profit=[20, 20, 100, 70, 60],
    )
)

print(
    answer.jobScheduling(
        startTime=[4, 2, 4, 8, 2],
        endTime=[5, 5, 5, 10, 8],
        profit=[1, 2, 8, 10, 4],
    )
)
