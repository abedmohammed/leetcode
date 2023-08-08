class Solution(object):
    def countSubstrings(self, s):
        # count = 0
        # dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

        # for i in range(len(s)):
        #     dp[i][i] = 1
        #     count += 1
        
        # for j in range(1, len(s)):
        #     for i in range(j-1, -1, -1):
        #         if s[i] != s[j]:
        #             continue 
        #         if j - i <= 1:
        #             dp[i][j] = 1
        #             count += 1
        #         elif dp[i+1][j-1]:
        #             dp[i][j] = 1
        #             count += 1

        
        # print(dp)

        # return count

        count = 0

        for i in range(len(s)):
            left = i
            right = i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

            left = i
            right = i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        return count



ans = Solution()
print(ans.countSubstrings("abc"))
print(ans.countSubstrings("aaa"))
print(ans.countSubstrings("cabada"))
print(ans.countSubstrings("c"))