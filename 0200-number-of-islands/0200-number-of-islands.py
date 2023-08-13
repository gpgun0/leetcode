class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        result = 0

        def dfs(x, y):
            visited.add((x, y))

            for dx, dy in move:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n \
                    and grid[nx][ny] == "1" \
                    and not (nx, ny) in visited:
                    dfs(nx, ny)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not (i, j) in visited:
                    dfs(i, j)
                    result += 1
        
        return result