class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()

        child, cookie = 0, 0
        res = 0

        while child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]:
                res += 1
                child += 1
            cookie += 1

        return res


answer = Solution()
print(answer.findContentChildren(g=[1, 2, 3], s=[1, 1]))
print(answer.findContentChildren(g=[1, 2], s=[1, 4, 2, 3]))
print(answer.findContentChildren(g=[1, 2, 4], s=[1, 4, 2, 3]))
print(answer.findContentChildren(g=[1, 2, 4, 6], s=[1, 4, 2, 3]))
