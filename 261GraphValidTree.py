class Solution(object):
    def validTree(self, n, edges):
        nodes = {i: [] for i in range(n)}
        valid = {}
        visited = {}

        def dfs(node, children, prev):
            if node in visited:
                return False
            if node in valid:
                return True
            if not children:
                visited[node] = 1
                return True
            
            visited[node] = 1

            for childNode in children:   
                if childNode == prev:
                    continue  
                if not dfs(childNode, nodes[childNode], node):
                    return False
                valid[childNode] = 1

            return True

        for edge in edges:
            nodes[edge[0]].append(edge[1])
            nodes[edge[1]].append(edge[0])


        if not dfs(0, nodes[0], -1):
          return False
            

        return len(valid) == n-1
                



answer = Solution()
print(answer.validTree(5, [[0,1],[0,2],[0,3],[1,4]]))
print(answer.validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]]))
print(answer.validTree(3, [[1,0],[2,0]]))