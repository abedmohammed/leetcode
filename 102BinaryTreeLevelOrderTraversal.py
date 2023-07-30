from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        if not root: return []

        ans = []
        nodesQueue = deque([root])

        while len(nodesQueue) > 0:
            subAns = []

            for i in range(len(nodesQueue)):
                if nodesQueue[0].left:
                    nodesQueue.append(nodesQueue[0].left)
                if nodesQueue[0].right:
                    nodesQueue.append(nodesQueue[0].right)

                subAns.append(nodesQueue.popleft().val)

            ans.append(subAns)

        return ans

node9 = TreeNode(9)
node15 = TreeNode(15)
node7 = TreeNode(7)
node20 = TreeNode(20, node15, node7)
node3 = TreeNode(3, node9, node20)

answer = Solution()
print(answer.levelOrder(node3))

