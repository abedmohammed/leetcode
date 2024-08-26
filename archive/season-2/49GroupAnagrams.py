class Solution(object):
    def groupAnagrams(self, strs):
        primes = [
            2,
            3,
            5,
            7,
            11,
            13,
            17,
            19,
            23,
            29,
            31,
            37,
            41,
            43,
            47,
            53,
            59,
            61,
            67,
            71,
            73,
            79,
            83,
            89,
            97,
        ]
        groupings = {}

        for word in strs:
            mult = 1
            for char in word:
                mult *= primes[ord(char) - 97]
            groupings[mult] = groupings.get(mult, []) + [word]

        res = []
        for grouping in groupings.values():
            res.append(grouping)

        return res


answer = Solution()
print(answer.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
