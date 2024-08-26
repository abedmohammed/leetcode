from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root):
        queue = deque([root])
        res = []
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                if not node:
                    continue
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            if level:
                res.append(level)

        return res
