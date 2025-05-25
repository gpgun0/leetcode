class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        hash_map = defaultdict(int)
        answer = 0

        for word in words:
            reversed_word = word[::-1]

            if hash_map[reversed_word]:
                hash_map[reversed_word] -= 1
                answer += 4
            
            else:
                hash_map[word] += 1
        
        if any(k[0] == k[1] for k, v in hash_map.items() if v > 0):
            answer += 2

        return answer