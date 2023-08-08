class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            print(dp)
            for word in wordDict:
                wordLength = len(word)

                if wordLength > len(s) - i:
                    continue
                if s[i:i+wordLength] == word:
                    dp[i] = dp[i+wordLength]
                if dp[i]:
                    break

        return dp[0]    


answer = Solution()
# print(answer.wordBreak("leetcode", ["leet","code"]))
# print(answer.wordBreak("applepenapple", ["apple","pen"]))
# print(answer.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))
print(answer.wordBreak("abcd", ["a","abc","b","cd"]))