class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        hash_map = defaultdict()
        only_once = 0
        answer = 0

        for word in words:
            reversed_word = word[::-1]

            if hash_map.get(reversed_word):
                if hash_map.get(reversed_word) == 1:
                    hash_map.pop(reversed_word)
                else:
                    hash_map[reversed_word] -= 1
                answer += 4
            
            else:
                if hash_map.get(word):
                    hash_map[word] += 1
                else:
                    hash_map[word] = 1
        
        for key in hash_map:
            if only_once == 0 and key[0] == key[1]:
                answer += 2
                only_once += 1

        return answer