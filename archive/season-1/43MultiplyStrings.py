class Solution(object):
    def multiply(self, num1, num2):
        if "0" in [num1, num2]:
            return "0"

        answer = [0 for i in range(len(num1) + len(num2))]

        for i2 in range(len(num2) - 1, -1, -1):
            for i1 in range(len(num1) - 1, -1, -1):
                res = int(num2[i2]) * int(num1[i1]) + answer[i1 + i2 + 1]
                digit = res % 10
                carry = res // 10

                answer[i1 + i2 + 1] = digit
                answer[i1 + i2] += carry

        start = 0
        for num in answer:
            if num != 0:
                break
            start += 1

        return "".join(str(num) for num in answer[start:])


answer = Solution()
print(answer.multiply(num1="123", num2="456"))
print(answer.multiply(num1="341234", num2="23456"))
print(answer.multiply(num1="0", num2="0"))
