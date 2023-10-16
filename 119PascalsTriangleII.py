class Solution(object):
    def getRow(self, rowIndex):
        row = [1]

        for i in range(rowIndex):
            nextRow = [0] * (len(row) + 1)
            for j in range(len(row)):
                nextRow[j] += row[j]
                nextRow[j + 1] += row[j]
            row = nextRow

        return row


answer = Solution()
print(answer.getRow(4))
