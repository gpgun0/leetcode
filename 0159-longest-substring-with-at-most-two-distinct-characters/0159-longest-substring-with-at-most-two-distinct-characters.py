class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)

        if n == 1:
            return 1

        i = 0
        for k in range(1, n):
            if s[i] != s[k]:
                j = k
                break
            i += 1
        else:
            return len(s)

        answer = j+1
        current_length = j+1
        
        for k in range(j+1, n):
            current_length += 1

            if s[k] != s[i] and s[k] != s[j]:
                start = min(i, j) + 1
                if i < j:
                    i = k
                else:
                    j = k
                current_length = k - start + 1
            
            if s[k] == s[i]:
                i = k
            
            if s[k] == s[j]:
                j = k
            
            answer = max(answer, current_length)

        return answer