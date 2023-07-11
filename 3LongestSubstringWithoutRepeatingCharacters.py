class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_length = 0
        window = {}
        left = 0
        right = 0

        # O(N)
        while(right < len(s)):
            # find letter to add to window 
            # O(1)
            letter = s[right]

            # check if letter already exists in window and if its part of the current window
            # O(1)
            if(letter in window and window[letter] >= left):
                # if letter exists in the current window, set the left pointer to the occurence location + 1
                left = window[letter] + 1

            # update the location of the letter in the window
            # O(1)
            window[letter] = right

            # increment right pointer
            # O(1)
            right += 1

            # get maximum length
            # O(1)
            max_length = max(right - left, max_length)
        
        return max_length


answer = Solution()
print(answer.lengthOfLongestSubstring("abcbefcbghij"))

# Time: O(N)
# Space: O(N) technically O(1) since there is a finite number of characters