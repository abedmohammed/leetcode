class Solution(object):
    def getLengthOfOptimalCompression(self, s, k):
        dp = {}

        def count(i, k, prevChar, prevCount):
            if k < 0:
                return float("inf")
            elif i == len(s):
                return 0
            elif (i, k, prevChar, prevCount) in dp:
                return dp[(i, k, prevChar, prevCount)]

            if s[i] == prevChar:
                increment = 1 if prevCount in [1, 9, 99] else 0
                res = increment + count(i + 1, k, prevChar, prevCount + 1)
            else:
                res = min(
                    1 + count(i + 1, k, s[i], 1),
                    count(i + 1, k - 1, prevChar, prevCount + 1),
                )

            dp[(i, k, prevChar, prevCount)] = res

            return res

        return count(0, k, "", 0)


answer = Solution()
print(answer.getLengthOfOptimalCompression(s="aaabcccd", k=2))
