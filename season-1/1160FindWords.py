from collections import Counter


class Solution(object):
    def countCharacters(self, words, chars):
        charCount = Counter(chars)

        ans = 0
        for word in words:
            wordCount = dict(charCount)
            tempAns = 0
            for letter in word:
                if letter not in wordCount or wordCount[letter] <= 0:
                    tempAns = 0
                    break
                tempAns += 1
                wordCount[letter] -= 1
            ans += tempAns

        return ans


answer = Solution()
print(answer.countCharacters(words=["cat", "bt", "hat", "tree"], chars="atach"))
print(
    answer.countCharacters(words=["hello", "world", "leetcode"], chars="welldonehoneyr")
)
