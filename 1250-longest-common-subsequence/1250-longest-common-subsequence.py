class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])

                if text2[i-1] == text1[j-1]:
                    dp[i][j] = max(dp[i-1][j-1]+1, dp[i][j])
        
        
        return dp[-1][-1]