class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)

        if n < d:
            return -1

        INF = int(1e9)
        dp = [[INF]*n for _ in range(d+1)]

        for i in range(n-1, -1, -1):
            dp[d][i] = max(jobDifficulty[i:])

        for day in range(d-1, 0, -1):
            for i in range(day-1, n-(d-day)):
                hardest = 0

                for k in range(i, n-(d-day)):
                    hardest = max(hardest, jobDifficulty[k])
                    dp[day][i] = min(dp[day][i], hardest+dp[day+1][k+1])
                    

        return dp[1][0]