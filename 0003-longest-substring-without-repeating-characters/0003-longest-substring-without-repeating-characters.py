class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table = {}
        answer = 0

        left = 0
        for right in range(len(s)):
            char = s[right]
            if char in table and table[char] >= left:
                left = table[char] + 1

            table[char] = right
            answer = max(answer, right-left+1)

        return answer
