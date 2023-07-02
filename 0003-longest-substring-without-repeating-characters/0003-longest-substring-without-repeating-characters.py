class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table = {}
        result = 0
        start = 0

        for index, char in enumerate(s):
            if char in table and table[char] >= start:
                start = table[char] + 1
                
            else:
                result = max(result, index - start + 1)
            table[char] = index
        
        return result