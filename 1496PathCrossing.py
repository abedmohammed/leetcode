class Solution(object):
    def isPathCrossing(self, path):
        history = set()
        x, y = 0, 0
        history.add((x, y))

        for dir in path:
            if dir == "N":
                y += 1
            elif dir == "S":
                y -= 1
            elif dir == "W":
                x -= 1
            elif dir == "E":
                x += 1
            if (x, y) in history:
                return True
            history.add((x, y))

        return False


answer = Solution()
print(answer.isPathCrossing("NES"))
