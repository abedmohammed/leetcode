from collections import Counter
import heapq


class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize != 0:
            return False

        hashMap = Counter(hand)

        minHeap = list(set(hand))
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]
            for i in range(first, groupSize + first):
                if i not in hashMap:
                    return False

                hashMap[i] -= 1

                if hashMap[i] == 0:
                    if minHeap[0] == i:
                        heapq.heappop(minHeap)
                    else:
                        return False

        return True


answer = Solution()
print(answer.isNStraightHand(hand=[1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize=3))
print(answer.isNStraightHand(hand=[1, 2, 3, 4, 5, 6], groupSize=2))
