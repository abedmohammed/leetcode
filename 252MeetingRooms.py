class Solution(object):
    def canAttendMeetings(self, intervals):
        if not intervals: return True
        intervals.sort(key=lambda a: a[0])
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prevEnd:
                return False
            prevEnd = end
        
        return True


answer = Solution()
print(answer.canAttendMeetings([[1,2],[2,3],[3,4]]))
print(answer.canAttendMeetings([]))
