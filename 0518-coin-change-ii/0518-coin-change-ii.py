class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[1]+[0]*(amount) for _ in range(len(coins))]

        
        for i in range(len(coins)):
            for j in range(1, amount+1):
                if j < coins[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]
        
        return dp[-1][-1]