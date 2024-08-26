class Solution(object):
    def largestOddNumber(self, num):
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 != 0:
                return num[: i + 1]
        return ""


answer = Solution()
print(answer.largestOddNumber(num="35427"))
print(answer.largestOddNumber(num="52"))
print(answer.largestOddNumber(num="4206"))
