class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        if m > n:
            text1, text2 = text2, text1
            m, n = n, m

        pre = [0]*(m+1)
        cur = [0]*(m+1)
        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[j-1] == text2[i-1]:
                    cur[j] = pre[j-1]+1
                else:
                    cur[j] = max(cur[j-1], pre[j])

            pre = cur[:]
        
        return pre[-1]