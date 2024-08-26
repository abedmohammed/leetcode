class Solution(object):
    def isValid(self, s):
        stack = []
        close = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in close:
                if len(stack) == 0 or stack.pop() != close[char]:
                    return False
            else:
                stack.append(char)
        
        return True if len(stack) == 0 else False
                
            

answer = Solution()
print(answer.isValid("[]"))