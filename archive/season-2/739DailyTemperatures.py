class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            curIndex = -1
            while stack:
                if stack[-1][0] > temperatures[i]:
                    curIndex = stack[-1][1]
                    break
                else:
                    stack.pop()

            res[i] = curIndex - i if curIndex >= 0 else 0
            stack.append((temperatures[i], i))

        return res


answer = Solution()
print(answer.dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]))
