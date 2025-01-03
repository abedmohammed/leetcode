# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTree(self, root):
        if not root:
            return None

        # queue = deque([root])

        # while len(queue) > 0:
        #     for i in range(len(queue)):
        #         node = queue.popleft()

        #         temp = node.left
        #         node.left = node.right
        #         node.right = temp

        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)

        # return root

        temp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)

        return root
