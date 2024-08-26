from collections import Counter
import heapq


class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        frequency = Counter(arr)

        # heap = list(frequency.values())

        # heapq.heapify(heap)

        # while heap and k - heap[0] >= 0:
        #     k -= heapq.heappop(heap)

        # return len(heap)

        buckets = [0] * (len(arr) + 1)

        for val in frequency.values():
            buckets[val] += 1

        for i in range(1, len(buckets)):
            if k >= buckets[i] * i:
                k -= buckets[i] * i
                buckets[i] = 0
            else:
                buckets[i] -= k // i
                break

        return sum(buckets)


answer = Solution()
print(answer.findLeastNumOfUniqueInts(arr=[4, 3, 1, 1, 3, 3, 2], k=3))
print(answer.findLeastNumOfUniqueInts(arr=[5, 5, 4], k=1))
