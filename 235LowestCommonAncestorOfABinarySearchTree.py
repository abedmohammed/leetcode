# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        # if p.val >= root.val and q.val <= root.val or q.val >= root.val and p.val <= root.val:
        #     return root
        # elif p.val > root.val and q.val > root.val:
        #     return self.lowestCommonAncestor(root.right, p, q)
        # elif p.val < root.val and q.val < root.val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        # return False
    
        curr = root

        while curr:
          if p.val > curr.val and q.val > curr.val:
              curr = curr.right
          elif p.val < curr.val and q.val < curr.val:
              curr = curr.left
          else:
              return curr