class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        n = len(s)
        
        def expand(left, right):
            
            while left >= 0 and right < n:
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                else:
                    break
            
            return [left+1, right-1]
        
        for i in range(n):
            left, right = expand(i, i)
            diff = right - left + 1
            
            if diff > len(result):
                result = s[left:right+1]
            
            left, right = expand(i, i+1)
            diff = right - left + 1
            
            if diff > len(result):
                result = s[left:right+1]
            
        return result