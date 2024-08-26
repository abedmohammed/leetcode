class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        courses = [set() for i in range(numCourses)]
        done = set()
        visited = set()

        for ai, bi in prerequisites:
            courses[ai].add(bi)

        ans = []
        cycle = [False]

        def dfs(c):
            if c in done:
                return
            elif c in visited:
                cycle[0] = True
                return

            visited.add(c)

            for child in courses[c]:
                dfs(child)

            visited.remove(c)

            done.add(c)
            ans.append(c)

        for i in range(numCourses):
            dfs(i)
            if cycle[0]:
                return []

        return ans


answer = Solution()
print(answer.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
print(answer.findOrder(5, [[1, 0], [2, 0], [3, 1], [3, 2], [2, 4]]))
