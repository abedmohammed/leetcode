class Solution(object):
    def firstPalindrome(self, words):
        for word in words:
            l, r = 0, len(word) - 1

            while word[l] == word[r]:
                l += 1
                r -= 1

                if l >= r:
                    return word

            # if word == word[::-1]:
            #     return word

        return ""


answer = Solution()
print(answer.firstPalindrome(words=["abc", "car", "racecasr", "cool"]))
