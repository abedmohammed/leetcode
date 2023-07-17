class Solution(object):
    def minWindow(self, s, t):
        hash = {}
        for letter in t:
            if(letter in hash):
                hash[letter] += 1
            else:
                hash[letter] = 1

        left = 0
        right = -1
        length = len(s)
        minimum = ""

        while(left < length):
            substringComplete = True
            for letter in hash.values():
                if(letter > 0):
                    substringComplete = False
            
            if(not substringComplete):
                right += 1
                if(right > length - 1):
                    return minimum
                letter = s[right]
                if(letter in hash):
                    hash[letter] -= 1
            else:
                sub = s[left:right+1]
                if(len(minimum) > len(sub) or minimum == ""):
                    minimum = sub
                letter = s[left]
                if(letter in hash):
                    hash[letter] += 1
                left += 1

        return minimum
            
        


answer = Solution()
print(answer.minWindow("ADOBECODEBANC", "ABC"))
print(answer.minWindow("AAAAAAAAB", "AB"))
print(answer.minWindow("A", "A"))
print(answer.minWindow("AA", "A"))
print(answer.minWindow("A", "AA"))
print(answer.minWindow("", "A"))