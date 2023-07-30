# Definition for a binary tree node.
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
    def isValidBST(self, root):
    #     ans = []

    #     self.inOrder(root, ans)

    #     for i in range(1, len(ans)):
    #         if ans[i] < ans[i-1]:
    #             return False
        
    #     return True

    # def inOrder(self, root, vals):
    #     if root.left: self.inOrder(root.left, vals)
    #     vals.append(root.val)
    #     if root.right: self.inOrder(root.right, vals)

      def valid(node, left, right):
          if not root: 
              return True
          
          if not (node.val > left and node.val < right):
              return False
          
          return valid(node.left, left, node.val) and valid(node.right, node.val, right)
      
      return valid(root, float("-inf"), float("inf"))

        
tree = TreeNode(6)
tree.insert(2)
tree.insert(8)
tree.insert(0)
tree.insert(4)
tree.insert(7)
tree.insert(9)
tree.insert(3)
tree.insert(5)

answer = Solution()
answer.inOrder(tree)