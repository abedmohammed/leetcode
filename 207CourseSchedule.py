class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        self.checked = {}

        self.nodes = {}

        for i in range(numCourses):
            self.nodes[i] = {}

        for requisite in prerequisites:
            startingNode = requisite[1]
            self.nodes[startingNode].update({requisite[0]: 1})

        self.hasCycle = False
        self.marked = {}
        for node in self.nodes:
            self.dfs(node, self.nodes[node])
            if self.hasCycle:
                return False
            self.marked = {}
            
        return True
    
    def dfs(self, node, children):
        if node in self.checked:
            return True
        if node in self.marked:
            self.hasCycle = True
            return False
        if not children:
            self.checked[node] = 1
            return True
        
        self.marked[node] = 1

        for childNode in children:
            if not self.dfs(childNode, self.nodes[childNode]):
                return False
            
        self.checked[node] = 1
        return True

answer = Solution()
print(answer.canFinish(5, [[0,2], [1,3], [4,3], [4, 1]]))