class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        indexi, i, indexj, j = 0, 0, 0, 0

        while indexi < len(word1) and indexj < len(word2):
            if word1[indexi][i] != word2[indexj][j]:
                return False

            i += 1
            j += 1

            if i >= len(word1[indexi]):
                i = 0
                indexi += 1
            if j >= len(word2[indexj]):
                j = 0
                indexj += 1

        return indexi == len(word1) and indexj == len(word2)


answer = Solution()
print(answer.arrayStringsAreEqual(word1=["abc", "d", "defg"], word2=["abcddefg"]))
print(answer.arrayStringsAreEqual(word1=["a", "cb"], word2=["ab", "c"]))
