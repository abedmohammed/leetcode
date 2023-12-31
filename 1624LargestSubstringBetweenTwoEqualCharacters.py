class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        history, res = {}, -1

        for i, c in enumerate(s):
            if c not in history:
                history[c] = i
            else:
                res = max(res, i - history[c] - 1)

        return res


answer = Solution()
print(answer.maxLengthBetweenEqualCharacters(s="aa"))
print(answer.maxLengthBetweenEqualCharacters(s="abca"))
print(answer.maxLengthBetweenEqualCharacters(s="abcabca"))
print(answer.maxLengthBetweenEqualCharacters(s="abcdefg"))
