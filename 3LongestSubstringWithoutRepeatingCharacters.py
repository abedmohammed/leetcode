class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_length = 0
        window = {}
        left = 0
        right = 0

        while(right < len(s)):
            # find letter to add to window
            letter = s[right]

            # check if letter already exists in window and if its part of the current window
            if(letter in window and window[letter] >= left):
                # if letter exists in the current window, set the left pointer to the occurence location + 1
                left = window[letter] + 1

            # update the location of the letter in the window
            window[letter] = right

            # increment right pointer
            right += 1

            # get maximum length
            max_length = max(right - left, max_length)
        
        return max_length


answer = Solution()
print(answer.lengthOfLongestSubstring("abcbefcbghij"))