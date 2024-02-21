class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        for i in range(32):
            if left == right:
                return left & right

            left = left & ~(1 << i)
            right = right & ~(1 << i)

        return 0


answer = Solution()
print(answer.rangeBitwiseAnd(left=5, right=7))
