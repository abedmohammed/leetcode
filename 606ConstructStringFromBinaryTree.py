# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def tree2str(self, root):
        if not root:
            return ""

        res = ""
        res += str(root.val)

        leftStr = self.tree2str(root.left)
        rightStr = self.tree2str(root.right)

        if leftStr == "" and rightStr == "":
            return res
        elif leftStr == "":
            return res + "()" + "(" + rightStr + ")"
        elif rightStr == "":
            return res + "(" + leftStr + ")"
        else:
            return res + "(" + leftStr + ")" + "(" + rightStr + ")"
