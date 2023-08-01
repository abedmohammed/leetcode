# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxPathSum(self, root):
        self.ans = float("-inf")

        def getMaximum(root):
            if not root: return 0

            left = getMaximum(root.left)
            right = getMaximum(root.right)

            if left < 0: left = 0
            if right < 0: right = 0

            self.ans = max(self.ans, root.val + left + right)

            return root.val + max(left,right)
            
        getMaximum(root)    
        return self.ans