class Solution(object):
    def maxCoins(self, piles):
        piles.sort(reverse=True)
        total = 0
        i = 0

        while i < len(piles):
            total += piles[i + 1]
            i += 2
            piles.pop()

        return total


answer = Solution()
print(answer.maxCoins(piles=[2, 4, 1, 2, 7, 8]))
print(answer.maxCoins(piles=[9, 8, 7, 6, 5, 1, 2, 3, 4]))
print(answer.maxCoins(piles=[9, 8, 7]))
