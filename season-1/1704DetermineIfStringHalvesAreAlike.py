class Solution(object):
    def halvesAreAlike(self, s):
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        a = 0
        b = 0

        for i in range(len(s) // 2):
            if s[i] in vowels:
                a += 1

        for i in range(len(s) // 2, len(s)):
            if s[i] in vowels:
                b += 1

        return a == b


answer = Solution()
print(answer.halvesAreAlike(s="ao"))
print(answer.halvesAreAlike(s="textbook"))
