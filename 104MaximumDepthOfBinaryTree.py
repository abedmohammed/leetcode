# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0

        # queue = deque([root])
        # counter = 0

        # while len(queue) > 0:
        #     counter += 1
        #     for i in range(len(queue)):
        #         node = queue.popleft()

        #         if node.left:
        #             queue.append(node.left)

        #         if node.right:
        #             queue.append(node.right)

        # return counter

        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)
