class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)

        def dfs(start, candidates, path):
            if sum(path) > target:
                return
            if sum(path) == target:
                result.append(path[:])
            
            for i in range(start, n):
                path.append(candidates[i])
                dfs(i, candidates, path)
                path.pop()
        
        dfs(0, candidates, [])

        return result