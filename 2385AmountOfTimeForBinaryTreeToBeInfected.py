from collections import deque


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
    def amountOfTime(self, root, start):
        specials = {"fromRoot": 0, "toStart": 0, "fromStart": 0}

        def dfs(node):
            if not node:
                return -1

            l = dfs(node.left)
            r = dfs(node.right)

            res = max(l, r) + 1

            if node == root:
                specials["fromRoot"] = res

            if node.val == start:
                specials["fromStart"] = res

            return res

        def dfsToStart(node, step):
            if not node:
                return

            l = dfsToStart(node.left, step + 1)
            r = dfsToStart(node.right, step + 1)

            if node.val == start:
                specials["toStart"] = step

            return

        dfs(root)
        dfsToStart(root, 0)
        
        return max(specials["fromRoot"] + specials["toStart"], specials["fromStart"])


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
print(answer.amountOfTime(tree, 8))
