class Solution(object):
    def maxScore(self, s):
        count, res = 0, 0
        for char in s:
            if char == "1":
                count += 1

        for char in s[:-1]:
            if char == "0":
                count += 1
            else:
                count -= 1
            res = max(res, count)

        return res


answer = Solution()
print(answer.maxScore("011101"))
print(answer.maxScore("11"))
print(answer.maxScore("00"))
