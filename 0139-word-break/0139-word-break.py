class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        l = len(s)

        dp = [False]*l

        for i in range(l):
            for word in wordDict:
                if i >= len(word) - 1 and (i == len(word) -1 or dp[i-len(word)]):
                    if s[i-len(word)+1:i+1] == word:
                        dp[i] = True
        
        return dp[-1]
