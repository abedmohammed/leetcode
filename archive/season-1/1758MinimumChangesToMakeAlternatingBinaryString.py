class Solution(object):
    def minOperations(self, s):
        zeroStart = 0
        oneStart = 0

        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == "0":
                    oneStart += 1
                elif s[i] == "1":
                    zeroStart += 1
            if i % 2 != 0:
                if s[i] == "1":
                    oneStart += 1
                elif s[i] == "0":
                    zeroStart += 1

        return min(oneStart, zeroStart)


answer = Solution()
print(answer.minOperations("10010100"))
print(answer.minOperations("0010"))
