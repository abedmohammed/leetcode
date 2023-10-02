from collections import deque


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
    def rightSideView(self, root):
        if not root:
            return []
        ans = []
        queue = deque([root])

        while queue:
            currRightest = None
            for i in range(len(queue)):
                currNode = queue.popleft()
                currRightest = currNode.val
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)

            ans.append(currRightest)

        return ans


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
print(answer.rightSideView(tree))
