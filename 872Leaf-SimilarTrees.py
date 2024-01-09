class Solution(object):
    def leafSimilar(self, root1, root2):
        arr1 = []
        arr2 = []

        def dfs(node, arr):
            if not node:
                return
            if not node.left and not node.right:
                arr.append(node.val)
                return

            dfs(node.left, arr)
            dfs(node.right, arr)

        dfs(root1, arr1)
        dfs(root2, arr2)

        return arr1 == arr2


answer = Solution()
print(
    answer.leafSimilar(
        root1=[3, 5, 1, 6, 2, 9, 8, None, None, 7, 4],
        root2=[3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8],
    )
)
