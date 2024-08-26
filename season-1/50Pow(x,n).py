class Solution(object):
    def myPow(self, x, n):
        def recursivePow(x, n):
            if n == 1:
                return x

            half = 0

            if n % 2 == 1:
                half = recursivePow(x, (n - 1) // 2)
                return half * half * x
            else:
                half = recursivePow(x, n // 2)
                return half * half

        if n == 0:
            return 1

        exp = recursivePow(x, abs(n))

        if n > 0:
            return exp
        if n < 0:
            return 1 / exp


answer = Solution()
print(answer.myPow(x=2.00000, n=4))
print(answer.myPow(x=2.10000, n=3))
print(answer.myPow(x=2.00000, n=-2))
