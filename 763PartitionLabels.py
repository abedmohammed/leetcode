class Solution(object):
    def partitionLabels(self, s):
        # # Mohammed Solution
        # sCharacters, windowCharacters = {}, {}
        # ans = []

        # for letter in s:
        #     sCharacters[letter] = sCharacters.get(letter, 0) + 1

        # length = 0
        # for i in range(len(s)):
        #     length += 1
        #     windowCharacters[s[i]] = windowCharacters.get(s[i], 0) + 1

        #     if windowCharacters[s[i]] == sCharacters[s[i]]:
        #         windowCharacters.pop(s[i])
        #         sCharacters.pop(s[i])
        #         if not windowCharacters:
        #             ans.append(length)
        #             length = 0

        # return ans

        # # Neetcode Solution
        ans, indexMap, length, end = [], {}, 0, 0

        for i in range(len(s)):
            indexMap[s[i]] = i

        for i in range(len(s)):
            length += 1
            end = max(end, indexMap[s[i]])

            if end == i:
                ans.append(length)
                length = 0

        return ans


answer = Solution()
print(answer.partitionLabels(s="ababcbacadefegdehijhklij"))
print(answer.partitionLabels(s="eccbbbbdec"))
