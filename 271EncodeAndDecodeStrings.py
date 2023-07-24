class Solution(object):
    def encode(self, strs):
        # sizes = ""
        # for i in range(len(strs) - 1):
        #     sizes += str(len(strs[i])) + ","
        # sizes += str(len(strs[-1])) + ":"
        
        # words = "".join(strs)

        # return sizes + words

        string = ""
        for word in strs:
            string += str(len(word)) + ":" + word
        return string

    def decode(self, str):
        # sizesString = str.split(":")[0]
        # sizes = sizesString.split(",")
        # words = str[len(sizesString)+1:]

        # strs = [""] * len(sizes)
        # last = 0
        # for i in range(len(sizes)):
        #     stringLength = int(sizes[i])
        #     strs[i] = words[last:last+stringLength]
        #     last += stringLength
        # return strs

        # nextLength = str.split(":")[0]
        # strs = []

        # while(nextLength):
        #     str = str[len(nextLength)+1:]
        #     strs.append(str[:int(nextLength)])
        #     str = str[int(nextLength):]
        #     nextLength = str.split(":")[0]

        # return strs
            
        res, i = [], 0
        
        while i < len(str):
            j = i
            while str[j] != ":":
                j += 1
            length = int(str[i:j])
            res.append(str[j + 1: j + 1 + length])
            i = j + 1 + length
        return res


answer = Solution()
encoded = answer.encode(["Hello", "Wor:ld", "Here:::"])
decoded = answer.decode(encoded)

print(encoded)
print(decoded)