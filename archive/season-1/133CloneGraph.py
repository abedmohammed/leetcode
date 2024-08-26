from collections import deque
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    # def cloneGraph(self, node):
    #     visited = {}
    #     copiedNodes = {}
    #     queue = deque()
    #     queue.append(node)
    #     copiedNodes[node.val] = Node(node.val)
    #     visited[node.val] = 1


    #     while queue:
    #         currentNode = queue.popleft()
    #         value = currentNode.val
    #         newNode = copiedNodes[value]

    #         for i in range(len(currentNode.neighbors)):
    #             neighbhor = currentNode.neighbors[i]
    #             if neighbhor.val not in copiedNodes:
    #                 copiedNodes[neighbhor.val] = Node(neighbhor.val)
    #             newNode.neighbors.append(copiedNodes[neighbhor.val])
    #             if neighbhor.val not in visited:
    #                 queue.append(neighbhor)
    #                 visited[neighbhor.val] = 1
        
    #     return copiedNodes[node.val]
        
    def cloneGraph(self, node):
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            newNode = Node(node.val)
            oldToNew[node] = newNode

            for neighbhor in node.neighbhors:
                addNode = dfs(neighbhor)
                newNode.neighbors.append(addNode)

            return newNode
        
        return dfs(node) if node else None


