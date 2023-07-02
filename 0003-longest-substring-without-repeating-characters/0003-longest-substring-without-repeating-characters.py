class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        l = len(s)
        if l == 0:
            return 0

        table = defaultdict(int)
        
        si = ei = 0
        table[s[si]] = 1
        

        while ei < l:
            for i in range(si, ei+1):
                if table[s[i]] > 1:
                    table[s[si]] -= 1
                    si += 1
                    break
            
            else:
                result = max(result, ei-si+1)
                ei += 1
                if ei < l:
                    table[s[ei]] += 1
        
        return result