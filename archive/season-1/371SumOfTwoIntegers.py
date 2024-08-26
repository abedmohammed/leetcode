class Solution(object):
    def getSum(self, a, b):
        mask = 0xffffffff
        
        while (b & mask) > 0:
            
            carry = ( a & b ) << 1
            a = (a ^ b) 
            b = carry
        
        # handles overflow
        return (a & mask) if b > 0 else a
            

answer = Solution()
print(answer.getSum(-1, 1))