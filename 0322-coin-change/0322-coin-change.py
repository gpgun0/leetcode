class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = [0] + coins
        n = len(coins)
        dp = [[1e9]*(amount+1) for _ in range(n)]

        for i in range(1, n):
            dp[i][0] = 0
        
        for i in range(1, n):
            coin = coins[i]
            for j in range(1, amount+1):
                if j < coin:
                    dp[i][j] = dp[i-1][j]
                    continue

                dp[i][j] = min(dp[i-1][j-coin] + 1, dp[i][j-coin] + 1, dp[i-1][j])
        
        return dp[-1][-1] if dp[-1][-1] < 1e9 else -1