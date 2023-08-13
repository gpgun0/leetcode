class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []

        def dfs(path):
            if len(path) == n:
                result.append(path[:])
                return
            
            for i in range(n):
                if nums[i] in path:
                    continue
                
                path.append(nums[i])
                dfs(path)
                path.pop()
                
        
        dfs([])

        return result