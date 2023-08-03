class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        result = s[0]
        
        for diff in range(1, n):
            for si in range(0, n-diff):
                str_ = s[si:si+diff+1]
                # print(s[si:si+diff+1], ": ", s[si:si+diff+1], end="")
                if str_ == str_[::-1]:
                    result = str_
                    break
        
        return result