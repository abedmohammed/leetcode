import heapq

class Solution(object):
    def minMeetingRooms(self, intervals):
        intervals.sort()

        heap = []
        for start, end in intervals:
            if not heap or start < heap[0]:
                heapq.heappush(heap, end)
            else:
                heapq.heapreplace(heap, end)
        
        return len(heap)
                


answer = Solution()
print(answer.minMeetingRooms([[1,2],[2,3],[3,4]]))
print(answer.minMeetingRooms([[0,30],[5,10],[15,20]]))
print(answer.minMeetingRooms([[0,30]]))
