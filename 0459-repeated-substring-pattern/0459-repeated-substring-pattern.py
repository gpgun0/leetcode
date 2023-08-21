class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)

        for i in range(1, l//2+1):
            pre = s[:i]

            for j in range(i, l-i+1, i):
                cur = s[j:j+i]

                if cur == pre:
                    pre = cur
                else:
                    break
            else:
                if j+i == l:
                    return True

        return False