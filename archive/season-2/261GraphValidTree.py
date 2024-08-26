class Solution(object):
    def validTree(self, n, edges):
        adjList = [[] for _ in range(n)]

        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        marked = set()

        def dfs(node, pred):
            if node in marked:
                return False

            marked.add(node)

            for adjNode in adjList[node]:
                if adjNode != pred:
                    if not dfs(adjNode, node):
                        return False

            return True

        res = dfs(0, 0)

        return res if len(marked) == n else False
