class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        comb = combinations([i for i in range(1, n+1)], k)
        
        return list(map(list, list(comb)))