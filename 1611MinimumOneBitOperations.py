class Solution(object):
    def minimumOneBitOperations(self, n):
        if n == 0:
            return 1

        k = 0
        while 2**k <= n:
            k += 1
        k -= 1

        return 2 ** (k + 1) - 1 - self.minimumOneBitOperations(2**k ^ n)


answer = Solution()
print(answer.minimumOneBitOperations(n=6))
