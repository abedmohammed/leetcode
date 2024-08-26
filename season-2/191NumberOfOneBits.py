class Solution(object):
    def hammingWeight(self, n):
        count = 0
        while n > 0:
            count += n & 1
            n = n >> 1

        return count


answer = Solution()
print(answer.hammingWeight(n=0b11111111111111111111111111111101))
