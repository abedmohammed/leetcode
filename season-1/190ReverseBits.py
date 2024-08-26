class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            res = (res << 1) + (n & 1)
            n = n >> 1 
        
        return res



answer = Solution()
# print(answer.reverseBits(43261596))
print(answer.reverseBits(11))