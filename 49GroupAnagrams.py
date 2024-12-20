class Solution(object):
    def groupAnagrams(self, strs):
        # Fun answer T: O(N*M) S: O(N)
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
            101,
        ]

        grouping = {}
        for word in strs:
            primeProduct = 1
            for letter in word:
                primeProduct *= primes[ord(letter) - ord("a")]

            if primeProduct in grouping:
                grouping[primeProduct].append(word)
            else:
                grouping[primeProduct] = [word]

        # # Real Answer T: O(MlogM*N) S: O(N)
        # grouping = {}
        # for word in strs:
        #     sortedWord = "".join(sorted(word))

        #     grouping[sortedWord] = grouping.get(sortedWord, []) + [word]

        # # More Efficient Real Answer T: O(M*N) S: O(N)
        # grouping = {}
        # for word in strs:
        #     letterCount = [0] * 26
        #     for letter in word:
        #         index = ord(letter) - ord("a")
        #         letterCount[index] += 1

        #     grouping[tuple(letterCount)] = grouping.get(tuple(letterCount), []) + [word]

        return grouping.values()
