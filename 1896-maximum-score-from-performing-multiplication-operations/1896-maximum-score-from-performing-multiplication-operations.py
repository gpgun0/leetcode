class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        
        dp = [[0]*m for _ in range(m+1)]

        m_idx = -1
        diff = n-m
        for k in range(n-m, n):
            for i in range(n-k):
                if k == 0:
                    dp[i][i] = nums[i]*multipliers[m_idx]
                    
                else:
                    dp[i][i+k-diff] = max(
                        dp[i][i+k-diff-1] + nums[i+k]*multipliers[m_idx],
                        dp[i+1][i+k-diff] + nums[i]*multipliers[m_idx],
                    )
                
            m_idx -= 1

        return dp[0][m-1]
