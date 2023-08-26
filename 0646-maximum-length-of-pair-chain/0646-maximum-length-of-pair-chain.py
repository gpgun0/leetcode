class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key= lambda x: (x[1], x[0]))

        cur = -1001
        result = 0
        for a, b in pairs:
            if cur < a:
                cur = b
                result += 1
        
        return result