class Solution(object):
    def isPowerOfTwo(self, n):
        for i in range(32):
            if n == 2**i:
                return True

        return False
