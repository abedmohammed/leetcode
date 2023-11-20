class Solution(object):
    def multiply(self, num1, num2):
        toAdd = []

        for i in range(len(num1) - 1, -1, -1):
            carry = 0
            section = "" + "0" * (len(num1) - i - 1)
            for j in range(len(num2) - 1, -1, -1):
                total = int(num1[i]) * int(num2[j]) + carry
                section = str(total % 10) + section
                carry = total // 10
            if carry > 0:
                section = str(carry) + section
            toAdd.append(section)

        return toAdd


answer = Solution()
print(answer.multiply(num1="123", num2="456"))
