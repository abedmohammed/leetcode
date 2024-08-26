class Solution(object):
    def generateParenthesis(self, n):
        ans = []

        def backtrack(open, close, string):
            if open == close and close == n:
                ans.append(string)
                return
            
            if open < n:
                backtrack(open + 1, close, string + "(")
            if close < open:
                backtrack(open, close + 1, string + ")")

        backtrack(0, 0, "")
        return ans


answer = Solution()
print(answer.generateParenthesis(3))
print(answer.generateParenthesis(1))