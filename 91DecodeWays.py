class Solution(object):
    def numDecodings(self, s):
        # previousPaths = {}

        # def dfs(s, i):
        #     paths = 0
        #     if i in previousPaths:
        #         return previousPaths[i]

        #     if not s: return 1
        #     if s[0] == "0": return 0
        #     if len(s) == 1: return 1
            
        #     if int(s[0:2]) <= 26:
        #         paths += dfs(s[2:], i+2)
        #     paths += dfs(s[1:], i+1)

        #     previousPaths[i] = paths
            
        #     return paths
        
        # return dfs(s, 0)

        dp = {len(s): 1}

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]

            if i + 1 < len(s) and int(s[i:i+2]) <= 26 and s[i] != "0":
                dp[i] += dp[i+2]

        return dp[0]
            
            


answer = Solution()
print(answer.numDecodings("226"))
print(answer.numDecodings("11106"))
print(answer.numDecodings("06"))
print(answer.numDecodings("121212"))