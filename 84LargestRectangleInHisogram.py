class Solution(object):
    def largestRectangleArea(self, heights):
        ans = 0
        stack = []

        for i, h in enumerate(heights):
            currIndex = i
            while stack and h <= stack[-1][0]:
                prevHeight, currIndex = stack.pop()
                ans = max(ans, prevHeight * (i - currIndex))

            stack.append((h, currIndex))

        while stack:
            prevHeight, currIndex = stack.pop()
            ans = max(ans, prevHeight * (len(heights) - currIndex))

        return ans


answer = Solution()
print(answer.largestRectangleArea([2, 1, 5, 6, 2, 3]))
print(answer.largestRectangleArea([1]))
print(answer.largestRectangleArea([1, 4]))
print(answer.largestRectangleArea([1, 1, 1, 1, 1, 4]))
print(answer.largestRectangleArea([1, 2, 1, 5, 6, 2, 3, 2, 6]))
