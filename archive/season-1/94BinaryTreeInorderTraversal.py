# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        # output = []

        # def dfs(node):
        #     if not node:
        #         return

        #     dfs(node.left)
        #     output.append(node.val)
        #     dfs(node.right)

        # return output

        output = []
        stack = []
        node = root

        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            output.append(node)
            node = node.right

        return output
