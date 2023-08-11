class Solution(object):
    def insert(self, intervals, newInterval):
        # ans = []
        # combined = []
        # i = 0

        # # Find start interval of new interval
        # while i < len(intervals):
        #     start = newInterval[0]

        #     # Before
        #     if start < intervals[i][0]:  
        #         combined.append(start)
        #         break
        #     # In Between
        #     elif intervals[i][0] <= start <= intervals[i][1]:
        #         combined.append(intervals[i][0])
        #         break
        #     # After
        #     else:
        #         ans.append(intervals[i])
        #         i += 1  

        # if not combined:
        #     combined.append(newInterval[0])

        # # Find end interval of new interval
        # while i < len(intervals):
        #     end = newInterval[1]

        #     # Before
        #     if end < intervals[i][0]:
        #         combined.append(end)
        #         break
        #     # In Between
        #     elif intervals[i][0] <= end <= intervals[i][1]:
        #         combined.append(intervals[i][1])
        #         i += 1
        #         break
        #     # After
        #     else:
        #         i += 1  

        # if len(combined) < 2:
        #     combined.append(newInterval[1])
        # ans.append(combined)

        # return ans + intervals[i:]

        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
              res.append(newInterval)
              return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
              res.append(intervals[i])
            else:
              newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]

        res.append(newInterval)
        return res
          

answer = Solution()
print(answer.insert([[1,3],[6,9]], [2,5]))
print(answer.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
print(answer.insert([[1,5]], [2,7]))
print(answer.insert([], [4,8]))
