class Solution(object):
    def characterReplacement(self, s, k):
        # longest = 1

        # for i in range(len(s)):
        #     for j in range(i+1, len(s)+1):
        #         substring = s[i:j]
        #         appears = {}
        #         most = 0
        #         for letter in substring:
        #             appears[letter] = appears.get(letter, 0) + 1
        #             if(appears[letter] > most):
        #                 most = appears[letter]
        #         if(len(substring) - most <= k):
        #             longest = max(longest, len(substring))
        # return longest

        l, r, window = 0, 0, {}

        mostRepeatedFreq = 0

        while (l < len(s) and r < len(s)):
            character = s[r]
            window[character] = window.get(character, 0) + 1

            mostRepeatedFreq = max(mostRepeatedFreq, window[character])

            if r + 1 - l - mostRepeatedFreq > k:
                window[s[l]] -= 1
                l += 1
            r += 1
        
        return r - l




answer = Solution()
print(answer.characterReplacement("ABABAA", 1))