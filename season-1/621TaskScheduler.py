import heapq
from collections import deque, Counter


class Solution(object):
    def leastInterval(self, tasks, n):
        count = Counter(tasks)  # O(N)
        frequencyHeap = [-frq for frq in count.values()]  # O(N)
        heapq.heapify(frequencyHeap)  # O(N)

        time = 0
        addbackQueue = deque()

        while frequencyHeap or addbackQueue:
            time += 1

            if addbackQueue and addbackQueue[0][1] < time:
                heapq.heappush(frequencyHeap, -addbackQueue.popleft()[0])

            if frequencyHeap:
                currentTask = -heapq.heappop(frequencyHeap)
                if currentTask > 1:
                    addbackQueue.append((currentTask - 1, time + n))

        return time


answer = Solution()
print(answer.leastInterval(["A", "A", "A", "B", "B", "B"], 2))
print(
    answer.leastInterval(
        ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2
    )
)
