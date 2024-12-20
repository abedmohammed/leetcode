class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        # # BASE SOLUTION
        letterCount = {}

        for letter in s:
            letterCount[letter] = letterCount.get(letter, 0) + 1

        for letter in t:
            if letter not in letterCount:
                return False
            letterCount[letter] -= 1

            if letterCount[letter] <= 0:
                letterCount.pop(letter)

        return True if len(letterCount) == 0 else False

        # # CHEATING
        # return Counter(s) == Counter(t)

        # # SORTING
        # return sorted(s) == sorted(t)
