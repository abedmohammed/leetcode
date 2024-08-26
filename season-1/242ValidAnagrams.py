class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t): return False

        sHash = {}
        
        for letter in s:
            sHash[letter] = sHash.get(letter, 0) + 1

        for letter in t:
            if letter not in sHash: return False
            sHash[letter] -= 1

        for value in sHash.values():
            if value != 0: return False
            
        return True

        # if len(s) != len(t): return False

        # primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
        # sHash, tHash = 1, 1

        # for i in range(len(s)):
        #     sHash *= primes[ord(s[i]) - ord('a')]
        #     tHash *= primes[ord(t[i]) - ord('a')]

        # return sHash == tHash
            


answer = Solution()
print(answer.isAnagram("bac", "abx"))