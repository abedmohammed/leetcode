class Solution(object):
    def hammingWeight(self, n):
        ans = 0

        while n:
            # ans += n % 2
            # n = n >> 1
            n = n & (n -1)
            res += 1
        return ans


answer = Solution()
print(answer.hammingWeight(00000000000000000000000000001011))