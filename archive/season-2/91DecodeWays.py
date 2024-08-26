class Solution(object):
    def numDecodings(self, s):
        minusTwo, minusOne = 1, 1

        if s[0] == "0":
            return 0

        for i in range(1, len(s)):
            if s[i] == "0":
                if s[i - 1] != "1" and s[i - 1] != "2":
                    return 0
                minusTwo, minusOne = minusOne, minusTwo
            elif s[i - 1] == "0":
                minusTwo = minusOne
            else:
                num = int(s[i - 1 : i + 1])
                if num <= 26:
                    minusTwo, minusOne = minusOne, minusOne + minusTwo
                else:
                    minusTwo = minusOne
            print(s[i], minusTwo, minusOne)
        return minusOne


answer = Solution()
print(answer.numDecodings("123123"))
