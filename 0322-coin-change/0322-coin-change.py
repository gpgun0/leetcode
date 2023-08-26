class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = int(1e9)
        m = len(coins)
        coins = [0]+coins

        dp = [[0]+[INF]*(amount) for _ in range(m+1)]
        answer = INF

        for i in range(1, m+1):
            coin = coins[i]
            for j in range(1, amount+1):
                if j < coin:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-coin]+1)

        if dp[-1][-1] == INF:
            return -1
        return dp[-1][-1]

        