class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxAncestorDiff(self, root):
        def dfs(node, small, large):
            if not node:
                return -1

            small = min(small, root.val)
            large = max(large, root.val)

            return max(
                abs(small - large),
                dfs(node.left, small, large),
                dfs(node.right, small, large),
            )

        return dfs(root, root.val, root.val)
