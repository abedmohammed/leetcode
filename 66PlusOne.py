class Solution(object):
    def plusOne(self, digits):
        carry = 0
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                carry = 1
            else:
                digits[i] += 1
                carry = 0

            if carry == 0:
                break

        if carry == 1:
            digits = [1] + digits

        return digits


answer = Solution()
print(answer.plusOne(digits=[1, 2, 3]))
print(answer.plusOne(digits=[9, 9, 9]))
print(answer.plusOne(digits=[1, 9, 9]))
print(answer.plusOne(digits=[1, 3, 9, 9]))
print(answer.plusOne(digits=[0]))
print(answer.plusOne(digits=[0, 0]))
