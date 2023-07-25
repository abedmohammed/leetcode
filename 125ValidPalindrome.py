class Solution(object):
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1

        while left <= right:
            while left < len(s) and not (self.isNum(s[left]) or self.isAlpha(s[left])):
                left += 1
            while right > 0 and not (self.isNum(s[right]) or self.isAlpha(s[right])):
                right -= 1

            if left > right:
                return True

            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        return True
    
    def isAlpha(self, char): 
        return ord(char) >= ord("A") and ord(char) <= ord("z") and not (ord(char) >= 91 and ord(char) <= 96)

    def isNum(self, char):
        return (ord(char) >= ord("0") and ord(char) <= ord("9"))
        

answer = Solution()
print(answer.isPalindrome(";;;;"))