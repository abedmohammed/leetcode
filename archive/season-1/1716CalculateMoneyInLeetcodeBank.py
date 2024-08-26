class Solution(object):
    def totalMoney(self, n):
        count = 0
        weeks = n // 7
        remainderDays = n % 7

        for i in range(remainderDays):
            count += i + weeks + 1

        if weeks > 0:
            count += 28 * weeks + 7 * (weeks * (weeks - 1) // 2)

        return count


answer = Solution()
print(answer.totalMoney(n=4))
print(answer.totalMoney(n=20))
print(answer.totalMoney(n=26))
