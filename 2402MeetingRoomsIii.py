import heapq


class Solution(object):
    def mostBooked(self, n, meetings):
        meetings.sort()

        rooms = [0] * n
        endHeap = []
        roomHeap = [i for i in range(n)]
        heapq.heapify(roomHeap)

        for start, end in meetings:
            # check if meetings finished before this starts
            while endHeap and endHeap[0][0] <= start:
                _, room = heapq.heappop(endHeap)
                heapq.heappush(roomHeap, room)

            # No meetings
            # some meetings
            if len(roomHeap) > 0:
                room = heapq.heappop(roomHeap)
                rooms[room] += 1
                heapq.heappush(endHeap, (end, room))
            else:
                # all meetings
                lastEnd, room = heapq.heappop(endHeap)
                rooms[room] += 1
                offset = lastEnd - start
                heapq.heappush(endHeap, (end + offset, room))

        res = 0
        for i in range(len(rooms)):
            if rooms[i] > rooms[res]:
                res = i

        return res


answer = Solution()
print(answer.mostBooked(n=2, meetings=[[0, 10], [1, 5], [2, 7], [3, 4]]))
print(answer.mostBooked(n=3, meetings=[[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]))
