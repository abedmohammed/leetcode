class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rangeSumBST(self, root, low, high):
        # if not root:
        #     return 0

        # l = self.rangeSumBST(root.left, low, high)
        # r = self.rangeSumBST(root.right, low, high)

        # if root.val >= low and root.val <= high:
        #     return root.val + l + r

        # return l + r

        ans = [0]

        def dfs(node):
            if not node:
                return

            if node.val >= low and node.val <= high:
                ans[0] += node.val

            self.rangeSumBST(node.left, low, high)
            self.rangeSumBST(node.right, low, high)

        dfs(root)
        return ans[0]


answer = Solution()
print(answer.rangeSumBST(root=[10, 5, 15, 3, 7, None, 18], low=7, high=15))
