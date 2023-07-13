class Solution(object):
    def groupAnagrams(self, strs):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                  43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 107]
        # hash map of anagrams
        anagrams = {}

        # O(N*M logM)
        for str in strs:
            
            # m + mlog(m)
            string_count = 1
            for letter in str:
                string_count *= primes[ord(letter)-96]

            if(string_count in anagrams):
               anagrams[string_count].append(str)
            else:
               anagrams[string_count] = [str]

        # O(N)   
        return list(anagrams.values())



answer = Solution()
print(answer.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))