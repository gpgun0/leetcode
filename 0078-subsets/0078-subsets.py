class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        def dfs(start, path):
            result.append(path[:])

            for i in range(start, n):
                if nums[i] not in path:
                    path.append(nums[i])
                    dfs(i+1, path)
                    path.pop()
        
        dfs(0, [])

        return result