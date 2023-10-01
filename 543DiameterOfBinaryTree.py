class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = TreeNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = TreeNode(val)


class Solution(object):
    def diameterOfBinaryTree(self, root):
        ans = [0]

        def dfs(self, node):
            if not node:
                return -1

            left = dfs(node.left) + 1
            right = dfs(node.right) + 1

            ans[0] = max(ans[0], left + right)

            return max(left, right)

        dfs(root)
        return ans[0]
