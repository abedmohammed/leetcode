class Solution(object):
    def makeEqual(self, words):
        n = len(words)
        chars = {}

        for word in words:
            for char in word:
                chars[char] = chars.get(char, 0) + 1

        for char in chars:
            if chars[char] % n != 0:
                return False

        return True


answer = Solution()
print(answer.makeEqual(words=["abc", "aabc", "bc"]))
print(answer.makeEqual(words=["bc", "aaabc", "bc"]))
print(answer.makeEqual(words=["ab", "a"]))
