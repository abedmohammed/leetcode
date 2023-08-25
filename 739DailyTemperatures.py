class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = []
        ans = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[i] >= stack[-1][0]:
                stack.pop()
            
            if not stack:
                stack.append([temperatures[i], i])
            
            ans[i] = stack[-1][1] - i
            stack.append([temperatures[i], i])

        return ans
            

answer = Solution()
print(answer.dailyTemperatures([73,74,75,71,69,72,76,73]))
print(answer.dailyTemperatures([30,40,50,60]))
print(answer.dailyTemperatures([30,60,90]))
print(answer.dailyTemperatures([90, 60, 30, 100]))