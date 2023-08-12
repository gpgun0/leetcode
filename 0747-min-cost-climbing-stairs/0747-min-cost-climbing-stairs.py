class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)+1
        dp = [0]*n
        
        for i in range(1, n):
            if i == 1:
                dp[i] = cost[i-1]
            else:
                dp[i] = cost[i-1] + min(dp[i-1], dp[i-2])
        
        return min(dp[n-1], dp[n-2])