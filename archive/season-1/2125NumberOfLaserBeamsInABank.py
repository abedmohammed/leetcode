class Solution(object):
    def numberOfBeams(self, bank):
        layers = []

        for row in bank:
            count = 0
            for num in row:
                count += 1 if num == "1" else 0
            if count > 0:
                layers.append(count)

        res = 0

        for i in range(len(layers) - 1):
            res += layers[i] * layers[i + 1]

        return res


answer = Solution()
print(answer.numberOfBeams(bank=["011001", "000000", "010100", "001000"]))
print(answer.numberOfBeams(bank=["000000", "010101", "010100", "001000"]))
print(answer.numberOfBeams(bank=["011001"]))
