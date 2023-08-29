class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0]*2 for _ in range(k+1)] for _ in range(n)]

        def func(i, remain, holding):
            if dp[i][remain][holding]:
                return dp[i][remain][holding]

            if remain == 0:
                dp[i][0][holding] = 0
                return 0

            if i == n-1:
                dp[n-1][remain][holding] = 0
                return 0
            
            if holding:
                dp[i][remain][1] = max(
                    func(i+1, remain-1, 0) + prices[i+1],
                    func(i+1, remain, 1)
                )
                return dp[i][remain][1]
            else:
                dp[i][remain][0] = max(
                    func(i+1, remain, 0),
                    func(i+1, remain, 1) - prices[i+1]
                )
                return dp[i][remain][0]
        
        return max(func(0, k, 0), func(0, k, 1) - prices[0])