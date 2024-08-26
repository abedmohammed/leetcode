class Solution(object):
    # def addBinary(self, a, b):
    #     length = max(len(a), len(b))
    #     a = a[::-1]
    #     b = b[::-1]
    #     ans = ""

    #     if(len(a) < length):
    #         for i in range(len(a), length):
    #             a += "0"

    #     if(len(b) < length):
    #         for i in range(len(b), length):
    #             b += "0"

    #     remainder = 0
    #     for i in range(length):
    #         digit = int(a[i]) ^ int(b[i]) ^ remainder
    #         remainder = (int(a[i]) and int(b[i])) or (int(a[i]) and remainder) or (int(b[i]) and remainder)
    #         ans += str(digit)

    #     if(remainder):
    #         ans += str(remainder)

    #     return ans[::-1]

    def addBinary(self, a, b):
        answer = ""
        i = len(a) - 1
        j = len(b) - 1

        carry = 0
        while(i >= 0 or j >= 0 or carry):
            if(i >= 0):
                carry += int(a[i])
                i -= 1
            if(j >= 0):
                carry += int(b[j])
                j -= 1

            answer = str(carry % 2) + answer
            carry //= 2

        return answer

answer = Solution()
print(answer.addBinary("1011", "10"))
