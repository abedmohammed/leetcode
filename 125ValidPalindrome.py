class Solution(object):
    def isPalindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.isValidCharacter(s[l]):
                l += 1
            while r > l and not self.isValidCharacter(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True

    def isValidCharacter(self, char):
        o = ord(char)
        return (
            (o <= ord("Z") and o >= ord("A"))
            or (o <= ord("z") and o >= ord("a"))
            or (o <= ord("9") and o >= ord("0"))
        )
