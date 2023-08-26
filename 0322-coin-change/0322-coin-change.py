class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = int(1e9)
        m = len(coins)
        coins = [0]+coins

        dp = [0] + [INF]*amount

        for i in range(1, m+1):
            coin = coins[i]
            for j in range(coin, amount+1):
                dp[j] = min(dp[j], dp[j-coin]+1)

        if dp[-1] == INF:
            return -1
        return dp[-1]

        