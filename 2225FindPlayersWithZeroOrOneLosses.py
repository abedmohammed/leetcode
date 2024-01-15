class Solution(object):
    def findWinners(self, matches):
        losses = {}

        for winner, loser in matches:
            losses[winner] = losses.get(winner, 0)
            losses[loser] = losses.get(loser, 0) + 1

        zero = []
        one = []

        for player in losses:
            if losses[player] == 0:
                zero.append(player)
            elif losses[player] == 1:
                one.append(player)

        zero.sort()
        one.sort()

        return [zero, one]


answer = Solution()
print(
    answer.findWinners(
        matches=[
            [1, 3],
            [2, 3],
            [3, 6],
            [5, 6],
            [5, 7],
            [4, 5],
            [4, 8],
            [4, 9],
            [10, 4],
            [10, 9],
        ]
    )
)
