class Solution(object):
    def judgeCircle(self, moves):
        x = 0
        y = 0
        for move in moves:
            if(move == "U"):
                y += 1
            if(move == "D"):
                y -= 1
            if(move == "R"):
                x += 1
            if(move == "L"):
                x -= 1

        return x == 0 and y == 0

    

answer = Solution()
print(answer.judgeCircle("UDD"))

