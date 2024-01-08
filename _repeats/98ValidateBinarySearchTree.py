class Solution(object):
    def isValidBST(self, root):
        # arr = []

        # def dfs(node):
        #     if not node:
        #         return

        #     dfs(node.left)
        #     arr.append(node.val)
        #     dfs(node.right)

        # dfs(root)

        # for i in range(1, len(arr)):
        #     if arr[i] <= arr[i - 1]:
        #         return False

        # return True

        def dfs(node, low, high):
            if not node:
                return True

            if node.val <= low or node.val >= high:
                return False

            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        return dfs(root, float("-inf", float("inf")))
