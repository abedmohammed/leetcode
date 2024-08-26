from collections import Counter


class Solution(object):
    def isAnagram(self, s, t):
        sCount = Counter(s)

        for char in t:
            if char not in sCount:
                return False

            sCount[char] -= 1

        for char in sCount:
            if sCount[char] != 0:
                return False

        return True


answer = Solution()
print(answer.isAnagram(s="anagram", t="nagaram"))
