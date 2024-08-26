class Solution(object):
    def checkValidString(self, s):
        leftMin, leftMax = 0, 0  # range of VALID possiblities

        for c in s:
            if c == "(":
                leftMin += 1
                leftMax += 1

            elif c == ")":
                leftMin -= 1
                leftMax -= 1

            elif c == "*":
                leftMin -= 1
                leftMax += 1

            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0

        return leftMin == 0


answer = Solution()
print(answer.checkValidString(s="(*))"))
print(answer.checkValidString(s="(*)(*"))
print(answer.checkValidString(s="(*(*)*)"))
print(
    answer.checkValidString(
        s="((((( *(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
    )
)
