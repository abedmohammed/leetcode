class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        seen = {}
        for i in range(len(s)):
            seen[s[i]] = seen.get(s[i], 0) + 1
            seen[t[i]] = seen.get(t[i], 0) - 1

        for letter in seen:
            if seen[letter] != 0:
                return False

        return True


"""
# Thoughts
Since its an anagram, we know that they have to be the same length, we can use this to our advantage by checking if they are the same length and exiting early

# What if we want to do this in O(1) space?
If they are anagrams and we sort them, they should be the exact same string. This will be an O(nlogn) time and O(1) space.

# REMEMBER
- You can sort strings
- If two things share a property, what does that tell us about them?

"""
