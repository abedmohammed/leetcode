from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        res = []
        mdQueue = deque()

        for i in range(len(nums)):
            while mdQueue and nums[mdQueue[-1]] <= nums[i]:
                mdQueue.pop()

            mdQueue.append(i)

            if mdQueue[0] == i - k:
                mdQueue.popleft()

            if i - k + 1 >= 0:
                res.append(nums[mdQueue[0]])
        
        return res