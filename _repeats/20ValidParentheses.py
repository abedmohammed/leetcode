class Solution(object):
    def isValid(self, s):
        brackets = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            elif stack and char == brackets[stack[-1]]:
                stack.pop()
            else:
                return False

        return True if not stack else False


answer = Solution()
print(answer.isValid(s="()[]{}}"))
