from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder: return None

        head = TreeNode(preorder[0])

        mid = inorder.index(head.val)

        head.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        head.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return head




                
            

answer = Solution()
print(answer.buildTree([3,9,20,15,7], [9,3,15,20,7]))