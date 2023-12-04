# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def kthSmallest(self, root, k):
        def inOrderDFS(node, curPositon, k):
            if not node:
                return (False, 0)

            leftDFS = inOrderDFS(node.left, curPositon, k)
            if leftDFS[0] == True:
                return leftDFS
            else:
                curPosition += leftDFS[1] + 1

            if curPositon == k:
                return (True, node.val)

            rightDFS = inOrderDFS(node.right, curPositon, k)
            if rightDFS[0] == True:
                return rightDFS
            else:
                curPositon += rightDFS[1]

            return (False, curPositon)

        return inOrderDFS(root, 0, k)[1]
