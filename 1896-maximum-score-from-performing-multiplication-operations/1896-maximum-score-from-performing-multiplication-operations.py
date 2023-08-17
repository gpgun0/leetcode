class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        
        dp = [[0]*n for _ in range(m+1)]

        m_idx = -1
        for k in range(n-m, n):
            for i in range(n-k):
                if k == 0:
                    dp[i][i] = nums[i]*multipliers[m_idx]
                else:
                    dp[i][i+k] = max(
                        dp[i][i+k-1] + nums[i+k]*multipliers[m_idx],
                        dp[i+1][i+k] + nums[i]*multipliers[m_idx],
                    )
                
            m_idx -= 1

        return dp[0][n-1]











        
        # dp = [[0]*(m) for _ in range(m+1)]

        # m_idx = -1
        # for k in range(n-m, n):
        #     for i in range(0, n-k):
        #         j = i+k
        #         mul = multipliers[m_idx]
        #         if k == 0:
        #             dp[i][j-(n-m)] = nums[i]*mul
        #         else:
        #             dp[i][j-(n-m)] = max(dp[i][j-1-(n-m)] + nums[j]*mul, dp[i+1][j-(n-m)] + nums[i]*mul)
                
        #     m_idx -= 1
            
        # return dp[0][m-1]