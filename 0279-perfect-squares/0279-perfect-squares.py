class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n+1)

        for i in range(1, floor(n**(1/2))+1):
            dp[i*i] = 1

        for i in range(1, n+1):
            if dp[i]:
                continue

            min_ = 1e9
            
            for j in range(1, floor(i**(1/2))+1):
                min_ = min(min_, dp[i-j*j]+1)
            
            dp[i] = min_

        return dp[n]