class Solution(object):
    def numberOfMatches(self, n):
        count = 0
        while n > 1:
            count += n // 2
            if n % 2 == 0:
                n = n // 2
            else:
                n = n // 2 + 1

        return count


answer = Solution()
print(answer.numberOfMatches(n=7))
print(answer.numberOfMatches(n=14))
print(answer.numberOfMatches(n=1))
