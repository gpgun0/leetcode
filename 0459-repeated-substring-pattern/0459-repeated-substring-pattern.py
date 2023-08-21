class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)

        for i in range(1, l//2+1):
            temp = s[:i]

            if l % i == 0:
                if temp * (l//i) == s:
                    return True

        return False