class Solution(object):
    def numRollsToTarget(self, n, k, target):
        MOD = 10**9 + 7
        dp = [0 for _ in range(target + 1)]

        for i in range(1, min(k + 1, target + 1)):
            dp[i] = 1

        for i in range(2, n + 1):
            nextDP = [0 for _ in range(target + 1)]
            for j in range(i, target + 1):
                n = j - 1
                currK = 1
                while currK <= k and n >= i - 1:
                    nextDP[j] += dp[n]
                    n -= 1
                    currK += 1

                nextDP[j] = nextDP[j] % MOD
            dp = nextDP

        return int(dp[-1])


answer = Solution()
print(answer.numRollsToTarget(n=3, k=6, target=7))
# print(answer.numRollsToTarget(n=1, k=6, target=3))
# print(answer.numRollsToTarget(n=30, k=30, target=500))
