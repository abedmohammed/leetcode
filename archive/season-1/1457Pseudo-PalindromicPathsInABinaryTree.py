class Solution(object):
    def pseudoPalindromicPaths(self, root):
        def dfs(node, mask):
            if not node:
                return 0

            mask[node.val - 1] = (mask[node.val - 1] + 1) % 2

            if not node.left and not node.right:
                return 1 if sum(mask) < 2 else 0

            return dfs(node.left, mask[:]) + dfs(node.right, mask[:])

        return dfs(root, [0 for _ in range(9)])


answer = Solution()
print(answer.pseudoPalindromicPaths(root=[2, 3, 1, 3, 1, null, 1]))
