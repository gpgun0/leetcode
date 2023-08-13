class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)

        def dfs(start, path):
            if sum(path) > target:
                return
            if sum(path) == target:
                result.append(path[:])
            
            for i in range(start, n):
                dfs(i, path + [candidates[i]])
        
        dfs(0, [])

        return result