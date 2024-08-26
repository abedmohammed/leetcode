class Solution(object):
    def largestGoodInteger(self, num):
        largest = ""

        for i in range(2, len(num)):
            if num[i] == num[i - 1] == num[i - 2] and (
                not largest or int(num[i]) > int(largest[0])
            ):
                largest = num[i - 2 : i + 1]

        return largest


answer = Solution()
print(answer.largestGoodInteger(num="8887771333399"))
