import heapq


class KthLargest(object):
    def __init__(self, k, nums):
        self.heap = []
        self.k = k
        for i in range(len(nums)):
            if i < k:
                heapq.heappush(self.heap, nums[i])
            else:
                self.add(nums[i])

    def add(self, val):
        if not self.heap or len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val >= self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)

        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(3, [4, 5, 8, 2])
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))
