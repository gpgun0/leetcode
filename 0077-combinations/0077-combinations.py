class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(idx, comb):
            if len(comb) == k:
                copied = comb.copy()
                result.append(copied)
                return
            
            for i in range(idx, n+1):
                comb.append(i)

                dfs(i+1, comb)

                comb.pop()
            
        dfs(1, [])

        return result