class Solution(object):
    def numberOfWays(self, corridor):
        # # O(n) time, O(1) space, not as fast
        # MOD = 10**9 + 7
        # left, right = 0, -1
        # currChairs = 0
        # res, numberOfChairs = 1, 0

        # while left < len(corridor) and right < len(corridor) - 1:
        #     right += 1

        #     if corridor[right] == "S":
        #         numberOfChairs += 1

        #         if currChairs < 2:
        #             currChairs += 1

        #         elif currChairs == 2:
        #             res *= right - left
        #             currChairs = 1

        #         left = right

        # if numberOfChairs % 2 != 0 or numberOfChairs == 0:
        #     return 0

        # return res % MOD

        # # O(n) O(n) even faster
        MOD = 10**9 + 7
        seats = []
        for i, c in enumerate(corridor):
            if c == "S":
                seats.append(i)

        length = len(seats)
        if length < 2 or length % 2 == 1:
            return 0

        res, i = 1, 1

        while i < length - 1:
            res *= seats[i + 1] - seats[i]
            i += 2

        return res % MOD


answer = Solution()
print(answer.numberOfWays(corridor="SSPPSPS"))
print(answer.numberOfWays(corridor="SSPPSPPPSPPPSPS"))
