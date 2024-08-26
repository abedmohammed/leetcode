# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isBalanced(self, root):
        balanced = [True]

        def dfs(node):
            if not node or not balanced[0]:
                return -1

            left = dfs(node.left) + 1
            right = dfs(node.right) + 1

            if abs(left - right) > 1:
                balanced[0] = False

            return max(left, right)

        dfs(root)
        return balanced[0]
