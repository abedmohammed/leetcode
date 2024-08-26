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
    def kthSmallest(self, root, k):
    #     ans = []

    #     self.inOrder(root, ans)
        
    #     return ans[k - 1]

    # def inOrder(self, root, vals):
    #     if root.left: self.inOrder(root.left, vals)
    #     vals.append(root.val)
    #     if root.right: self.inOrder(root.right, vals)

        n = 0
        stack = []
        cur = root
        
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right


# tree = TreeNode(6)
# tree.insert(2)
# tree.insert(8)
# tree.insert(0)
# tree.insert(4)
# tree.insert(7)
# tree.insert(9)
# tree.insert(3)
# tree.insert(5)

tree = TreeNode(6)
tree.insert(4)
tree.insert(2)
tree.insert(0)
tree.insert(3)

answer = Solution()
print(answer.kthSmallest(tree,2))