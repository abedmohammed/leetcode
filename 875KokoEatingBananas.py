class Solution(object):
    def minEatingSpeed(self, piles, h):
        def eatingIsViable(eatingSpeed):
            currentHours = 0
            for pile in piles:
                currentHours += -(-pile // eatingSpeed)
                if currentHours > h:
                    return False
            return True

        left, right = 1, max(piles)

        while left < right:
            middle = (right + left) // 2
            if eatingIsViable(middle):
                right = middle
            else:
                left = middle + 1

        return right


answer = Solution()
print(answer.minEatingSpeed([3, 6, 7, 11], 8))
print(answer.minEatingSpeed([30, 11, 23, 4, 20], 5))
print(answer.minEatingSpeed([30], 6))
