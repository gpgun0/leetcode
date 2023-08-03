class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        n = len(s)
        
        def expand(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                
            return s[left+1:right-1+1]
        
        for i in range(n):
            odd_window = expand(i, i)
            even_window = expand(i, i+1)
        
            result = max(result, odd_window, even_window, key=len)
            
        return result