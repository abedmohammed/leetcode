class Solution(object):
    def groupAnagrams(self, strs):
        # anagramsHash = {}
        # for word in strs:
        #     sortedWord = "".join(sorted(word))
        #     anagramsHash[sortedWord] = anagramsHash.get(sortedWord, []) + [word]

        # return anagramsHash.values()

        # letterCount = {}
        # for word in strs:
        #     letterCountKey = [0] * 26
        #     for letter in word:
        #         letterCountKey[ord(letter) - ord("a")] += 1

        #     letterCount[tuple(letterCountKey)] = letterCount.get(tuple(letterCountKey), []) + [word]

        # return letterCount.values()

        letterCount = defaultdict(list)
        for word in strs:
            letterCountKey = [0] * 26
            for letter in word:
                letterCountKey[ord(letter) - ord("a")] += 1

            letterCount[tuple(letterCountKey)].append(word)

        return letterCount.values()


"""
# Learnings
- If you are counting numbers, recognize that comparisons or things you can do with it wont be O(N) but O(26)
- ALWAYS REMEMBER THAT IF YOU COUNT CHARACTERS, IS THIS HASH MAP OR KEY INFINITELY LARGE

- defaultfict(list)
- python uses append
- python hashmap keys have to be immutable, so no hash maps or lists, but tuples work

"""
