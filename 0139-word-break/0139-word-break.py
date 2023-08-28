class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        l = len(s)

        dp = [False]*l

        for i in range(l):
            if s[:i+1] in wordDict:
                dp[i] = True

        for i in range(1, l):
            for k in range(i):
                if dp[k] and s[k+1:i+1] in wordDict:
                    dp[i] = True

        return dp[-1]