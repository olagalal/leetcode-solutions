class Solution:
    def numTilings(self, n: int) -> int:
        #dynamic programming
        MOD = 10**9 + 7

        dp = [0] * (n + 1)

        for i in range(n + 1):
            if i == 0:
                dp[i] = 1
            elif i == 1 or i == 2:
                dp[i] = i
            elif i == 3:
                dp[i] = 5
            else:
                dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD


        return dp[n]
        